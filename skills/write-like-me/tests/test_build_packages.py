import importlib.util
import tempfile
import unittest
import zipfile
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parents[1]
SCRIPT = SKILL_ROOT / "scripts" / "build_packages.py"
SPEC = importlib.util.spec_from_file_location("build_packages", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MODULE)


class BuildPackagesTests(unittest.TestCase):
    def test_platform_packages_are_separate_and_valid(self):
        with tempfile.TemporaryDirectory() as directory:
            result = MODULE.build(Path(directory))
            claude = Path(result["claude"]["path"])
            openai = Path(result["openai"]["path"])
            source = Path(result["source"]["path"])
            self.assertTrue(claude.exists())
            self.assertTrue(openai.exists())
            self.assertTrue(source.exists())
            with zipfile.ZipFile(claude) as archive:
                claude_names = set(archive.namelist())
                claude_entries = archive.infolist()
            with zipfile.ZipFile(openai) as archive:
                openai_names = set(archive.namelist())
            with zipfile.ZipFile(source) as archive:
                source_names = set(archive.namelist())
            self.assertIn("write-like-me/SKILL.md", claude_names)
            self.assertTrue(all(
                entry.date_time == MODULE.FIXED_ZIP_TIMESTAMP
                for entry in claude_entries
            ))
            self.assertNotIn("write-like-me/agents/openai.yaml", claude_names)
            self.assertNotIn("write-like-me/evaluations/beta/README.md", claude_names)
            self.assertIn("write-like-me/.codex-plugin/plugin.json", openai_names)
            self.assertIn("write-like-me/ACKNOWLEDGEMENTS.md", openai_names)
            self.assertIn("write-like-me/LICENSE", openai_names)
            self.assertIn("write-like-me/PRIVACY.md", openai_names)
            self.assertIn("write-like-me/README.md", openai_names)
            self.assertIn("write-like-me/TERMS.md", openai_names)
            self.assertIn("write-like-me/skills/write-like-me/SKILL.md", openai_names)
            self.assertIn("write-like-me/skills/write-like-me/scripts/build_starter_voice_file.py", openai_names)
            self.assertIn("write-like-me/skills/write-like-me/scripts/verify_rewrite.py", openai_names)
            self.assertIn("write-like-me/skills/write-like-me/scripts/update_writing_pattern.py", openai_names)
            self.assertNotIn("write-like-me/skills/write-like-me/evaluations/beta/README.md", openai_names)
            self.assertNotIn("write-like-me/skills/write-like-me/scripts/run_blind_beta.py", openai_names)
            self.assertNotIn("write-like-me/skills/write-like-me/tests/test_build_packages.py", openai_names)
            self.assertIn("write-like-me/skills/write-like-me/evaluations/beta/README.md", source_names)
            self.assertIn("write-like-me/skills/write-like-me/scripts/run_blind_beta.py", source_names)
            self.assertIn("write-like-me/skills/write-like-me/tests/test_build_packages.py", source_names)
            self.assertFalse(any("/.git/" in name for name in source_names))
            self.assertFalse(any("/node_modules/" in name for name in source_names))
            self.assertFalse(any(name.endswith(".zip") for name in source_names))
            self.assertNotIn("write-like-me/SOCIAL-LAUNCH.md", source_names)
            manifest = MODULE.public_manifest(result)
            self.assertEqual(
                manifest["claude"]["file"],
                claude.name,
            )
            self.assertNotIn("/", manifest["claude"]["file"])
            with tempfile.TemporaryDirectory() as second_directory:
                second = MODULE.build(Path(second_directory))
            self.assertEqual(
                result["claude"]["sha256"],
                second["claude"]["sha256"],
            )
            self.assertEqual(
                result["openai"]["sha256"],
                second["openai"]["sha256"],
            )

    def test_runtime_only_build_works_inside_the_repository(self):
        output_dir = SKILL_ROOT.parents[1] / "website" / "public" / "downloads"
        result = MODULE.build(output_dir, include_source=False)
        self.assertEqual(set(result), {"claude", "openai"})
        self.assertTrue(Path(result["claude"]["path"]).is_file())
        self.assertTrue(Path(result["openai"]["path"]).is_file())


if __name__ == "__main__":
    unittest.main()
