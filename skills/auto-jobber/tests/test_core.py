import tempfile
import unittest
from pathlib import Path

from support import AFTER, BEFORE, fixture
from ja.blocks import apply_edits, read_blocks
from ja.build import build_application
from ja.common import read_json, sha256, write_json, write_text
from ja.manifest import archive, verify_manifest
from ja.validate import check_application


class CoreTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.workspace, self.app = fixture(self.temp.name)

    def change_plan(self, update):
        plan = read_json(self.app / "plan.json")
        update(plan)
        write_json(self.app / "plan.json", plan)

    def test_bounded_edits_and_original_preservation(self):
        original, css = sha256(self.workspace / "cv.html"), sha256(self.workspace / "cv.css")
        data = check_application(self.app)
        self.assertIn(AFTER, data["tailored"])
        self.assertNotIn(BEFORE, data["tailored"])
        self.assertIn("2021–2025", data["tailored"])
        self.assertEqual(original, sha256(self.workspace / "cv.html"))
        self.assertEqual(css, sha256(self.workspace / "cv.css"))

    def test_stale_and_unknown_blocks_fail(self):
        source = "<p><!-- cv:x -->Original<!-- /cv:x --></p>"
        with self.assertRaisesRegex(ValueError, "Stale"):
            apply_edits(source, [{"block_id": "x", "before": "Old", "after": "New"}])
        with self.assertRaisesRegex(ValueError, "Unknown"):
            apply_edits(source, [{"block_id": "y", "before": "Original", "after": "New"}])
        with self.assertRaises(ValueError):
            read_blocks("<!-- cv:x -->nested <!-- cv:y -->text<!-- /cv:y --><!-- /cv:x -->")

    def test_numeric_and_employer_evidence_cannot_back_cv_claim(self):
        self.change_plan(lambda p: p["edits"][0].update(after="I have 5 years of FreeRTOS experience."))
        with self.assertRaisesRegex(ValueError, "numeric"):
            check_application(self.app)
        self.change_plan(lambda p: p["edits"][0].update(evidence_ids=["company-fact"]))
        with self.assertRaisesRegex(ValueError, "unknown evidence"):
            check_application(self.app)

    def test_budget_and_changed_snapshot_fail(self):
        self.change_plan(lambda p: p["edits"][0].update(after="Extensive rewritten prose " * 100))
        with self.assertRaisesRegex(ValueError, "budget"):
            check_application(self.app)
        write_text(self.app / "posting.txt", "Changed source")
        with self.assertRaisesRegex(ValueError, "posting changed"):
            check_application(self.app)

    def test_revisions_archive_and_tamper_detection(self):
        first = Path(build_application(self.app, html_only=True)["build"])
        second = Path(build_application(self.app, html_only=True)["build"])
        self.assertNotEqual(first, second)
        self.assertFalse(verify_manifest(first)["submitted"])
        target = Path(archive(first)["archive"])
        self.assertTrue((target / "cv.html").exists())
        with self.assertRaises(ValueError):
            archive(first)
        write_text(first / "cv.html", "tampered")
        with self.assertRaisesRegex(ValueError, "Build changed"):
            verify_manifest(first)


if __name__ == "__main__":
    unittest.main()
