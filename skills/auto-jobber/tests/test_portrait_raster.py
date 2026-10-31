"""Synthetic JPEG fixtures exercise optional portrait-only Pillow validation."""
import io
import tempfile
import unittest
from pathlib import Path

from support import fixture
from ja.html_safety import standalone
from ja.raster import raster_type

try:
    from PIL import Image
except ImportError:
    Image = None


@unittest.skipUnless(Image, "Optional existing Pillow generates synthetic JPEG test bytes")
class JpegTests(unittest.TestCase):
    def test_baseline_and_progressive_jpeg(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            for progressive in (False, True):
                stream = io.BytesIO()
                Image.new("RGB", (12, 16), (120, 60, 30)).save(stream, "JPEG", progressive=progressive)
                data = stream.getvalue()
                self.assertEqual(raster_type(data), "jpeg")
                (root / "photo.jpg").write_bytes(data)
                result = standalone('<head></head><img src="photo.jpg">', "", root / "cv.html", root)
                self.assertIn("data:image/jpeg;base64,", result)
                with self.assertRaises(ValueError):
                    raster_type(data[:-2])


if __name__ == "__main__":
    unittest.main()
