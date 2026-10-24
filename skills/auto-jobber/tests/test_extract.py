import tempfile
import unittest
import zipfile
from pathlib import Path

from support import fixture
from ja.extract_cv import extract_cv


class ExtractionTests(unittest.TestCase):
    def test_text_html_and_docx_are_local_and_no_overwrite(self):
        text = "Alex Example develops and tests embedded software using C and documents the results."
        with tempfile.TemporaryDirectory() as root:
            root = Path(root)
            txt, html, docx = root / "cv.txt", root / "cv.html", root / "cv.docx"
            txt.write_text(text)
            html.write_text(f"<html><body><script>do not execute</script><p>{text}</p></body></html>")
            xml = ('<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
                   f"<w:body><w:p><w:r><w:t>{text}</w:t></w:r></w:p></w:body></w:document>")
            with zipfile.ZipFile(docx, "w") as archive:
                archive.writestr("word/document.xml", xml)
            for source in (txt, html, docx):
                output = root / (source.suffix[1:] + "-extracted.txt")
                self.assertEqual("needs-source-audit", extract_cv(source, output)["status"])
                self.assertIn(text, output.read_text())
                self.assertNotIn("do not execute", output.read_text())
                with self.assertRaisesRegex(ValueError, "already exists"):
                    extract_cv(source, output)

    def test_scanned_empty_or_unsupported_input_is_not_invented(self):
        with tempfile.TemporaryDirectory() as root:
            root = Path(root)
            source = root / "empty.txt"
            source.write_text(" ")
            with self.assertRaisesRegex(ValueError, "Too little"):
                extract_cv(source, root / "result.txt")
            source = root / "legacy.doc"
            source.write_bytes(b"unsupported")
            with self.assertRaisesRegex(ValueError, "unsupported"):
                extract_cv(source, root / "result.txt")


if __name__ == "__main__":
    unittest.main()
