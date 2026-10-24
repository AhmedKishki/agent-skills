import tempfile
import unittest
from pathlib import Path

from support import fixture
from ja.blocks import read_blocks
from ja.bootstrap import bootstrap
from ja.common import read_json, sha256, write_json
from ja.profile import check_baseline, initialise, seal
from ja.freshness import confirm_current


class BootstrapTests(unittest.TestCase):
    def test_upstream_json_import_preserves_facts_and_requires_review(self):
        with tempfile.TemporaryDirectory() as root:
            workspace, source = Path(root) / "workspace", Path(root) / "own-data.json"
            initialise(workspace)
            css = sha256(workspace / "cv.css")
            data = {"about-me": {"first-name": "Alex", "last-name": "Example",
                "email": "alex@example.invalid", "description": "Engineer using C & Python."},
                "experience": [{"title": "Engineer", "institution": "Example Co",
                    "date-range": "2021–2025", "list-items": ["Tested C software."]}],
                "education": [{"study": "BSc", "institution": "Example University", "gpa": 3.65}],
                "skills": [{"heading": "Languages", "list-items": ["C", "Python"]}]}
            write_json(source, data)
            result = bootstrap(workspace, source)
            self.assertEqual("pending-candidate-review", result["status"])
            self.assertEqual(data, read_json(workspace / "candidate-source.json"))
            self.assertEqual(css, sha256(workspace / "cv.css"))
            profile = read_json(workspace / "qualifications.json")
            html = (workspace / "cv.html").read_text()
            self.assertEqual(set(read_blocks(html)), set(profile["editable_blocks"]))
            self.assertTrue(any("BSc" in item["text"] for item in profile["evidence"]))
            self.assertIn("3.65", html)
            with self.assertRaisesRegex(ValueError, "verified"):
                seal(workspace)
            for item in profile["evidence"]:
                item["verified"] = True  # Synthetic test review, not a real candidate approval.
            write_json(workspace / "qualifications.json", profile)
            confirm_current(workspace, "Synthetic fixture approval, current-month confirmation.")
            seal(workspace)
            self.assertIn("candidate-source.json", check_baseline(workspace)["files"])
            with self.assertRaisesRegex(ValueError, "sealed"):
                bootstrap(workspace, source)


if __name__ == "__main__":
    unittest.main()
