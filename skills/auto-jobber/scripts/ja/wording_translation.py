"""Keep original wording and explicitly approved translations as separate sources."""
from uuid import uuid4

from .common import read_json, require, safe_child, sha256, utc_now, write_json, write_text


def effective_text(app, record, target_language):
    language = record.get("language", target_language)
    require(language in {"en", "de"} and target_language in {"en", "de"},
            "User wording and offer languages must be en or de")
    if language == target_language:
        return safe_child(app, record["file"]).read_text(encoding="utf-8")
    translation = record.get("translation", {})
    require(translation.get("language") == target_language and translation.get("approval_source"),
            "Ask the user to approve a translation of their wording into the offer language")
    relative = translation.get("file", "")
    require(isinstance(relative, str) and relative.startswith("wording/translation-")
            and relative.endswith(".txt"), "Invalid approved translation path")
    path = safe_child(app, relative)
    require(path.is_file() and sha256(path) == translation.get("sha256"), "Approved translation changed")
    return path.read_text(encoding="utf-8")


def approve_translation(app, text_file, source, language):
    plan = read_json(app / "plan.json")
    require(language == plan["job"]["language"], "Translation must match the offer language")
    record = plan.get("user_input")
    require(isinstance(record, dict) and record.get("authorship") == "user", "Capture original user wording first")
    require(source.strip(), "Record the actual user's translation approval")
    text = text_file.read_text(encoding="utf-8")
    require(text.strip(), "Translation cannot be empty")
    relative = f"wording/translation-{uuid4().hex}.txt"
    path = safe_child(app, relative)
    write_text(path, text)
    translation = {"file": relative, "sha256": sha256(path), "language": language,
                   "approval_source": source, "approved_at": utc_now(),
                   "authorship": "user-approved-translation"}
    record["translation"] = translation
    write_json(app / "plan.json", plan)
    return translation
