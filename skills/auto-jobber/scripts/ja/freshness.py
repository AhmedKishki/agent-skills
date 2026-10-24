"""Calendar-month qualification review; confirmation is gated by the caller."""
from datetime import datetime
from pathlib import Path

from .common import read_json, require, write_json


def _date(value):
    if not isinstance(value, str) or not value.strip():
        return None
    try:
        text = value.strip()
        if len(text) == 4:
            text += "-01-01"
        elif len(text) == 7:
            text += "-01"
        return datetime.fromisoformat(text.replace("Z", "+00:00")).astimezone()
    except ValueError:
        return None


def _entry_dates(value):
    if isinstance(value, dict):
        for key, child in value.items():
            if key in {"updated_at", "date", "end", "start"}:
                parsed = _date(child)
                if parsed:
                    yield parsed
            elif isinstance(child, (dict, list)):
                yield from _entry_dates(child)
    elif isinstance(value, list):
        for child in value:
            yield from _entry_dates(child)


def freshness_status(profile: dict, now: datetime | None = None) -> dict:
    current = (now or datetime.now().astimezone()).astimezone()
    dates = [date for date in _entry_dates(profile.get("qualifications", {}))
             if date <= current]
    latest = max(dates) if dates else None
    raw_review = profile.get("last_reviewed_at")
    reviewed = _date(raw_review)
    if raw_review is not None:
        require(reviewed is not None, "Invalid last_reviewed_at timestamp")
        require(reviewed <= current, "last_reviewed_at cannot be in the future")
    reference = reviewed or latest
    month = current.strftime("%Y-%m")
    stale = reference is None or reference.strftime("%Y-%m") != month
    return {"current_datetime": current.isoformat(), "current_month": month,
            "latest_entry_month": latest.strftime("%Y-%m") if latest else None,
            "last_reviewed_at": raw_review, "needs_confirmation": stale,
            "reason": ("No dated qualifications or review" if reference is None else
                       "Review required for current calendar month" if stale else
                       "Qualifications reviewed or dated in current calendar month")}


def require_current(profile, now=None):
    status = freshness_status(profile, now)
    require(not status["needs_confirmation"],
            f'{status["current_datetime"]}: confirm qualifications are current '
            "(including confirming no changes) before continuing")
    return status


def confirm_current(workspace: Path, note: str) -> dict:
    require(isinstance(note, str) and note.strip(), "Provide a confirmation note")
    path = Path(workspace) / "qualifications.json"
    profile = read_json(path)
    timestamp = datetime.now().astimezone().isoformat()
    profile["last_reviewed_at"] = timestamp
    profile["current_confirmation"] = {"note": note.strip(), "timestamp": timestamp}
    write_json(path, profile)
    return freshness_status(profile)
