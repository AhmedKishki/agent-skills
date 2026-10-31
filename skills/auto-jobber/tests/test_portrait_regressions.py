"""Malformed pixels and comment lookalikes must not bypass portrait validation."""
import struct
import tempfile
import unittest
import zlib
from pathlib import Path
from unittest.mock import patch

from support import fixture
from test_portraits import png
from ja.applications import new_application
from ja.html_safety import standalone
from ja.profile import seal
from ja.raster import raster_type
from ja.portrait_decode import decode_portrait


class PortraitRegressionTests(unittest.TestCase):
    def test_marker_only_jpeg_is_not_a_decodable_portrait(self):
        fake = bytes.fromhex("ffd8ffc0000b080010000c01011100ffda0002ffd9")
        with self.assertRaisesRegex(ValueError, "decod"):
            raster_type(fake)

    def test_duplicate_png_header(self):
        body = struct.pack(">IIBBBBB", 100000, 1, 8, 2, 0, 0, 0)
        duplicate = struct.pack(">I", len(body)) + b"IHDR" + body
        duplicate += struct.pack(">I", zlib.crc32(b"IHDR" + body))
        data = png()
        with self.assertRaisesRegex(ValueError, "Duplicate PNG IHDR"):
            raster_type(data[:33] + duplicate + data[33:])

    def test_decoder_bomb_and_dimension_mismatch_are_rejected(self):
        from PIL import Image
        with patch("PIL.Image.open", side_effect=Image.DecompressionBombError("synthetic bomb")):
            with self.assertRaisesRegex(ValueError, "decoding failed"):
                decode_portrait(png(), "png", (1, 1))
        with self.assertRaisesRegex(ValueError, "dimensions differ"):
            decode_portrait(png(), "png", (2, 1))

    def test_corrupt_png_pixels_with_valid_crc(self):
        data = png()
        kind, body = b"IDAT", b"invalid zlib pixels"
        corrupt = struct.pack(">I", len(body)) + kind + body
        corrupt += struct.pack(">I", zlib.crc32(kind + body))
        with self.assertRaisesRegex(ValueError, "decoding failed"):
            raster_type(data[:33] + corrupt + data[-12:])

    def test_commented_duplicate_is_untouched_in_standalone_and_snapshot(self):
        with tempfile.TemporaryDirectory() as root:
            workspace, _ = fixture(root)
            (workspace / "photo.png").write_bytes(png())
            cv = workspace / "cv.html"
            image = '<img src="photo.png" alt="Synthetic">'
            comment = "<!-- " + image + " -->"
            source = cv.read_text().replace("</header>", comment + "\n" + image + image + "</header>")
            cv.write_text(source)
            rendered = standalone(source, "", cv, workspace)
            self.assertIn(comment, rendered)
            self.assertEqual(rendered.count("data:image/png;base64,"), 2)
            record = seal(workspace, asset_root=workspace)
            app = Path(new_application(workspace, job_file=Path(root) / "vacancy.txt")["application"])
            frozen = (app / "input" / "cv.html").read_text()
            self.assertIn(comment, frozen)
            asset = next(iter(record["assets"]))
            self.assertEqual(frozen.count(f'src="{asset}"'), 2)
            (workspace / "photo.png").unlink()
            output = standalone(frozen, "", app / "input" / "cv.html", app / "input")
            self.assertEqual(output.count("data:image/png;base64,"), 2)

    def test_missing_pillow_does_not_affect_image_free_html(self):
        import builtins
        original = builtins.__import__

        def without_pillow(name, *args, **kwargs):
            if name == "PIL" or name.startswith("PIL."):
                raise ImportError("Synthetic missing Pillow")
            return original(name, *args, **kwargs)

        with patch("builtins.__import__", side_effect=without_pillow):
            self.assertIn("img-src 'none'", standalone("<head></head><p>Text</p>", ""))
            with self.assertRaisesRegex(ValueError, "requires optional Pillow"):
                raster_type(png())


if __name__ == "__main__":
    unittest.main()
