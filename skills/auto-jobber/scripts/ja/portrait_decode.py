"""Decode portraits only when requested; image-free workflows need no Pillow."""
import io
import warnings

from .common import require


def dimensions_ok(size):
    width, height = size
    require(0 < width <= 8192 and 0 < height <= 8192 and width * height <= 20000000,
            "Portrait dimensions exceed limits (8192 per side, 20 megapixels)")


def decode_portrait(data, mime, expected):
    try:
        from PIL import Image, ImageFile
    except ImportError as error:
        raise ValueError("Portrait validation requires optional Pillow; install Pillow in the "
                         "CLI Python environment or omit the portrait. Image-free CVs need no Pillow.") from error
    try:
        require(not ImageFile.LOAD_TRUNCATED_IMAGES,
                "Portrait validation requires Pillow's strict truncated-image checking")
        with warnings.catch_warnings():
            warnings.simplefilter("error", Image.DecompressionBombWarning)
            with Image.open(io.BytesIO(data)) as image:
                require(image.format == {"jpeg": "JPEG", "png": "PNG"}[mime],
                        "Decoded portrait format differs from its header")
                dimensions_ok(image.size)
                require(image.size == expected, "Decoded portrait dimensions differ from header")
                require(not getattr(image, "is_animated", False) and getattr(image, "n_frames", 1) == 1,
                        "Animated portraits are forbidden")
                image.verify()
            with Image.open(io.BytesIO(data)) as image:
                dimensions_ok(image.size)
                image.load()
                dimensions_ok(image.size)
                require(image.size == expected, "Decoded portrait dimensions changed")
    except Exception as error:
        raise ValueError(f"Portrait raster decoding failed: {error}") from error
