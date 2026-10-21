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
        self.bin = self.root / "bin"
        self.bin.mkdir()
        # A closed PATH makes absent-tool tests independent of the host.
        for name in ("bash", "readlink", "dirname", "mkdir", "basename", "ln", "python3"):
            (self.bin / name).symlink_to(shutil.which(name))
        self.calls = self.root / "calls"
        self.env = {
            **os.environ,
            "HOME": str(self.home),
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
                self.assertEqual(
                    (self.home / ".claude/skills/example").resolve(),
                    self.repo / "skills/example",
                )

    def test_unregistered_marketplace_is_not_added(self):
        result, calls = self.run_update(MARKETPLACES='[{"name":"ahmedkishki-skills-other"}]')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("not registered", result.stdout)
        self.assertEqual(calls, ["claude plugin marketplace list --json"])

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

    def test_git_failure_never_touches_claude(self):
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
                self.assertFalse((self.home / ".claude/skills").exists())


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
