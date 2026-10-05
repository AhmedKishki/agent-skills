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


OWNER_MODULES = {
    "article/thesis-and-vision.md": (
        (r"motivation|thesis", r"theory|commitment|scope"),
        (r"\brequirements\b", r"\bplan\b", r"\bdraft\b"),
    ),
    "article/requirements.md": (
        (r"audience", r"voice|style", r"citation"),
        (r"thesis-and-vision", r"\bplan\b", r"\bdraft\b"),
    ),
    "article/plan.md": (
        (r"section order|article order", r"sequence", r"current.section"),
        (r"\barc\b", r"\bprogress\b", r"\bmaterial\b"),
    ),
    "section/arc.md": (
        (r"passage", r"purpose", r"connection|order"),
        (r"\bmaterial\b", r"\bprogress\b", r"\bdraft\b"),
    ),
    "section/progress.md": (
        (r"resume|handoff|current", r"approval", r"\bstate\b", r"blocker|counter"),
        (r"source maps?", r"\bmaterial\b", r"\barc\b"),
    ),
    "section/material.md": (
        (r"constraint|condition", r"approved", r"basis|provenance"),
        (r"source maps?", r"\barc\b", r"\bdraft\b"),
    ),
    "section/draft.md": (
        (r"prose|passage", r"footnote|note marker", r"marker"),
        (r"\bmaterial\b", r"\barc\b", r"\brequirements\b"),
    ),
    "supplement/source-maps.md": (
        (r"excerpt", r"locator"),
        (r"\bmaterial\b", r"\bdraft\b", r"\bprogress\b"),
    ),
}

ENTRY_GATE = {
    "allowlist": (r"allow\s*list|\ballowed\b",),
    "rejects unlisted content": (
        r"reject|refuse|absent|not allowed|prohibit|do not write|cannot enter|only listed",
    ),
    "author override": (r"override|except", r"author|user"),
    "no implicit owner": (r"no implicit|do(?:es)? not create|never create", r"owner"),
    "no breadcrumb substitute": (
        r"breadcrumb|in place of the content|substitut|pointer instead|"
        r"cannot replace|can not replace|does not replace|stand in for",
    ),
}

PROGRESS_EXCLUSIONS = {
    "source qualifications": (r"qualification|source scope|\bscope\b",),
    "approval history": (r"history|approvals? record|decided decisions?",),
    "source inventories": (r"inventor|source list|next.excerpt|excerpt counter",),
}

SOURCE_MAP_ALLOWED = {
    "scope": r"scope|qualification",
    "attribution": r"attribution",
    "normalisation": r"normalis|normaliz|transcription",
    "correction": r"correction",
}

MATERIAL_EXCLUSIONS = (r"scope|qualification", r"source maps?")

INBOUND = r"incoming|inbound|cites|referencing|another file"
ANCHOR_AFTER_EDIT = r"resolv|verif|check|update|redirect|repair|rename"

QUALIFICATION_CHECKS = {
    "before": r"\bbefore\b",
    "after": r"\bafter\b",
    "qualification": r"qualification|qualifier",
    "scope": r"\bscope\b",
    "order": r"\border\b",
    "quantifier first": r"\bfirst\b",
    "quantifier much": r"\bmuch\b",
    "quantifier all": r"\ball\b",
}

SECOND_ORDER_DOC = (
    r"second-order|second order|breadcrumb|describe what another file holds|"
    r"documen(?:t|ts|ing) (?:other|another) file"
)
LINK_SUBSTITUTION = r"replace[sd]? (?:its|the) content with a link|in place of its content"
PROTECTED = r"content and evidence|drafts?\b|material|source maps?"
APPROVAL = r"approval|approved|ask"


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


def contract_fields(text, label):
    """Return every prose line declaring `**label:**`; a fenced shape is not a contract."""
    pattern = rf"^\*\*{label}:\*\*\s*(.+)$"
    return [match.group(1).strip() for match in re.finditer(pattern, prose(text), re.M)]


def declared_items(payload):
    """Split one contract field into its distinct declared items."""
    parts = re.split(r"[;,]|\band\b", payload)
    return [part.strip(" .:*") for part in parts if part.strip(" .:*")]


def missing_groups(text, groups):
    """Return the label groups that `text` does not state at all."""
    return [group for group in groups if not re.search(group, text, re.I)]


def has_any(text, pattern):
    """Report whether one alternative appears, in any wording."""
    return bool(re.search(pattern, text, re.I))


def names_any(text, alternatives):
    """Report whether the text names at least one of the alternatives."""
    return any(re.search(alternative, text, re.I) for alternative in alternatives)


def section(text, heading, level=2):
    """Return the body of one plain heading, up to the next heading of the same or higher level."""
    lines = prose(text).splitlines()
    start = next((i + 1 for i, line in enumerate(lines)
                  if line.strip() == "#" * level + f" {heading}"), None)
    if start is None:
        return ""
    body = []
    for line in lines[start:]:
        marker = re.match(r"^(#{1,6})\s", line)
        if marker and len(marker[1]) <= level:
            break
        body.append(line)
    return "\n".join(body)


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
    def test_new_project_paths_and_plan_links(self):
        entry = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        tree = re.search(r"```text\n(.*?)\n```", entry, re.S)[1]
        self.assertIn("  organisation/\n    thesis-and-vision.md\n    requirements.md\n    plan.md", tree)
        self.assertIn("  sources/\n  source-maps/\n    <author-title>.md", tree)
        for filename in ("thesis-and-vision.md", "requirements.md", "plan.md"):
            owner = f"`organisation/{filename}`"
            self.assertIn(owner, (REFERENCES / "article" / filename).read_text(encoding="utf-8"))
            self.assertIn(owner, (REFERENCES / "rules/user-prompts.md").read_text(encoding="utf-8"))
        source_map = (REFERENCES / "supplement/source-maps.md").read_text(encoding="utf-8")
        self.assertIn("`source-maps/<author-title>.md`", source_map)
        self.assertNotIn("sources/source-maps/", source_map)
        plan = (REFERENCES / "article/plan.md").read_text(encoding="utf-8")
        example = re.search(r"```markdown\n(.*?)\n```", plan, re.S)[1]
        with TemporaryDirectory(prefix="draft-writing-project-") as temporary:
            project = Path(temporary)
            (project / "organisation").mkdir()
            for section in (1, 2):
                folder = project / "sections" / f"section-{section}"
                folder.mkdir(parents=True)
                for role in ("arc", "progress"):
                    (folder / f"{role}-section-{section}.md").write_text("# Section\n", encoding="utf-8")
            path = project / "organisation/plan.md"
            path.write_text(example, encoding="utf-8")
            self.assertEqual(link_errors(path), [])

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


