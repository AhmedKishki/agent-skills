import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from support import fixture
from ja.common import safe_child
from ja.html_safety import standalone, visible_text
from ja.network import fetch_text


class SecurityTests(unittest.TestCase):
    def test_active_markup_and_remote_css_are_rejected(self):
        bad = ['<script>alert(1)</script>', '<img src="https://example.com/pixel">',
               '<iframe src="file:///etc/passwd"></iframe>', '<p onclick="x()">x</p>',
               '<meta http-equiv="refresh" content="0;url=https://example.com">']
        for fragment in bad:
            with self.subTest(fragment=fragment), self.assertRaises(ValueError):
                standalone(f"<html><head></head><body>{fragment}</body></html>", "")
        for css in ['@import "https://example.com";', 'p{background:url(https://example.com)}',
                    r'p{background:u\72l(https://example.com)}', 'p{overflow:hidden}',
                    '/* </style><meta http-equiv="refresh" content="0;url=https://example.com"><style> */']:
            with self.subTest(css=css), self.assertRaises(ValueError):
                standalone("<html><head></head><body>Safe</body></html>", css)

    def test_contact_links_and_visible_text(self):
        source = '<html><head><title>Hidden</title></head><body><a href="mailto:a@b.com">Alex</a></body></html>'
        result = standalone(source, "@page{size:A4}")
        self.assertIn("Content-Security-Policy", result)
        self.assertEqual("Alex", visible_text(result))

    def test_local_private_urls_and_credentials_are_rejected(self):
        for url in ["file:///etc/passwd", "http://example.com", "https://user:pass@example.com",
                    "https://127.0.0.1", "https://[::1]", "https://169.254.169.254"]:
            with self.subTest(url=url), self.assertRaises((ValueError, OSError)):
                fetch_text(url)
        with patch("socket.getaddrinfo", return_value=[(2, 1, 6, "", ("10.0.0.1", 443))]):
            with self.assertRaises(ValueError):
                fetch_text("https://private.example")

    def test_path_escape_and_symlink(self):
        with tempfile.TemporaryDirectory() as root:
            inside = Path(root) / "inside"
            inside.mkdir()
            (inside / "escape").symlink_to(Path(root), target_is_directory=True)
            for name in ["../outside", "/etc/passwd", "escape/file"]:
                with self.subTest(name=name), self.assertRaises(ValueError):
                    safe_child(inside, name)


if __name__ == "__main__":
    unittest.main()
