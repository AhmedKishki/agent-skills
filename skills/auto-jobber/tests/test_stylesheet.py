import tempfile
import unittest
from pathlib import Path

import support  # noqa: F401
from ja.html_safety import standalone
from ja.stylesheet import normalize_stylesheet


class StylesheetTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        root = Path(self.temp.name)
        (root / "cv").mkdir()
        (root / "template").mkdir()
        self.html = root / "cv/cv.html"
        self.css = root / "template/cv.css"
        self.css.write_text("body { color: black; }")

    def source(self, attributes):
        return f"<html><head><link {attributes}></head><body>Candidate</body></html>"

    def test_selected_relative_stylesheet_is_portable(self):
        source = self.source('rel="stylesheet" href="../template/cv.css"')
        normalized = normalize_stylesheet(source, self.html, self.css)
        self.assertIn('href="cv.css"', normalized)
        self.assertNotIn("../template", standalone(normalized, self.css.read_text()))

    def test_legacy_alias_is_unchanged(self):
        source = self.source('rel="stylesheet" href="cv.css"')
        self.assertEqual(normalize_stylesheet(source, self.html, self.css), source)

    def test_wrong_selected_file_is_rejected(self):
        other = self.css.with_name("other.css")
        other.write_text("body { color: red; }")
        with self.assertRaises(ValueError):
            normalize_stylesheet(self.source('rel="stylesheet" href="../template/other.css"'),
                                 self.html, self.css)

    def test_remote_and_encoded_stylesheets_are_rejected(self):
        for target in ("https://example.org/cv.css", "//example.org/cv.css", "file:///cv.css",
                       "data:text/css,body{}", "%2e%2e/template/cv.css", "../template/cv.css?x=1"):
            with self.subTest(target=target), self.assertRaises(ValueError):
                normalize_stylesheet(self.source(f'rel="stylesheet" href="{target}"'),
                                     self.html, self.css)

    def test_duplicate_and_active_attributes_are_not_hidden(self):
        duplicate = self.source('rel="stylesheet" href="../template/cv.css" href="cv.css"')
        with self.assertRaises(ValueError):
            normalize_stylesheet(duplicate, self.html, self.css)
        active = self.source('rel="stylesheet" href="../template/cv.css" onload="alert(1)"')
        normalized = normalize_stylesheet(active, self.html, self.css)
        with self.assertRaises(ValueError):
            standalone(normalized, self.css.read_text())


if __name__ == "__main__":
    unittest.main()
