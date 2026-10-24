"""Validate captured evidence; source truth still requires human/agent review."""
from datetime import date, datetime, timezone
from pathlib import Path
from urllib.parse import urlsplit

from .common import read_json, safe_child, sha256


def _require(condition, message):
    if not condition:
        raise ValueError(message)


def _date(value, label, timestamp=False):
    _require(isinstance(value, str) and bool(value), f"Missing {label}")
    try:
        if timestamp:
            parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
            _require(parsed.tzinfo is not None, f"{label} needs a timezone")
            _require(parsed <= datetime.now(timezone.utc), f"Future {label}")
            return parsed.date()
        parsed = date.fromisoformat(value)
        _require(parsed.isoformat() == value, f"Invalid ISO date: {label}")
        _require(parsed <= datetime.now(timezone.utc).date(), f"Future {label}")
        return parsed
    except (TypeError, ValueError) as error:
        raise ValueError(f"Invalid {label}: {value}") from error


def validate_research(app: Path, policy: dict) -> list[str]:
    data = read_json(safe_child(app, "research.json"))
    _require(isinstance(data, dict), "Research must be an object")
    status = data.get("status")
    _require(status in {"complete", "limited", "unavailable"}, "Research is pending/invalid")
    _require(data.get("project_search") in {"found", "not_found", "unavailable"},
             "Invalid project_search")
    log = data.get("search_log")
    _require(isinstance(log, list) and all(isinstance(x, str) and x.strip() for x in log),
             "Invalid search log")
    _require(status == "complete" or bool(log), "Fallback requires a search log")
    sources, facts = data.get("sources"), data.get("facts")
    _require(isinstance(sources, list) and isinstance(facts, list), "Invalid evidence lists")
    _require(status != "complete" or bool(sources and facts), "Complete needs sources/facts")
    maximum = policy.get("research_max_age_days", 180)
    _require(type(maximum) is int and maximum >= 0, "Invalid research_max_age_days")
    indexed, texts, ids = {}, {}, set()
    for source in sources:
        _require(isinstance(source, dict), "Invalid source")
        sid = source.get("id")
        _require(isinstance(sid, str) and sid.strip() and sid not in ids, "Duplicate/invalid ID")
        ids.add(sid)
        _require(source.get("kind") in {"primary", "secondary"}, "Invalid source kind")
        for key in ("url", "title", "file", "sha256"):
            _require(isinstance(source.get(key), str) and source[key].strip(), f"Missing {key}")
        parsed_url = urlsplit(source["url"])
        _require(parsed_url.scheme == "https" and parsed_url.hostname and not parsed_url.username,
                 "Sources need credential-free HTTPS URLs")
        _require(source["file"] == f"sources/{sid}.txt", "Source file must match its source ID")
        _date(source.get("retrieved_at"), "retrieved_at", timestamp=True)
        if source.get("published_at") is not None:
            _date(source["published_at"], "published_at")
        path = safe_child(app, source["file"])
        try:
            _require(sha256(path) == source["sha256"], f"Source hash mismatch: {sid}")
            texts[sid] = " ".join(path.read_text(encoding="utf-8").split())
        except (OSError, UnicodeError) as error:
            raise ValueError(f"Cannot read source: {sid}") from error
        indexed[sid] = source
    for fact in facts:
        _require(isinstance(fact, dict), "Invalid fact")
        fid, sid = fact.get("id"), fact.get("source_id")
        _require(isinstance(fid, str) and fid.strip() and fid not in ids, "Duplicate/invalid ID")
        ids.add(fid)
        _require(isinstance(sid, str) and sid in indexed, "Unknown source ID")
        _require(isinstance(fact.get("statement"), str) and fact["statement"].strip(),
                 "Missing statement")
        quote = fact.get("quote")
        _require(isinstance(quote, str) and quote.strip(), "Missing quote")
        _require(" ".join(quote.split()) in texts[sid], "Quote not contained in source")
        _require(fact.get("kind") in {"company", "project"}, "Invalid fact kind")
        _require(fact.get("project_status") in
                 {"active", "announced", "completed", "historical", "unknown"}, "Invalid status")
        _require(type(fact.get("ongoing")) is bool, "ongoing must be boolean")
        as_of = fact.get("status_as_of")
        dated = _date(as_of, "status_as_of") if as_of is not None else None
        if fact["ongoing"]:
            _require(indexed[sid]["kind"] == "primary" and fact["kind"] == "project"
                     and fact["project_status"] == "active" and dated is not None,
                     "Ongoing needs primary, active project evidence and status date")
            age = (datetime.now(timezone.utc).date() - dated).days
            _require(age <= maximum, "Ongoing project evidence is stale")
    return [] if status == "complete" else [f"Company research is {status}; inspect search log"]
