import tempfile
import unittest
from datetime import date, timedelta
from pathlib import Path

from support import fixture
from ja.common import read_json, write_json, write_text
from ja.research import validate_research
from ja.sources import add_source


class ResearchTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        _, self.app = fixture(self.temp.name)
        self.text = Path(self.temp.name) / "project.txt"
        write_text(self.text, "Northstar Example is actively developing the Aurora device pilot.")
        source = add_source(self.app, "https://northstar.example/projects", "Project update",
                            "primary", self.text, date.today().isoformat())
        self.research = read_json(self.app / "research.json")
        self.research.update(status="complete", project_search="found")
        self.research["facts"] = [{"id": "f-aurora", "statement": "Aurora is an active pilot.",
            "source_id": source["id"], "quote": self.text.read_text(), "kind": "project",
            "project_status": "active", "status_as_of": date.today().isoformat(), "ongoing": True}]

    def validate(self):
        write_json(self.app / "research.json", self.research)
        return validate_research(self.app, {"research_max_age_days": 180})

    def test_primary_dated_exact_quote_passes(self):
        self.assertEqual([], self.validate())

    def test_fabricated_quote_and_modified_source_fail(self):
        self.research["facts"][0]["quote"] = "An invented project statement."
        with self.assertRaisesRegex(ValueError, "Quote"):
            self.validate()
        self.research["facts"][0]["quote"] = self.text.read_text()
        source = self.app / self.research["sources"][0]["file"]
        write_text(source, "tampered")
        with self.assertRaisesRegex(ValueError, "hash"):
            self.validate()

    def test_old_completed_announced_secondary_are_not_ongoing(self):
        fact = self.research["facts"][0]
        for status in ("completed", "announced", "historical", "unknown"):
            fact["project_status"] = status
            with self.subTest(status=status), self.assertRaises(ValueError):
                self.validate()
        fact["project_status"] = "active"
        fact["status_as_of"] = (date.today() - timedelta(days=181)).isoformat()
        with self.assertRaisesRegex(ValueError, "stale"):
            self.validate()
        fact["status_as_of"] = date.today().isoformat()
        self.research["sources"][0]["kind"] = "secondary"
        with self.assertRaises(ValueError):
            self.validate()

    def test_source_cannot_point_at_another_application_file(self):
        self.research["sources"][0]["file"] = "posting.txt"
        with self.assertRaisesRegex(ValueError, "Source file"):
            self.validate()


if __name__ == "__main__":
    unittest.main()
