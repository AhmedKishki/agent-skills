import tempfile
import unittest
from pathlib import Path

from support import fixture
from ja.applications import new_application
from ja.common import read_json, write_json, write_text
from ja.documents import cover_letter
from ja.languages import choose_variant, localize_labels
from ja.profile import seal
from ja.validate import check_application


class LanguageTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.workspace, self.app = fixture(self.temp.name)

    def test_missing_german_variant_cannot_silently_use_english(self):
        with self.assertRaisesRegex(ValueError, "de CV variant"):
            choose_variant(self.workspace, "de")

    def test_bilingual_approved_source_and_plan_language_lock(self):
        source = (self.workspace / "cv.html").read_text()
        german = self.workspace / "cv.de.html"
        write_text(german, localize_labels(source, "de"))
        record = seal(self.workspace, "de", german)
        self.assertEqual("de", record["language"])
        self.assertTrue((self.workspace / record["revision"] / "cv.html").exists())
        app = Path(new_application(self.workspace, job_file=self.app / "posting.txt", language="de")["application"])
        self.assertEqual("de", read_json(app / "plan.json")["job"]["language"])
        self.assertIn("Berufserfahrung", (app / "input" / "cv.html").read_text())
        plan = read_json(self.app / "plan.json")
        plan["job"]["language"] = "de"
        write_json(self.app / "plan.json", plan)
        with self.assertRaisesRegex(ValueError, "Plan language differs"):
            check_application(self.app)

    def test_german_cover_letter_fixed_text_and_date(self):
        plan = read_json(self.app / "plan.json")
        plan["job"].update(language="de", role="Softwareentwickler")
        plan["letter"].update(greeting="Sehr geehrtes Team,", closing="Mit freundlichen Grüßen")
        html = cover_letter(plan, {"name": "Alex Example"}, "@page{size:A4}")
        self.assertIn('<html lang="de">', html)
        self.assertIn("Bewerbung als Softwareentwickler", html)
        self.assertNotIn("Application for", html)


if __name__ == "__main__":
    unittest.main()
