"""Private, atomic file operations shared by the command-line tools."""
import hashlib
import json
import os
import re
import tempfile
from datetime import datetime, timezone
from pathlib import Path

ASSETS = Path(__file__).resolve().parents[2] / "assets"


def utc_now():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def read_json(path):
    with Path(path).open(encoding="utf-8") as stream:
        return json.load(stream)


def write_text(path, text):
    path = Path(path)
    if path.is_symlink():
        raise ValueError(f"Refusing to replace a symlink: {path}")
    with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=path.parent,
                                     delete=False) as stream:
        temporary = Path(stream.name)
        try:
            stream.write(text)
            stream.flush()
            os.fsync(stream.fileno())
        except BaseException:
            temporary.unlink(missing_ok=True)
            raise
    try:
        temporary.replace(path)
    finally:
        temporary.unlink(missing_ok=True)


def write_json(path, value):
    write_text(path, json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def safe_child(root, relative):
    root = Path(root).resolve()
    relative = Path(relative)
    if relative.is_absolute() or ".." in relative.parts:
        raise ValueError(f"Not a relative workspace path: {relative}")
    result = (root / relative).resolve()
    if not result.is_relative_to(root):
        raise ValueError(f"Path escapes workspace: {relative}")
    return result


def require(condition, message):
    if not condition:
        raise ValueError(message)


def indexed(items, label):
    require(isinstance(items, list), f"{label} must be a list")
    result = {}
    for item in items:
        require(isinstance(item, dict), f"{label} entries must be objects")
        key = item.get("id", "")
        require(isinstance(key, str) and re.fullmatch(r"[a-z][a-z0-9-]*", key),
                f"Invalid {label} id: {key!r}")
        require(key not in result, f"Duplicate {label} id: {key}")
        result[key] = item
    return result
