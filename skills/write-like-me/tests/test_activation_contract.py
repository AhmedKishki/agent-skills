import json
import unittest
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parents[1]
SCENARIOS = SKILL_ROOT / "evaluations" / "activation-scenarios.json"


class ActivationContractTests(unittest.TestCase):
    def test_activation_cases_are_balanced_and_unique(self):
        payload = json.loads(SCENARIOS.read_text(encoding="utf-8"))
        positive = payload["should_trigger"]
        negative = payload["should_not_trigger"]
        self.assertGreaterEqual(len(positive), 5)
        self.assertGreaterEqual(len(negative), 4)
        ids = [item["id"] for item in [*positive, *negative]]
        self.assertEqual(len(ids), len(set(ids)))
        for item in [*positive, *negative]:
            self.assertTrue(item["prompt"].strip())

    def test_description_covers_core_trigger_language_without_becoming_generic(self):
        skill_text = (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8")
        frontmatter = skill_text.split("---", 2)[1].lower()
        for phrase in ("write, rewrite, or reply", "user's voice", "emails", "social posts", "generic ai texture", "evidence-based writing pattern"):
            self.assertIn(phrase, frontmatter)
        self.assertNotIn("summarize", frontmatter)
        self.assertNotIn("translate", frontmatter)
        self.assertNotIn("debug", frontmatter)

    def test_implicit_personal_prose_and_third_party_boundary(self):
        payload = json.loads(SCENARIOS.read_text(encoding="utf-8"))
        positive_ids = {item["id"] for item in payload["should_trigger"]}
        negative_ids = {item["id"] for item in payload["should_not_trigger"]}
        self.assertTrue({"personal-email-implicit", "social-post-implicit", "personal-reply-implicit"}.issubset(positive_ids))
        self.assertIn("third-party-impersonation", negative_ids)


if __name__ == "__main__":
    unittest.main()
