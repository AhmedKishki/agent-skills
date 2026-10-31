import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import support  # noqa: F401
from ja.common import read_json, write_json
from ja.freshness import confirm_current
from ja.profile import initialise, seal, check_baseline
from ja.baseline_preview import preview_baseline


class StylesheetSourceTests(unittest.TestCase):
    def test_sealed_source_keeps_the_selected_template_self_contained(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            workspace = root / "native"
            initialise(workspace)
            (root / "cv").mkdir()
            (root / "template").mkdir()
            html = root / "cv/example.html"
            css = root / "template/cv.css"
            css.write_text("@page { size: A4; } body { color: black; }")
            html.write_text('<html lang="en"><head><link rel="stylesheet" '
                            'href="../template/cv.css"></head><body><h1>Example Candidate</h1>'
                            '<p><!-- cv:profile -->Engineering<!-- /cv:profile --></p></body></html>')
            profile = read_json(workspace / "qualifications.json")
            profile["person"]["name"] = "Example Candidate"
            profile["evidence"] = [{"id": "source", "text": "Engineering", "source": "fixture",
                                    "verified": True}]
            profile["editable_blocks"] = {"profile": {"kind": "summary", "evidence_ids": ["source"]}}
            write_json(workspace / "qualifications.json", profile)
            confirm_current(workspace, "Synthetic fixture confirmation")
            record = seal(workspace, "en", html, css)
            revision = workspace / record["revision"]
            self.assertEqual(check_baseline(revision), record)
            self.assertIn('href="cv.css"', (revision / "cv.html").read_text())
            self.assertEqual((revision / "cv.css").read_text(), css.read_text())

    def test_preview_requires_explicit_selection_for_non_alias_links(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            workspace = root / "native"
            initialise(workspace)
            (root / "cv").mkdir()
            html = root / "cv/example.html"
            html.write_text('<html lang="en"><head><link rel="stylesheet" '
                            'href="../native/cv.css"></head><body>Example Candidate</body></html>')
            profile = read_json(workspace / "qualifications.json")
            profile["person"]["name"] = "Example Candidate"
            write_json(workspace / "qualifications.json", profile)
            with patch("ja.baseline_preview.render_documents", return_value={"passed": True}) as render:
                with self.assertRaises(ValueError):
                    preview_baseline(workspace, html_file=html)
                render.assert_not_called()

    def test_seal_requires_explicit_selection_for_non_alias_links(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            workspace = root / "native"
            initialise(workspace)
            (root / "cv").mkdir()
            html = root / "cv/example.html"
            html.write_text('<html lang="en"><head><link rel="stylesheet" '
                            'href="../native/cv.css"></head><body><h1>Example Candidate</h1>'
                            '<p><!-- cv:profile -->Engineering<!-- /cv:profile --></p></body></html>')
            profile = read_json(workspace / "qualifications.json")
            profile["person"]["name"] = "Example Candidate"
            profile["evidence"] = [{"id": "source", "text": "Engineering", "source": "fixture",
                                    "verified": True}]
            profile["editable_blocks"] = {"profile": {"kind": "summary", "evidence_ids": ["source"]}}
            write_json(workspace / "qualifications.json", profile)
            confirm_current(workspace, "Synthetic fixture confirmation")
            with self.assertRaises(ValueError):
                seal(workspace, "en", html)


if __name__ == "__main__":
    unittest.main()