class OwnershipChecks(unittest.TestCase):
    """Closed per-owner contracts and the central admission gate they answer to."""

    def setUp(self):
        self.modules = {name: (REFERENCES / name).read_text(encoding="utf-8")
                        for name in OWNER_MODULES}

    def field(self, name, label):
        fields = contract_fields(self.modules[name], label)
        self.assertEqual(len(fields), 1, f"{name} needs exactly one **{label}:** contract line")
        return fields[0]

    def test_owner_modules_declare_closed_contracts(self):
        for name, (allowed_groups, deferred_to) in OWNER_MODULES.items():
            with self.subTest(module=name):
                allowed = self.field(name, "Allowed")
                excluded = self.field(name, "Excluded")
                self.assertEqual(missing_groups(allowed, allowed_groups), [])
                self.assertTrue(names_any(excluded, deferred_to),
                                f"{name} must name the owner that holds its excluded content")
                self.assertGreaterEqual(len(declared_items(allowed)), 3)
                self.assertGreaterEqual(len(declared_items(excluded)), 3)

    def test_progress_excludes_qualifications_history_and_inventories(self):
        excluded = self.field("section/progress.md", "Excluded")
        for label, group in PROGRESS_EXCLUSIONS.items():
            with self.subTest(exclusion=label):
                self.assertEqual(missing_groups(excluded, group), [])

    def test_source_maps_allow_source_specific_qualifications(self):
        allowed = self.field("supplement/source-maps.md", "Allowed")
        for label, pattern in SOURCE_MAP_ALLOWED.items():
            with self.subTest(field=label):
                self.assertTrue(has_any(allowed, pattern), f"source maps omit {label}")

    def test_material_constraint_is_not_a_source_scope(self):
        allowed = self.field("section/material.md", "Allowed")
        excluded = self.field("section/material.md", "Excluded")
        self.assertTrue(has_any(allowed, r"constraint|condition"))
        self.assertEqual(missing_groups(excluded, MATERIAL_EXCLUSIONS), [])
        fields = re.findall(r"^\*\*Constraint:\*\*\s*(.+)$", self.modules["section/material.md"], re.M)
        self.assertEqual(len(fields), 1, "one passage Constraint field, in the file shape")
        self.assertTrue(fields[0].strip())

    def test_entry_binds_ownership_and_creates_no_implicit_owner(self):
        body = section((ROOT / "SKILL.md").read_text(encoding="utf-8"), "Binding ownership")
        self.assertTrue(body, "SKILL.md needs a ## Binding ownership section")
        for label, groups in ENTRY_GATE.items():
            with self.subTest(gate=label):
                self.assertEqual(missing_groups(body, groups), [])


class RefactorChecks(unittest.TestCase):
    """Contract checks for the sibling refactor skill, skipped when it is not installed."""

    @classmethod
    def setUpClass(cls):
        path = ROOT.parents[0] / "agent-md-refactor" / "SKILL.md"
        if not path.is_file():
            raise unittest.SkipTest("Standalone skill has no sibling refactor skill")
        cls.text = path.read_text(encoding="utf-8")
        cls.lines = prose(cls.text).splitlines()

    def test_incoming_anchors_are_checked_after_a_rename(self):
        anchors = [line for line in self.lines if re.search(r"\banchors?\b", line, re.I)]
        self.assertGreaterEqual(len(anchors), 2, "one anchor line is not a verification procedure")
        self.assertTrue([line for line in anchors if re.search(INBOUND, line, re.I)],
                        "no anchor line states that another file may cite the heading")
        self.assertTrue([line for line in anchors if re.search(ANCHOR_AFTER_EDIT, line, re.I)],
                        "no anchor line requires resolving or repairing the result")

    def test_qualifications_survive_before_and_after(self):
        body = section(self.text, "Verification")
        self.assertTrue(body, "the refactor skill needs a Verification section")
        for label, pattern in QUALIFICATION_CHECKS.items():
            with self.subTest(check=label):
                self.assertTrue(has_any(body, pattern), f"Verification omits {label}")

    def test_no_second_order_document(self):
        self.assertTrue(has_any(prose(self.text), SECOND_ORDER_DOC),
                        "a file may not hold documentation about other files")

    def test_link_substitution_is_forbidden(self):
        self.assertTrue(has_any(prose(self.text), LINK_SUBSTITUTION),
                        "a link may not stand in for the information")

    def test_protected_content_is_not_edited_without_approval(self):
        self.assertTrue([line for line in self.lines
                         if re.search(PROTECTED, line, re.I) and re.search(APPROVAL, line, re.I)],
                        "content and evidence files state no approval boundary for edits")


if __name__ == "__main__":
    unittest.main(verbosity=2)
