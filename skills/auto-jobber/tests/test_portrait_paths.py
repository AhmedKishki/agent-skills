"""Local authorization remains separate from rendered data-image permission."""
import tempfile
import unittest
from pathlib import Path

from support import fixture
from test_portraits import png
from ja.arguments import parser
from ja.html_safety import standalone
from ja.languages import choose_variant
from ja.profile import check_baseline, seal


class PortraitPathTests(unittest.TestCase):
    def test_explicit_root_with_sibling_source(self):
        with tempfile.TemporaryDirectory() as root:
            root = Path(root)
            (root / "cv").mkdir()
            (root / "profile").mkdir()
            photo = root / "profile" / "photo.png"
            photo.write_bytes(png())
            source = '<head></head><img src="../profile/photo.png" alt="Synthetic">'
            rendered = standalone(source, "", root / "cv" / "cv.html", root)
            self.assertIn("data:image/png;base64,", rendered)
            with self.assertRaises(ValueError):
                standalone(source, "", root / "cv" / "cv.html", root / "cv")
            with self.assertRaises(ValueError):
                standalone(source, "", root / "cv" / "cv.html")
            (root / "linked").symlink_to(root / "profile", target_is_directory=True)
            with self.assertRaises(ValueError):
                standalone(source.replace("profile", "linked"), "", root / "cv" / "cv.html", root)
            with self.assertRaises(ValueError):
                standalone(rendered, "", root / "cv" / "cv.html", root)

    def test_snapshot_missing_and_directory_symlink(self):
        with tempfile.TemporaryDirectory() as root:
            workspace, _ = fixture(root)
            photo = workspace / "photo.png"
            photo.write_bytes(png())
            cv = workspace / "cv.html"
            cv.write_text(cv.read_text().replace("</header>", '<img src="photo.png"></header>'))
            record = seal(workspace, asset_root=workspace)
            revision = workspace / record["revision"]
            name = next(iter(record["assets"]))
            (revision / name).unlink()
            with self.assertRaises(ValueError):
                check_baseline(revision)
            (revision / "portrait-assets").rmdir()
            (workspace / "external").mkdir()
            (workspace / "external" / Path(name).name).write_bytes(png())
            (revision / "portrait-assets").symlink_to(workspace / "external", target_is_directory=True)
            with self.assertRaises(ValueError):
                choose_variant(workspace, "en")

    def test_cli_and_legacy_csp(self):
        for command in ("preview", "seal"):
            args = parser().parse_args([command, "--asset-root", "/tmp/example"])
            self.assertEqual(args.asset_root, Path("/tmp/example"))
        self.assertIn("img-src 'none'", standalone("<head></head><p>Text</p>", ""))


if __name__ == "__main__":
    unittest.main()
