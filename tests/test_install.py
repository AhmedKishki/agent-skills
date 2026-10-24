"""Installation contracts in an isolated home, without any agent binaries."""

import os
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AGENTS = ("claude", "kilo", "cline")


class InstallTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix="agent skills install-")
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.repo = self.root / "repo"
        (self.repo / "bin").mkdir(parents=True)
        shutil.copy2(ROOT / "bin/agent-skills", self.repo / "bin/agent-skills")
        self.home = self.root / "home"
        self.home.mkdir()
        self.bin = self.root / "bin"
        self.bin.mkdir()
        for name in ("bash", "readlink", "dirname", "mkdir", "basename", "ln",
                     "mktemp", "date", "mv", "rm"):
            (self.bin / name).symlink_to(shutil.which(name))
        self.env = {**os.environ, "HOME": str(self.home), "PATH": str(self.bin),
                    "XDG_CONFIG_HOME": str(self.home / ".config")}
        for name in ("alpha", "beta"):
            directory = self.repo / "skills" / name
            directory.mkdir(parents=True)
            (directory / "SKILL.md").write_text(f"---\nname: {name}\ndescription: Test.\n---\n")
        (self.repo / "skills/not-a-skill").mkdir()

    def install(self, **env):
        result = subprocess.run([str(self.repo / "bin/agent-skills"), "install"],
                                env={**self.env, **env}, capture_output=True,
                                text=True, timeout=10)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        return result.stdout + result.stderr

    def assert_links(self):
        for agent in AGENTS:
            directory = self.home / f".{agent}/skills"
            for name in ("alpha", "beta"):
                self.assertEqual(os.readlink(directory / name), str(self.repo / "skills" / name))
            self.assertFalse(os.path.lexists(directory / "not-a-skill"))

    def test_install_without_agents_is_idempotent_and_warns_about_path(self):
        sentinels = {}
        for relative in (".bashrc", ".profile", ".zshrc", ".config/kilo/kilo.jsonc",
                         ".claude/settings.json", ".cline/settings.json"):
            path = self.home / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("unchanged sentinel\n")
            sentinels[path] = path.read_bytes()
        before = {p.relative_to(self.home) for p in self.home.rglob("*") if p.is_file()}
        output = self.install()
        self.assertIn("PATH", output)
        self.assertIn(str(self.home / ".local/bin"), output)
        self.assert_links()
        command = self.home / ".local/bin/agent-skills"
        self.assertEqual(command.resolve(), self.repo / "bin/agent-skills")
        output = self.install(PATH=f"{self.home / '.local/bin'}:{self.bin}")
        self.assertNotIn("PATH", output)
        self.assert_links()
        self.assertFalse(any(self.home.glob(".*/skill-backups/*")))
        for path, content in sentinels.items():
            self.assertEqual(path.read_bytes(), content)
        after = {p.relative_to(self.home) for p in self.home.rglob("*")
                 if p.is_file() and not p.is_symlink()}
        self.assertEqual(after, before)

    def test_installed_command_discovers_additions_and_exposes_edits(self):
        self.install()
        added = self.repo / "skills/new-skill"
        added.mkdir()
        (added / "SKILL.md").write_text("new instructions\n")
        (self.repo / "skills/alpha/SKILL.md").write_text("updated instructions\n")
        result = subprocess.run(
            [str(self.home / ".local/bin/agent-skills"), "install"],
            env=self.env, capture_output=True, text=True, timeout=10,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        for agent in AGENTS:
            directory = self.home / f".{agent}/skills"
            self.assertEqual(os.readlink(directory / "new-skill"), str(added))
            self.assertEqual((directory / "alpha/SKILL.md").read_text(), "updated instructions\n")

    def test_conflicts_are_preserved_in_unique_backup_directories(self):
        # Freeze date so repeated runs cannot rely on second-resolution names.
        (self.bin / "date").unlink()
        date = self.bin / "date"
        date.write_text("#!/usr/bin/env bash\nprintf '20261024T120000\\n'\n")
        date.chmod(0o755)
        for iteration, kind in enumerate(("file", "directory", "link", "broken")):
            for agent in AGENTS:
                directory = self.home / f".{agent}/skills"
                directory.mkdir(parents=True, exist_ok=True)
                conflict = directory / "alpha"
                if conflict.is_symlink():
                    conflict.unlink()
                if kind == "file":
                    conflict.write_text("original file")
                elif kind == "directory":
                    conflict.mkdir()
                    (conflict / "payload").write_text("original directory")
                else:
                    target = self.root / ("existing" if kind == "link" else "missing")
                    if kind == "link":
                        target.mkdir(exist_ok=True)
                    conflict.symlink_to(target)
            self.install()
            self.assert_links()
            for agent in AGENTS:
                backups = list((self.home / f".{agent}/skill-backups").glob("*/alpha"))
                self.assertEqual(len(backups), iteration + 1)
                self.assertEqual(sum(p.is_symlink() for p in backups), max(0, iteration - 1))
                self.assertTrue(any(not p.is_symlink() and p.is_file()
                                    and p.read_text() == "original file" for p in backups))
                if iteration >= 1:
                    self.assertTrue(any(p.is_dir() and (p / "payload").is_file()
                                        and (p / "payload").read_text() == "original directory"
                                        for p in backups))
                for previous in ("existing", "missing")[:max(0, iteration - 1)]:
                    self.assertTrue(any(p.is_symlink() and os.readlink(p) == str(self.root / previous)
                                        for p in backups))

    def test_stale_cleanup_preserves_unrelated_entries(self):
        self.install()
        (self.repo / "skills/alpha/SKILL.md").unlink()
        shutil.rmtree(self.repo / "skills/beta")
        for agent in AGENTS:
            directory = self.home / f".{agent}/skills"
            (directory / "personal").mkdir()
            (directory / "personal/note").write_text("keep")
            (directory / "file").write_text("keep file")
            (directory / "foreign").symlink_to(self.root / "missing")
            (directory / "nested").symlink_to(self.repo / "skills/alpha/missing")
            (directory / "alias").symlink_to(self.repo / "skills/alpha")
        self.install()
        for agent in AGENTS:
            directory = self.home / f".{agent}/skills"
            for name in ("alpha", "beta"):
                self.assertFalse(os.path.lexists(directory / name))
            self.assertEqual((directory / "personal/note").read_text(), "keep")
            self.assertEqual((directory / "file").read_text(), "keep file")
            for name, target in (("foreign", self.root / "missing"),
                                 ("nested", self.repo / "skills/alpha/missing"),
                                 ("alias", self.repo / "skills/alpha")):
                self.assertEqual(os.readlink(directory / name), str(target))
