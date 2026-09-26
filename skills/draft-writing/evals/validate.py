"""Check skill structure and test definitions; does not run model evaluations."""

import json
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
MODULES = {"thesis", "source-mapping", "plan", "white-box-synthesis", "drafting", "progress"}


class SkillChecks(unittest.TestCase):
    def test_reference_modules(self):
        self.assertEqual({p.stem for p in (ROOT / "references").glob("*.md")}, MODULES)

    def test_frontmatter_and_links(self):
        for path in [ROOT / "SKILL.md", *sorted((ROOT / "references").glob("*.md"))]:
            with self.subTest(path=path.name):
                text = path.read_text()
                front = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
                self.assertIsNotNone(front)
                fields = dict(line.split(":", 1) for line in front[1].splitlines())
                self.assertEqual(set(fields), {"name", "description"})
                expected = "draft-writing" if path.name == "SKILL.md" else path.name
                self.assertEqual(fields["name"].strip(), expected)
                self.assertTrue(fields["description"].strip())
                self.assertEqual(len(re.findall(r"^# ", text, re.M)), 1)
                for link in re.findall(r"\]\(([^)]+)\)", text):
                    self.assertTrue((path.parent / link).is_file(), link)

    def test_no_obsolete_templates(self):
        text = "\n".join(p.read_text() for p in [ROOT / "SKILL.md", *(ROOT / "references").glob("*.md")])
        for template in ("{project}-arguments.md", "{project}-material.md", "{project}-user-material.md"):
            self.assertNotIn(template, text)
        self.assertNotRegex(text, r"ARG-\d+")

    def test_release(self):
        version = (ROOT / "version").read_text().strip()
        self.assertRegex(version, r"^\d+\.\d+\.\d+$")
        self.assertIn(f"## {version} —", (ROOT / "changelog.md").read_text())
        self.assertIn("white-box synthesis", (ROOT / "agents/openai.yaml").read_text())

    def test_behavioural_case_schema(self):
        data = json.loads((ROOT / "evals/evals.json").read_text())
        self.assertEqual(data["skill_name"], "draft-writing")
        cases = data["evals"]
        self.assertGreaterEqual(len(cases), 25)
        self.assertEqual(len({c["id"] for c in cases}), len(cases))
        for case in cases:
            with self.subTest(case=case["id"]):
                self.assertIsInstance(case["id"], int)
                for key in ("prompt", "expected_output"):
                    self.assertIsInstance(case[key], str)
                    self.assertTrue(case[key].strip())
                self.assertIsInstance(case["files"], list)
                self.assertTrue(case["expectations"])
                self.assertTrue(all(isinstance(e, str) and e.strip() for e in case["expectations"]))

    def test_required_safeguards(self):
        synthesis = (ROOT / "references/white-box-synthesis.md").read_text()
        for operation in ("COPY", "DELETE", "ORDER", "INFLECT", "NORMALISE"):
            self.assertIn(f"**{operation}:**", synthesis)
        for requirement in ("every sentence", "exact copied span", "author, source and locator", "permanently ineligible"):
            self.assertIn(requirement, synthesis)
        drafting = (ROOT / "references/drafting.md").read_text()
        for requirement in ("missing definitions", "first-use citations", "local numbering", "separate user-wording section"):
            self.assertIn(requirement, drafting)
        self.assertIn("Do not migrate an existing project", (ROOT / "SKILL.md").read_text())


if __name__ == "__main__":
    unittest.main(verbosity=2)