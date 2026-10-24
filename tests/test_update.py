"""Exercise the updater without touching real Git remotes or Claude state."""

import json
import os
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class UpdateTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="agent-skills-test-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.repo = self.root / "repo"
        (self.repo / "bin").mkdir(parents=True)
        shutil.copy2(ROOT / "bin/agent-skills", self.repo / "bin/agent-skills")
        skill = self.repo / "skills/example"
        skill.mkdir(parents=True)
        (skill / "SKILL.md").write_text("---\nname: example\ndescription: Example.\n---\n")
        self.home = self.root / "home"
        self.home.mkdir()
        for agent in ("claude", "kilo", "cline"):
            (self.home / f".{agent}").mkdir()
        self.bin = self.root / "bin"
        self.bin.mkdir()
        # A closed PATH makes absent-tool tests independent of the host.
        for name in ("bash", "readlink", "dirname", "mkdir", "basename", "ln", "python3",
                     "mktemp", "date", "mv", "rm", "cat"):
            (self.bin / name).symlink_to(shutil.which(name))
        self.calls = self.root / "calls"
        self.env = {
            **os.environ,
            "HOME": str(self.home),
            "XDG_CONFIG_HOME": str(self.home / ".config"),
            "PATH": str(self.bin),
            "CALLS": str(self.calls),
            "MARKETPLACES": json.dumps([
                {"name": "claude-plugins-official", "source": "github"},
                {"name": "ahmedkishki-skills", "source": "git", "ref": "main"},
            ]),
            "AHEAD": "0",
            "BEHIND": "0",
            "FAIL_LIST": "0",
            "FAIL_REFRESH": "0",
            "FAIL_MERGE": "0",
            "FAIL_PUSH": "0",
        }
        self.executable("git", r"""#!/usr/bin/env bash
printf 'git %s\n' "$*" >> "$CALLS"
shift 2
case "$1" in
fetch) exit 0 ;;
rev-parse) printf 'origin/main\n' ;;
rev-list)
    if [[ "$3" = HEAD..* ]]; then printf '%s\n' "$BEHIND"; else printf '%s\n' "$AHEAD"; fi ;;
merge) exit "$FAIL_MERGE" ;;
push) exit "$FAIL_PUSH" ;;
status) exit 0 ;;
*) exit 99 ;;
esac
""")
        self.executable("claude", r"""#!/usr/bin/env bash
printf 'claude %s\n' "$*" >> "$CALLS"
case "$*" in
'plugin marketplace list --json') printf '%s\n' "$MARKETPLACES"; exit "$FAIL_LIST" ;;
'plugin marketplace update ahmedkishki-skills') exit "$FAIL_REFRESH" ;;
*) exit 99 ;;
esac
""")

    def executable(self, name, text):
        path = self.bin / name
        path.write_text(text)
        path.chmod(0o755)

    def run_update(self, **env):
        result = subprocess.run(
            [str(self.repo / "bin/agent-skills"), "update"],
            env={**self.env, **env}, text=True, capture_output=True, timeout=10,
        )
        calls = self.calls.read_text().splitlines()
        return result, [line for line in calls if line.startswith("claude ")]

    def test_refresh_after_each_successful_git_path(self):
        for ahead, behind in (("0", "0"), ("1", "0"), ("0", "1")):
            with self.subTest(ahead=ahead, behind=behind):
                self.calls.write_text("")
                result, calls = self.run_update(AHEAD=ahead, BEHIND=behind)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual(calls, [
                    "claude plugin marketplace list --json",
                    "claude plugin marketplace update ahmedkishki-skills",
                ])
                for agent in ("claude", "kilo", "cline"):
                    link = self.home / f".{agent}/skills/example"
                    self.assertTrue(link.is_symlink())
                    self.assertEqual(os.readlink(link), str(self.repo / "skills/example"))
                    self.assert_sync_report(result.stdout, self.home / f".{agent}")

    def assert_sync_report(self, output, root):
        lines = [line.lower() for line in output.splitlines() if str(root).lower() in line.lower()]
        self.assertTrue(any("synchronized" in line and "local skill link" in line
                            for line in lines), output)

    def test_present_cli_does_not_materialize_missing_homes(self):
        for agent in ("claude", "kilo", "cline"):
            (self.home / f".{agent}").rmdir()
        self.executable("claude", '#!/usr/bin/env bash\nmkdir -p "$HOME/.claude"\nprintf "claude called\\n" >> "$CALLS"\n')
        result, calls = self.run_update()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(calls, [])
        for root in [self.home / f".{agent}" for agent in ("claude", "kilo", "cline")] + [self.home / ".config/kilo"]:
            self.assertFalse(os.path.lexists(root))
            self.assertTrue(any(str(root) in line and "skipped" in line.lower()
                                for line in result.stdout.splitlines()), result.stdout)

    def test_cli_absent_still_synchronizes_existing_subset_and_xdg(self):
        (self.bin / "claude").unlink()
        (self.home / ".cline").rmdir()
        xdg = self.root / "xdg/kilo"
        xdg.mkdir(parents=True)
        result, calls = self.run_update(XDG_CONFIG_HOME=str(xdg.parent))
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(calls, [])
        self.assertIn("Claude CLI", result.stdout)
        self.assertIn("PATH", result.stdout)
        self.assertNotIn("Claude Code not found", result.stdout + result.stderr)
        for root in (self.home / ".claude", self.home / ".kilo", xdg):
            self.assertTrue((root / "skills/example").is_symlink())
            self.assert_sync_report(result.stdout, root)
        self.assertFalse((self.home / ".cline").exists())

    def test_update_discovers_new_skills_and_removes_only_canonical_stale_links(self):
        result, _ = self.run_update()
        self.assertEqual(result.returncode, 0, result.stderr)
        (self.repo / "skills/example/SKILL.md").unlink()
        new = self.repo / "skills/new-skill"
        new.mkdir()
        (new / "SKILL.md").write_text("new skill\n")
        for agent in ("claude", "kilo", "cline"):
            directory = self.home / f".{agent}/skills"
            directory.mkdir(parents=True, exist_ok=True)
            (directory / "foreign").symlink_to(self.root / "missing")
            (directory / "nested").symlink_to(self.repo / "skills/unrelated/nested")
        result, _ = self.run_update()
        self.assertEqual(result.returncode, 0, result.stderr)
        for agent in ("claude", "kilo", "cline"):
            directory = self.home / f".{agent}/skills"
            self.assertFalse(os.path.lexists(directory / "example"))
            self.assertEqual(os.readlink(directory / "new-skill"), str(new))
            self.assertEqual(os.readlink(directory / "foreign"), str(self.root / "missing"))
            self.assertEqual(os.readlink(directory / "nested"),
                             str(self.repo / "skills/unrelated/nested"))

    def test_unregistered_marketplace_is_not_added(self):
        result, calls = self.run_update(MARKETPLACES='[{"name":"ahmedkishki-skills-other"}]')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("not registered", result.stdout)
        self.assertEqual(calls, ["claude plugin marketplace list --json"])

    def test_real_git_fast_forward_reconciles_all_agents(self):
        git = shutil.which("git")
        if git is None:
            self.skipTest("Git is unavailable")

        def run_git(*args):
            result = subprocess.run(
                [git, "-c", "user.name=Test", "-c", "user.email=test@example.invalid",
                 "-c", "commit.gpgsign=false", *map(str, args)],
                env={**os.environ, "HOME": str(self.home),
                     "XDG_CONFIG_HOME": self.env["XDG_CONFIG_HOME"], "GIT_CONFIG_NOSYSTEM": "1"},
                text=True, capture_output=True, timeout=10,
            )
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

        remote = self.root / "remote.git"
        run_git("init", "--bare", remote)
        run_git("init", "-b", "main", self.repo)
        run_git("-C", self.repo, "add", ".")
        run_git("-C", self.repo, "commit", "-m", "Initial skills")
        run_git("-C", self.repo, "remote", "add", "origin", remote)
        run_git("-C", self.repo, "push", "-u", "origin", "main")
        publisher = self.root / "publisher"
        run_git("clone", "-b", "main", remote, publisher)
        (self.bin / "git").unlink()
        (self.bin / "git").symlink_to(git)
        result, _ = self.run_update()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        (publisher / "skills/example/SKILL.md").unlink()
        (publisher / "skills/new").mkdir()
        (publisher / "skills/new/SKILL.md").write_text("new skill\n")
        run_git("-C", publisher, "add", "-A")
        run_git("-C", publisher, "commit", "-m", "Replace skill")
        run_git("-C", publisher, "push")
        result, _ = self.run_update()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        for agent in ("claude", "kilo", "cline"):
            directory = self.home / f".{agent}/skills"
            self.assertFalse(os.path.lexists(directory / "example"))
            self.assertEqual(os.readlink(directory / "new"), str(self.repo / "skills/new"))

    def test_missing_optional_tools(self):
        for tool in ("claude", "python3"):
            with self.subTest(tool=tool):
                original = self.bin / tool
                original.rename(self.root / tool)
                self.calls.write_text("")
                result, calls = self.run_update()
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertIn("refresh skipped", result.stdout)
                self.assertIn("claude plugin marketplace update ahmedkishki-skills", result.stdout)
                self.assertEqual(calls, [])
                for agent in ("claude", "kilo", "cline"):
                    self.assertTrue((self.home / f".{agent}/skills/example").is_symlink())
                    self.assert_sync_report(result.stdout, self.home / f".{agent}")
                (self.root / tool).rename(original)

    def test_failed_or_invalid_lookup_never_refreshes(self):
        for env in (
            {"FAIL_LIST": "1"}, {"MARKETPLACES": "not JSON"},
            {"MARKETPLACES": "{}"}, {"MARKETPLACES": "[{}]"},
        ):
            with self.subTest(env=env):
                self.calls.write_text("")
                result, calls = self.run_update(**env)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("lookup failed", result.stderr)
                self.assertEqual(calls, ["claude plugin marketplace list --json"])

    def test_failed_refresh_reports_partial_success_and_remedy(self):
        result, calls = self.run_update(FAIL_REFRESH="1")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Git/link update finished", result.stderr)
        self.assertIn("claude plugin marketplace update ahmedkishki-skills", result.stderr)
        self.assertEqual(len(calls), 2)

    def test_git_failure_never_links_skills_or_refreshes_marketplace(self):
        for env in (
            {"AHEAD": "1", "BEHIND": "1"},
            {"BEHIND": "1", "FAIL_MERGE": "1"},
            {"AHEAD": "1", "FAIL_PUSH": "1"},
        ):
            with self.subTest(env=env):
                self.calls.write_text("")
                result, calls = self.run_update(**env)
                self.assertNotEqual(result.returncode, 0)
                self.assertEqual(calls, [])
                for agent in ("claude", "kilo", "cline"):
                    self.assertFalse((self.home / f".{agent}/skills").exists())


class MarketplaceTests(unittest.TestCase):
    def test_every_skill_is_independently_discoverable(self):
        marketplace = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text())
        skills = {path.parent.name for path in (ROOT / "skills").glob("*/SKILL.md")}
        plugins = marketplace["plugins"]
        self.assertEqual({plugin["name"] for plugin in plugins}, skills)
        self.assertEqual(len(plugins), len(skills))
        for plugin in plugins:
            with self.subTest(plugin=plugin["name"]):
                self.assertEqual(plugin["source"], f'./skills/{plugin["name"]}')
                source = ROOT / plugin["source"]
                manifest = json.loads((source / ".claude-plugin/plugin.json").read_text())
                self.assertEqual(manifest["name"], plugin["name"])
                self.assertEqual(manifest["skills"], ["./"])
                self.assertTrue((source / "SKILL.md").is_file())


if __name__ == "__main__":
    unittest.main()
