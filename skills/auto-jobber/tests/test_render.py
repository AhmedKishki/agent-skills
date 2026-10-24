import shutil
import tempfile
import unittest
from pathlib import Path

from support import fixture
from ja.build import build_application
from ja.common import read_json, write_text
from ja.pdf_checks import tokens
from ja.render import browser_path, render_documents
from bilingual_fixture import german_fixture

TOOLS = bool(browser_path() and shutil.which("pdfinfo") and shutil.which("pdftotext"))


class TokenTests(unittest.TestCase):
    def test_unicode_ligatures_normalise(self):
        self.assertEqual(tokens("Efficient ﬂow"), tokens("efficient flow"))


@unittest.skipUnless(TOOLS, "Existing Chrome and Poppler are required; no installation is attempted")
class RenderTests(unittest.TestCase):
    def test_actual_german_documents_and_readable_umlauts(self):
        with tempfile.TemporaryDirectory() as root:
            _, app = german_fixture(root)
            build = Path(build_application(app)["build"])
            cv, letter = (build / "cv.txt").read_text(), (build / "cover-letter.txt").read_text()
            self.assertIn("eingebettete Geräte", cv)
            self.assertIn("Berufserfahrung", cv)
            self.assertIn("Bewerbung als Softwareentwickler", letter)
            self.assertIn("Mit freundlichen Grüßen", letter)
            self.assertNotIn("Application for", letter)
            self.assertNotIn("B2", cv)

    def test_actual_cv_and_letter_pass_and_stale_outputs_fail(self):
        with tempfile.TemporaryDirectory() as root:
            _, app = fixture(root)
            build = Path(build_application(app)["build"])
            report = read_json(build / "report.json")
            self.assertTrue(report["render"]["passed"])
            self.assertTrue((build / "cv.pdf").is_file())
            self.assertTrue((build / "cover-letter.pdf").is_file())
            self.assertIn("Alex Example", (build / "cv.txt").read_text())
            self.assertIn("2021", (build / "cv.txt").read_text())
            for result in report["render"]["documents"].values():
                self.assertLessEqual(result["page_count"], 2)
            with self.assertRaisesRegex(ValueError, "existing"):
                render_documents(build, {"paper": "A4"})

    def test_pdf_overflow_fails_instead_of_trimming(self):
        with tempfile.TemporaryDirectory() as root:
            folder = Path(root)
            html = ('<html><head><style>@page{size:A4} p{break-before:page}</style></head>'
                    '<body><p>First page</p><p>Second page</p></body></html>')
            for name in ("cv", "cover-letter"):
                write_text(folder / f"{name}.html", html)
            with self.assertRaisesRegex(ValueError, "pages"):
                render_documents(folder, {"paper": "A4", "cv_max_pages": 1, "letter_max_pages": 1})


if __name__ == "__main__":
    unittest.main()
