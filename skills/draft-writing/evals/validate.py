"""Validate skill files, Markdown links and case definitions, not model behaviour."""

import json
from pathlib import Path
import re
from tempfile import TemporaryDirectory
import unittest
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
REFERENCES = ROOT / "references"
MODULES = {
    "article/thesis-and-vision.md", "article/requirements.md", "article/plan.md",
    "section/arc.md", "section/progress.md", "section/material.md", "section/draft.md",
    "supplement/source-maps.md",
    "tools/white-box-synthesis.md", "tools/smoothing.md", "tools/ai-authored.md",
    "rules/user-prompts.md", "rules/decisions.md", "rules/retention.md",
}


def prose(text):
    """Exclude fenced examples: their placeholder paths are not installed files."""
    lines = []
    fence = None
    for line in text.splitlines():
        marker = re.match(r"^\s*(`{3,}|~{3,})(.*)$", line)
        if fence:
            if (marker and marker[1][0] == fence[0]
                    and len(marker[1]) >= len(fence) and not marker[2].strip()):
                fence = None
        elif marker:
            fence = marker[1]
        else:
            lines.append(line)
    return "\n".join(lines)


def anchors(text):
    """Resolve the plain Markdown heading style used by this skill and its IDs."""
    found = set()
    for heading in re.findall(r"^#{1,6}\s+(.+?)\s*#*\s*$", prose(text), re.M):
        slug = re.sub(r"[^\w\- ]", "", heading.lower()).replace(" ", "-")
        candidate = slug
        suffix = 1
        while candidate in found:
            candidate = f"{slug}-{suffix}"
            suffix += 1
        found.add(candidate)
    return found


def link_errors(path):
    errors = []
    for link in re.findall(r"\]\(([^)]+)\)", prose(path.read_text(encoding="utf-8"))):
        url = urlsplit(link)
        if url.scheme in {"http", "https", "mailto"}:
            continue
        target = (path.parent / unquote(url.path)).resolve() if url.path else path
        if not target.is_file():
            errors.append(f"{path}: missing file for {link}")
        elif url.fragment and unquote(url.fragment) not in anchors(target.read_text(encoding="utf-8")):
            errors.append(f"{path}: missing anchor for {link}")
    return errors


class LinkChecks(unittest.TestCase):
    def setUp(self):
        temporary = TemporaryDirectory(prefix="draft-writing-links-")
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        (self.root / "nested").mkdir()
        self.source = self.root / "nested/source.md"
        (self.root / "target.md").write_text("# Target\n## MAT-001\n## Local Identifiers\n", encoding="utf-8")

    def check_links(self, text):
        self.source.write_text(text, encoding="utf-8")
        return link_errors(self.source)

    def test_nested_path_and_heading(self):
        self.assertEqual(self.check_links("[IDs](../target.md#local-identifiers)"), [])

    def test_hyphenated_id(self):
        self.assertEqual(self.check_links("[Material](../target.md#mat-001)"), [])

    def test_same_file_fragment(self):
        self.assertEqual(self.check_links("# Source\n## U-001\n[Input](#u-001)"), [])

    def test_missing_file(self):
        self.assertIn("missing file", self.check_links("[Bad](missing.md)")[0])

    def test_missing_fragment(self):
        self.assertIn("missing anchor", self.check_links("[Bad](../target.md#mat-002)")[0])
        self.assertIn("missing anchor", self.check_links("# Source\n[Bad](#u-001)")[0])

    def test_fenced_examples_and_external_urls(self):
        self.assertEqual(self.check_links(
            "[Web](https://example.org)\n```markdown\n[Example](missing.md)\n```\n"
            "~~~markdown\n[Example](missing.md)\n~~~\n"
        ), [])

    def test_example_heading_is_not_an_anchor(self):
        self.assertIn("missing anchor", self.check_links("```markdown\n## U-001\n```\n[Bad](#u-001)")[0])


