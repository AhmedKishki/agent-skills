import importlib.util
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "update_writing_pattern.py"
SPEC = importlib.util.spec_from_file_location("update_writing_pattern", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MODULE)


class UpdateWritingPatternTests(unittest.TestCase):
    def test_records_confirmed_rule_without_storing_drafts(self):
        profile = "# My Writing Pattern\n\nUse the current draft as truth.\n"
        original = "We are pleased to announce the launch."
        edited = "We launched it today."
        updated, metadata = MODULE.update_profile(
            profile,
            rule="Prefer a direct announcement over ceremonial framing",
            context="product update",
            original=original,
            edited=edited,
        )
        self.assertIn("## Confirmed corrections", updated)
        self.assertIn("Prefer a direct announcement", updated)
        self.assertNotIn(original, updated)
        self.assertNotIn(edited, updated)
        self.assertIn(metadata["original_sha256"][:16], updated)
        self.assertIn(metadata["edited_sha256"][:16], updated)
        self.assertFalse(metadata["draft_text_stored_in_profile"])

    def test_duplicate_rule_is_updated_not_duplicated(self):
        profile = "# My Writing Pattern\n"
        arguments = {
            "rule": "Keep the opening direct",
            "context": "email",
            "original": "I wanted to write and let you know.",
            "edited": "Here is the update.",
        }
        first, _ = MODULE.update_profile(profile, **arguments)
        second, _ = MODULE.update_profile(first, **arguments)
        self.assertEqual(second.count("Keep the opening direct"), 1)

    def test_identical_text_has_no_learnable_correction(self):
        with self.assertRaisesRegex(ValueError, "identical"):
            MODULE.update_profile(
                "# Profile",
                rule="Use shorter openings",
                context="email",
                original="Same.",
                edited="Same.",
            )


if __name__ == "__main__":
    unittest.main()
