import ast
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class PackageTests(unittest.TestCase):
    def test_frontmatter_and_plugin(self):
        skill = (ROOT / "SKILL.md").read_text()
        self.assertTrue(skill.startswith("---\nname: auto-jobber\n"))
        self.assertRegex(skill, r"(?m)^description: .+")
        plugin = json.loads((ROOT / ".claude-plugin" / "plugin.json").read_text())
        self.assertEqual("auto-jobber", plugin["name"])
        self.assertIn("./", plugin["skills"])

    def test_all_package_text_files_are_short_and_valid(self):
        for path in ROOT.rglob("*"):
            if not path.is_file() or "__pycache__" in path.parts:
                continue
            with self.subTest(path=str(path.relative_to(ROOT))):
                text = path.read_text(encoding="utf-8")
                self.assertLessEqual(len(text.splitlines()), 100)
                if path.suffix == ".py":
                    ast.parse(text, filename=str(path))
                if path.suffix == ".json":
                    json.loads(text)

    def test_relative_markdown_links_and_direct_reference_routing(self):
        skill = (ROOT / "SKILL.md").read_text()
        for path in ROOT.rglob("*.md"):
            text = path.read_text()
            for link in re.findall(r"\]\(([^)]+)\)", text):
                if not re.match(r"\w+://|#", link):
                    self.assertTrue((path.parent / link.split("#")[0]).exists(), str(path) + ": " + link)
        for path in (ROOT / "references").glob("*.md"):
            self.assertIn(f"references/{path.name}", skill)


if __name__ == "__main__":
    unittest.main()
