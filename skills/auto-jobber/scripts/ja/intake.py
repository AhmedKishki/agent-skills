"""Import a list, old-CV extraction and user additions without inventing missing data."""
from pathlib import Path

from .bootstrap import bootstrap
from .common import read_json, require, write_json, write_text
from .intake_data import entry_text, extra_section, upstream_data
from .profile_checks import CATEGORIES, validate_details
from .languages import localize_labels


def intake(workspace, data_file):
    workspace = Path(workspace).expanduser().resolve()
    data = read_json(Path(data_file).expanduser())
    require(isinstance(data.get("person", {}).get("name"), str), "Intake needs person.name")
    require(isinstance(data.get("qualifications"), dict), "Intake needs qualifications")
    require(not (workspace / "intake-source.json").exists(), "Original intake already exists")
    validate_details(data)
    language = data.get("document_language", "en")
    require(language in {"en", "de"}, "Intake document_language must be en or de")
    temporary = workspace / ".intake-upstream.json"
    require(not temporary.exists(), "Unexpected intake staging file; inspect it first")
    write_json(temporary, upstream_data(data))
    try:
        bootstrap(workspace, temporary)
    finally:
        temporary.unlink(missing_ok=True)
    write_json(workspace / "intake-source.json", data)
    profile = read_json(workspace / "qualifications.json")
    profile["person"] = data["person"]
    profile["qualifications"] = {key: data["qualifications"].get(key, []) for key in CATEGORIES}
    profile["interests"] = data.get("interests", [])
    profile["voice"].update(data.get("voice", {}))
    for category, items in profile["qualifications"].items():
        for index, item in enumerate(items):
            prefix = category.replace("_", "-")
            profile["evidence"].append({"id": f'ev-{prefix}-{item["id"]}',
                "text": entry_text(item), "verified": False,
                "source": f"intake-source.json#/qualifications/{category}/{index}"})
    for index, interest in enumerate(profile["interests"]):
        require(isinstance(interest, str), "Interests must be user-supplied text")
        profile["evidence"].append({"id": f"ev-interest-{index + 1}", "text": interest,
            "verified": False, "source": f"intake-source.json#/interests/{index}"})
    html = (workspace / "cv.html").read_text(encoding="utf-8")
    for title, category in (("Certificates", "certificates"), ("Languages", "languages"),
                            ("Online presence", "online_presence")):
        section = extra_section(title, category, profile["qualifications"][category])
        html = html.replace("</main>", section + "\n</main>")
    html = localize_labels(html, language)
    write_text(workspace / "cv.html", html)
    write_json(workspace / "qualifications.json", profile)
    return {"status": "needs-source-audit-freshness-confirmation-and-CV-review",
            "qualification_count": sum(map(len, profile["qualifications"].values())),
            "evidence_count": len(profile["evidence"])}
