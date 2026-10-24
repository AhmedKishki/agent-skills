"""Retain user-authored prose, never treat voice samples as qualification evidence."""
from pathlib import Path
from uuid import uuid4

from .common import read_json, require, safe_child, sha256, utc_now, write_json, write_text
from .wording_translation import effective_text


def _text(path, source):
    require(isinstance(source, str) and source.strip(), "User wording needs a source")
    text = Path(path).read_text(encoding="utf-8")
    require(bool(text.strip()), "User wording cannot be empty")
    return text


def _normalize(text):
    return " ".join(text.split())


def capture_wording(app: Path, text_file: Path, source: str,
                    must_include: list[str] | None = None, language: str | None = None) -> dict:
    text = _text(text_file, source)
    includes = [] if must_include is None else must_include
    require(isinstance(includes, list) and all(isinstance(x, str) and x.strip()
            for x in includes), "must_include must contain nonempty strings")
    app = Path(app)
    folder = safe_child(app, "wording")
    folder.mkdir(mode=0o700, exist_ok=True)
    relative = f"wording/w-{uuid4()}.txt"
    path = safe_child(app, relative)
    require(not path.exists(), "Wording snapshot already exists")
    write_text(path, text)
    record = {"file": relative, "application": str(app.resolve()), "sha256": sha256(path), "source": source,
              "authorship": "user", "captured_at": utc_now(), "must_include": includes}
    plan = read_json(app / "plan.json")
    record["language"] = language or plan.get("job", {}).get("language", "en")
    plan["user_input"] = record
    write_json(app / "plan.json", plan)
    return record


def validate_wording(app, plan, profile) -> list[str]:
    errors = []
    try:
        record = plan.get("user_input")
        require(isinstance(record, dict), "Capture this job's user wording first")
        require(record.get("application") == str(Path(app).resolve()), "Wording belongs to another job")
        require(record.get("authorship") == "user", "Wording must be user-authored")
        require(isinstance(record.get("source"), str) and record["source"].strip()
                and isinstance(record.get("captured_at"), str), "Missing wording provenance")
        relative = record.get("file", "")
        require(isinstance(relative, str) and relative.startswith("wording/w-")
                and relative.endswith(".txt"), "Invalid wording snapshot path")
        path = safe_child(app, relative)
        require(path.is_file() and sha256(path) == record.get("sha256"),
                "Missing or changed current-job wording snapshot")
        text = _normalize(effective_text(app, record, plan.get("job", {}).get("language", "en")))
        require(bool(text), "Empty wording snapshot")
        quotes = plan.get("letter", {}).get("wording_quotes")
        require(isinstance(quotes, list) and bool(quotes), "Add user wording quotes")
        require(all(isinstance(q, str) and len(q.split()) >= 3
                    and sum(c.isalpha() for c in q) >= 3
                    and _normalize(q) in text for q in quotes),
                "Quotes must be meaningful exact excerpts of current user input")
        sentences = [s["text"] for p in plan["letter"].get("paragraphs", [])
                     for s in p["sentences"]]
        require(any(_normalize(q) in _normalize(sentence) for q in quotes for sentence in sentences),
                "Preserve at least one user quote verbatim in the letter")
        includes = record.get("must_include")
        require(isinstance(includes, list) and all(isinstance(x, str) and x.strip()
                for x in includes), "Invalid must_include wording")
        require(all(x in " ".join(sentences) for x in includes), "Missing must_include wording")
        voice = profile.get("voice", {})
        require(isinstance(voice, dict), "voice must be an object")
        for key in ("tone_preferences", "character_notes", "writing_preferences", "avoid"):
            require(isinstance(voice.get(key, []), list) and all(isinstance(x, str)
                    for x in voice.get(key, [])), f"voice.{key} must be a string list")
        require(isinstance(voice.get("samples", []), list), "voice.samples must be a list")
        for sample in voice.get("samples", []):
            require(isinstance(sample, dict) and sample.get("authorship") == "user"
                    and all(isinstance(sample.get(k), str) and sample[k].strip()
                            for k in ("id", "text", "source", "recorded_at")),
                    "Voice samples need raw user text and provenance, not evidence")
    except (ValueError, OSError, KeyError, TypeError) as exc:
        errors.append(str(exc))
    return errors


def remember_voice(workspace, text_file, source) -> dict:
    text = _text(text_file, source)
    path = Path(workspace) / "qualifications.json"
    profile = read_json(path)
    sample = {"id": str(uuid4()), "text": text, "source": source,
              "authorship": "user", "recorded_at": utc_now()}
    profile.setdefault("voice", {}).setdefault("samples", []).append(sample)
    write_json(path, profile)
    return sample
