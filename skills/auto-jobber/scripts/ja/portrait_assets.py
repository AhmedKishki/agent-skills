"""Authorize local raster inputs and freeze their bytes under content-addressed names."""
import base64
import hashlib
import os
import re
import stat
from html import escape
from html.parser import HTMLParser
from pathlib import Path

from .common import require
from .raster import MAX_BYTES, raster_type


def regular_path(path):
    path = Path(path).absolute()
    require(not any(p.is_symlink() for p in (path, *path.parents)),
            f"Symlink components are forbidden: {path}")
    require(path.is_file(), f"Missing regular asset: {path}")
    return path.resolve()


def asset_name(name):
    return bool(re.fullmatch(r"portrait-assets/[0-9a-f]{64}\.(png|jpeg)", name))


def read_raster(path):
    """Open every component without following links, including during concurrent replacement."""
    parts = Path(path).absolute().parts
    descriptor = os.open(parts[0], os.O_RDONLY | os.O_DIRECTORY)
    try:
        for component in parts[1:-1]:
            child = os.open(component, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=descriptor)
            os.close(descriptor)
            descriptor = child
        child = os.open(parts[-1], os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK, dir_fd=descriptor)
        with os.fdopen(child, "rb") as stream:
            require(stat.S_ISREG(os.fstat(stream.fileno()).st_mode), "Portrait must be a regular file")
            data = stream.read(MAX_BYTES + 1)
        require(len(data) <= MAX_BYTES, "Portrait exceeds 5 MiB")
        return data
    finally:
        os.close(descriptor)


def prepare_assets(source, html_file=None, asset_root=None, snapshot=None):
    parser = HTMLParser(convert_charrefs=True)
    replacements, records = [], {}
    line_offsets = [0]
    for match in re.finditer("\n", source):
        line_offsets.append(match.end())

    def image(tag, attrs):
        if tag != "img":
            return
        require(html_file is not None and asset_root is not None,
                "Local portraits require an explicit --asset-root")
        require(len(dict(attrs)) == len(attrs), "Duplicate image attributes are forbidden")
        attrs = dict(attrs)
        require(set(attrs) <= {"class", "src", "alt", "width", "height", "style", "title"},
                "Unsupported image attribute (srcset/events are forbidden)")
        src = attrs.get("src", "")
        require(src and not re.search(r"[:\\?#%\x00-\x20]", src) and not Path(src).is_absolute(),
                "Portrait src must be a plain relative local path")
        root = Path(asset_root).absolute()
        require(not any(p.is_symlink() for p in (root, *root.parents)), "Asset root is a symlink")
        origin = regular_path(Path(html_file).absolute().parent / src)
        require(origin.is_relative_to(root.resolve()), "Portrait escapes asset root")
        require(origin.suffix.lower() in {".png", ".jpg", ".jpeg"}, "Unsupported portrait format")
        require(origin.stat().st_size <= MAX_BYTES, "Portrait exceeds 5 MiB")
        data = read_raster(origin)
        mime = raster_type(data)
        digest = hashlib.sha256(data).hexdigest()
        name = f"portrait-assets/{digest}.{mime}"
        require(name not in records or records[name]["origin"] == str(origin),
                "Identical portraits must reference the same source file")
        records[name] = {"origin": str(origin), "sha256": digest}
        if snapshot is not None:
            target = Path(snapshot) / name
            target.parent.mkdir(mode=0o700, exist_ok=True)
            target.write_bytes(data)
            attrs["src"] = name
        else:
            attrs["src"] = f"data:image/{mime};base64," + base64.b64encode(data).decode("ascii")
        markup = "<img " + " ".join(f'{k}="{escape(v or "", quote=True)}"' for k, v in attrs.items()) + ">"
        line, column = parser.getpos()
        start = line_offsets[line - 1] + column
        replacements.append((start, start + len(parser.get_starttag_text()), markup))

    parser.handle_starttag = image
    parser.handle_startendtag = image
    parser.feed(source)
    for start, end, replacement in reversed(replacements):
        source = source[:start] + replacement + source[end:]
    return source, records