class SkillChecks(unittest.TestCase):
    def test_reference_modules(self):
        self.assertEqual({p.relative_to(REFERENCES).as_posix() for p in REFERENCES.rglob("*.md")}, MODULES)

    def test_frontmatter_and_h1(self):
        for path in [ROOT / "SKILL.md", *(REFERENCES / name for name in sorted(MODULES))]:
            with self.subTest(path=path.name):
                text = path.read_text(encoding="utf-8")
                front = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
                self.assertIsNotNone(front)
                entries = [line.split(":", 1) for line in front[1].splitlines()]
                self.assertTrue(all(len(entry) == 2 for entry in entries))
                fields = {key.strip(): value.strip().strip('"') for key, value in entries}
                self.assertEqual(len(entries), 2)
                self.assertEqual(set(fields), {"name", "description"})
                self.assertEqual(fields["name"], "draft-writing" if path.name == "SKILL.md" else path.name)
                self.assertTrue(fields["description"])
                self.assertEqual(len(re.findall(r"^# ", prose(text), re.M)), 1)

    def test_links_and_entry_routes(self):
        entry = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        for name in sorted(MODULES):
            self.assertIn(f"(references/{name})", entry)
        for path in [ROOT / "SKILL.md", *(REFERENCES / name for name in sorted(MODULES))]:
            with self.subTest(path=path):
                self.assertEqual(link_errors(path), [])

    def test_no_obsolete_templates(self):
        text = "\n".join(p.read_text(encoding="utf-8") for p in [ROOT / "SKILL.md", *REFERENCES.rglob("*.md")])
        for template in ("{project}-arguments.md", "{project}-material.md", "{project}-user-material.md"):
            self.assertNotIn(template, text)
        self.assertNotRegex(text, r"ARG-\d+")

    def test_documented_safeguards(self):
        # Presence checks protect the contract; behavioural compliance needs model runs.
        required = {
            "tools/white-box-synthesis.md": [
                "every sentence", "exact copied span", "author, source and locator",
                "permanently ineligible", "relations dependent on them",
                *[f"**{op}:**" for op in ("COPY", "DELETE", "ORDER", "INFLECT", "NORMALISE")],
            ],
            "tools/ai-authored.md": ["⟦AI-AUTHORED: exact wording⟧", "material-section-n.md", "Direct insertion", "permanently ineligible", "stricter project rule"],
            "tools/smoothing.md": ["one bounded amendment", "before-and-after", "fresh", "approval"],
            "section/draft.md": ["missing definitions", "first-use citations", "section-local numbering", "Material approval alone is not insertion approval"],
            "section/progress.md": ["Local Identifiers", "Never reuse", "approved but unsaved"],
            "rules/decisions.md": ["dismissed question", "one focused question", "completed write"],
            "rules/retention.md": ["uncommitted", "recoverable", "release-history exception"],
        }
        for name, phrases in required.items():
            text = (REFERENCES / name).read_text(encoding="utf-8").lower()
            for phrase in phrases:
                with self.subTest(module=name, phrase=phrase):
                    self.assertIn(phrase.lower(), text)
        entry = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("Do not migrate an existing project", entry)
        self.assertIn("established owners, identifiers and provenance restrictions", entry)

    def test_release(self):
        version = (ROOT / "version").read_text().strip()
        self.assertRegex(version, r"^\d+\.\d+\.\d+$")
        self.assertIn(f"## {version} —", (ROOT / "changelog.md").read_text(encoding="utf-8"))
        metadata = (ROOT / "agents/openai.yaml").read_text()
        self.assertIn("white-box synthesis", metadata)
        for icon in re.findall(r'icon_(?:small|large): "([^"]+)"', metadata):
            self.assertTrue((ROOT / icon).is_file())

    def test_marketplace(self):
        path = ROOT.parents[1] / ".claude-plugin/marketplace.json"
        if not path.is_file():
            self.skipTest("Standalone skill has no repository marketplace")
        plugins = json.loads(path.read_text())["plugins"]
        entries = [plugin for plugin in plugins if plugin["name"] == "draft-writing"]
        self.assertEqual(len(entries), 1)
        self.assertEqual(entries[0]["source"], "./skills/draft-writing")
        self.assertNotIn("version", entries[0])
        self.assertIn("isolated sections", entries[0]["description"])

    def test_behavioural_case_schema(self):
        data = json.loads((ROOT / "evals/evals.json").read_text(encoding="utf-8"))
        self.assertEqual(data["skill_name"], "draft-writing")
        cases = data["evals"]
        self.assertGreaterEqual(len(cases), 41)
        self.assertEqual(len({case["id"] for case in cases}), len(cases))
        for case in cases:
            with self.subTest(case=case["id"]):
                self.assertIs(type(case["id"]), int)
                for key in ("prompt", "expected_output"):
                    self.assertIsInstance(case[key], str)
                    self.assertTrue(case[key].strip())
                self.assertIsInstance(case["files"], list)
                for filename in case["files"]:
                    self.assertTrue((ROOT / filename).is_file())
                self.assertTrue(case["expectations"])
                self.assertTrue(all(isinstance(e, str) and e.strip() for e in case["expectations"]))


if __name__ == "__main__":
    unittest.main(verbosity=2)
