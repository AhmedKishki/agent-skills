import tempfile
import unittest
from pathlib import Path

from support import fixture
from ja.common import read_json, write_json
from ja.freshness import confirm_current, freshness_status
from ja.intake import intake
from ja.languages import choose_variant
from ja.profile import initialise, seal


class IntakeTests(unittest.TestCase):
    def test_comprehensive_old_cv_and_extra_details_are_retained(self):
        with tempfile.TemporaryDirectory() as root:
            workspace, source = Path(root) / "workspace", Path(root) / "intake.json"
            initialise(workspace)
            def entry(identity, title, **extra):
                return {"id": identity, "title": title, "source": "Fictional old CV and user additions",
                        "details": [], "updated_at": "2026-09-30", **extra}
            data = {"document_language": "de", "person": {"name": "Alex Example"},
                "summary": "Ich entwickle und teste Software für eingebettete Systeme.",
                "qualifications": {
                    "study": [entry("degree", "Informatik", organisation="Beispieluniversität")],
                    "work": [entry("role", "Softwareentwickler", details=["Testete Software in C."])],
                    "experience": [entry("volunteer", "Technischer Mentor")],
                    "certificates": [entry("cert", "Zertifikat", organisation="Beispielanbieter")],
                    "expertise": [entry("c", "C", details=["Fehlersuche"])],
                    "languages": [entry("de", "Deutsch", level=None)],
                    "projects": [entry("device", "Geräteprojekt")],
                    "online_presence": [entry("github", "GitHub", url="https://github.com/example")]},
                "interests": ["Zuverlässige kleine Systeme"],
                "voice": {"tone_preferences": ["direkt"], "character_notes": ["zurückhaltend"]}}
            write_json(source, data)
            self.assertEqual(8, intake(workspace, source)["qualification_count"])
            profile = read_json(workspace / "qualifications.json")
            self.assertEqual(data["qualifications"], profile["qualifications"])
            self.assertEqual(data, read_json(workspace / "intake-source.json"))
            self.assertIsNone(profile["qualifications"]["languages"][0]["level"])
            html = (workspace / "cv.html").read_text()
            self.assertIn('<html lang="de">', html)
            self.assertIn("Zertifikate", html)
            self.assertNotIn("B2", html)
            for evidence in profile["evidence"]:
                evidence["verified"] = True
            write_json(workspace / "qualifications.json", profile)
            confirm_current(workspace, "Fictional user confirms all additions are current.")
            seal(workspace)
            folder, record = choose_variant(workspace, "de")
            self.assertTrue((folder / "intake-source.json").exists())
            self.assertEqual("de", record["language"])


if __name__ == "__main__":
    unittest.main()
