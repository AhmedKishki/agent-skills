import tempfile
import unittest
from pathlib import Path

from support import fixture
from ja.build import build_application
from ja.common import write_text
from ja.manifest import archive, verify_manifest


class ArchiveSafetyTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        _, app = fixture(self.temp.name)
        self.build = Path(build_application(app, html_only=True)["build"])

    def test_nested_manifest_is_not_invisible(self):
        write_text(self.build / "input" / "manifest.json", "unexpected private notes")
        with self.assertRaisesRegex(ValueError, "file set changed"):
            verify_manifest(self.build)

    def test_directory_symlink_is_rejected_before_archive(self):
        secret = Path(self.temp.name) / "private"
        secret.mkdir()
        write_text(secret / "private.txt", "Must not be copied")
        (self.build / "extra").symlink_to(secret, target_is_directory=True)
        with self.assertRaisesRegex(ValueError, "Symlinks"):
            archive(self.build)
        self.assertFalse((self.build.parent.parent / "archive").exists())

    def test_file_symlink_is_rejected(self):
        (self.build / "linked").symlink_to(self.build / "cv.html")
        with self.assertRaisesRegex(ValueError, "Symlinks"):
            verify_manifest(self.build)


if __name__ == "__main__":
    unittest.main()
