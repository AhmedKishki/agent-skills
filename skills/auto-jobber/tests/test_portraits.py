"""Synthetic raster assets exercise native snapshots without applicant material."""
import shutil
import struct
import subprocess
import tempfile
import unittest
import zlib
from pathlib import Path
from unittest.mock import patch

from support import fixture
from ja.applications import new_application, check_snapshot
from ja.baseline_preview import preview_baseline
from ja.build import build_application
from ja.common import read_json, write_json
from ja.voice import capture_wording
from ja.html_safety import standalone
from ja.languages import choose_variant
from ja.manifest import archive, verify_manifest
from ja.profile import seal
from ja.render import browser_path, render_documents


def png(width=1):
    def chunk(kind, body):
        return struct.pack(">I", len(body)) + kind + body + struct.pack(">I", zlib.crc32(kind + body))
    return (b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", struct.pack(">IIBBBBB", width, 1, 8, 2, 0, 0, 0))
            + chunk(b"IDAT", zlib.compress(b"\0\xff\0\0")) + chunk(b"IEND", b""))


class PortraitTests(unittest.TestCase):
    def test_native_flow(self):
        with tempfile.TemporaryDirectory() as root:
            workspace, old = fixture(root)
            cv = workspace / "cv.html"
            photo = workspace / "photo.png"
            photo.write_bytes(png())
            cv.write_text(cv.read_text().replace("</header>", '<img src="photo.png" alt="Synthetic"></header>'))
            with patch("ja.baseline_preview.render_documents", return_value={"passed": True}):
                preview = preview_baseline(workspace, asset_root=workspace)
            self.assertIn("data:image/png;base64,", (Path(preview["preview"]) / "cv.html").read_text())
            if browser_path() and all(shutil.which(t) for t in ("pdfinfo", "pdftotext", "pdfimages")):
                folder = Path(preview["preview"])
                render_documents(folder, read_json(workspace / "qualifications.json")["policy"], stems=("cv",))
                images = subprocess.run(["pdfimages", "-list", str(folder / "cv.pdf")],
                                        check=True, capture_output=True, text=True).stdout
                self.assertIn("image", images.splitlines()[-1])
            record = seal(workspace, asset_root=workspace)
            photo.write_bytes(png(2))
            with self.assertRaises(ValueError):
                choose_variant(workspace, "en")
            photo.write_bytes(png())
            app = Path(new_application(workspace, job_file=Path(root) / "vacancy.txt")["application"])
            for name in ("plan.json", "research.json"):
                shutil.copyfile(old / name, app / name)
            shutil.copytree(old / "wording", app / "wording")
            capture_wording(app, Path(root) / "user-words.txt", "Synthetic current-job reply")
            photo.unlink()
            with self.assertRaises(ValueError):
                choose_variant(workspace, "en")
            build = Path(build_application(app, html_only=True)["build"])
            self.assertIn("img-src data:", (build / "cv.html").read_text())
            verify_manifest(build)
            archive(build)
            asset = next(iter(record["assets"]))
            (app / "input" / asset).write_bytes(png(2))
            with self.assertRaises(ValueError):
                check_snapshot(app)
            (build / "input" / asset).unlink()
            with self.assertRaises(ValueError):
                verify_manifest(build)

    def test_forbidden_inputs(self):
        with tempfile.TemporaryDirectory() as root:
            root = Path(root)
            photo = root / "photo.png"
            photo.write_bytes(png())
            (root / "link.png").symlink_to(photo)
            for src in ("https://example.invalid/x.png", "data:image/png;base64,AA==",
                        "file:photo.png", "/photo.png", "../escape.png", "link.png", "x.svg"):
                with self.subTest(src=src), self.assertRaises((ValueError, FileNotFoundError)):
                    standalone(f'<html><head></head><img src="{src}"></html>', "", root / "cv.html", root)
            for attrs in ('srcset="photo.png 2x"', 'onload="alert(1)"'):
                with self.assertRaises(ValueError):
                    standalone(f'<head></head><img src="photo.png" {attrs}>', "", root / "cv.html", root)
            for data in (png(9000), b"x" * (5 * 1024 * 1024 + 1), b"<svg/>"):
                photo.write_bytes(data)
                with self.assertRaises(ValueError):
                    standalone('<head></head><img src="photo.png">', "", root / "cv.html", root)


if __name__ == "__main__":
    unittest.main()
