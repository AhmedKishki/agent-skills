"""Capture source text and provenance in an application workspace."""
from pathlib import Path
from uuid import uuid4
from urllib.parse import urlsplit

from .common import read_json, safe_child, sha256, utc_now, write_json, write_text
from .network import fetch_text


def add_source(app: Path, url: str, title: str, kind: str,
               text_file: Path | None = None, published_at: str | None = None) -> dict:
    if kind not in {"primary", "secondary"}:
        raise ValueError("Source kind must be primary or secondary")
    if not isinstance(url, str) or not url.strip() or not title.strip():
        raise ValueError("Source URL and title are required")
    parsed = urlsplit(url)
    if parsed.scheme != "https" or not parsed.hostname or parsed.username or parsed.password:
        raise ValueError("Source URL must be credential-free HTTPS")
    text = text_file.read_text(encoding="utf-8") if text_file else fetch_text(url)
    if not text.strip():
        raise ValueError("Source text is empty")
    research_path = safe_child(app, "research.json")
    research = read_json(research_path)
    source_id = "s-" + uuid4().hex
    relative = f"sources/{source_id}.txt"
    destination = safe_child(app, relative)
    destination.parent.mkdir(parents=True, exist_ok=True)
    write_text(destination, text)
    source = {"id": source_id, "url": url, "title": title, "kind": kind,
              "published_at": published_at, "retrieved_at": utc_now(),
              "file": relative, "sha256": sha256(destination)}
    research["sources"].append(source)
    write_json(research_path, research)
    return source
