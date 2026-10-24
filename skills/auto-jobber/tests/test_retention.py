import tempfile
import unittest
from pathlib import Path

from support import fixture
from ja.common import read_json, sha256, write_text
from ja.profile import seal
from ja.baseline_preview import preview_baseline
from ja.render import browser_path
import shutil


class RetentionTests(unittest.TestCase):
    def test_later_CV_edits_preserve_approved_source_and_old_application(self):
        with tempfile.TemporaryDirectory() as root:
            workspace, app = fixture(root)
            first = read_json(workspace / "baseline.json")
            approved = workspace / first["revision"] / "cv.html"
            digest = sha256(approved)
            source = (workspace / "cv.html").read_text()
            write_text(workspace / "cv.html", source.replace("<title>Curriculum vitae</title>",
                                                             "<title>Reviewed curriculum vitae</title>"))
            second = seal(workspace)
            self.assertNotEqual(first["revision"], second["revision"])
            self.assertEqual(digest, sha256(approved))
            self.assertEqual(digest, sha256(app / "input" / "cv.html"))

    @unittest.skipUnless(browser_path() and shutil.which("pdfinfo") and shutil.which("pdftotext"),
                         "Existing Chrome/Poppler required")
    def test_review_preview_produces_CV_only(self):
        with tempfile.TemporaryDirectory() as root:
            workspace, _ = fixture(root)
            preview = Path(preview_baseline(workspace)["preview"])
            self.assertTrue((preview / "cv.pdf").exists())
            self.assertTrue((preview / "cv-source.html").exists())
            self.assertFalse((preview / "cover-letter.pdf").exists())


if __name__ == "__main__":
    unittest.main()
