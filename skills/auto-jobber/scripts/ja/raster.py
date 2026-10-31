"""Bound structure before the optional Pillow decoder processes portrait pixels."""
import struct
import zlib

from .common import require
from .portrait_decode import decode_portrait, dimensions_ok

MAX_BYTES = 5 * 1024 * 1024


def raster_type(data):
    require(0 < len(data) <= MAX_BYTES, "Portrait exceeds 5 MiB or is empty")
    if data.startswith(b"\x89PNG\r\n\x1a\n"):
        pos, dimensions, ended, pixels = 8, None, False, False
        while pos + 12 <= len(data):
            size = int.from_bytes(data[pos:pos + 4], "big")
            kind, body = data[pos + 4:pos + 8], data[pos + 8:pos + 8 + size]
            require(pos + size + 12 <= len(data), "Truncated PNG")
            crc = int.from_bytes(data[pos + size + 8:pos + size + 12], "big")
            require(zlib.crc32(kind + body) == crc, "Invalid PNG checksum")
            if dimensions is None:
                require(kind == b"IHDR" and size == 13, "Invalid PNG header")
                dimensions = struct.unpack(">II", body[:8])
            else:
                require(kind != b"IHDR", "Duplicate PNG IHDR is forbidden")
            dimensions_ok(dimensions)
            require(kind not in {b"acTL", b"fcTL", b"fdAT"}, "Animated PNG is forbidden")
            pixels = pixels or kind == b"IDAT" and size > 0
            pos += size + 12
            if kind == b"IEND":
                ended = size == 0 and pos == len(data)
                break
        require(ended and dimensions and pixels, "Invalid PNG ending or missing pixels")
        mime = "png"
    else:
        require(data.startswith(b"\xff\xd8") and data.endswith(b"\xff\xd9"),
                "Only JPEG and PNG portraits are supported")
        pos, dimensions, scan = 2, None, False
        while pos + 4 <= len(data):
            require(data[pos] == 255, "Invalid JPEG marker")
            while pos < len(data) and data[pos] == 255:
                pos += 1
            require(pos < len(data), "Truncated JPEG marker")
            marker = data[pos]
            pos += 1
            size = int.from_bytes(data[pos:pos + 2], "big")
            require(size >= 2 and pos + size <= len(data), "Invalid JPEG segment")
            if marker in {0xC0, 0xC1, 0xC2}:
                require(size >= 8, "Invalid JPEG frame")
                height, width = struct.unpack(">HH", data[pos + 3:pos + 7])
                dimensions = width, height
                dimensions_ok(dimensions)
            if marker == 0xDA:
                scan = True
                break
            pos += size
        require(dimensions is not None and scan, "JPEG needs a supported frame and scan")
        mime = "jpeg"
    dimensions_ok(dimensions)
    decode_portrait(data, mime, dimensions)
    return mime
