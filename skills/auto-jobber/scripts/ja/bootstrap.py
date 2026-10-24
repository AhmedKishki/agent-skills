"""Import user-supplied awesome-cv-html JSON before candidate review and sealing.

No demo data is fetched.
"""
import re
from html import escape
from pathlib import Path

from .bootstrap_sections import FIELDS, render_section, validate
from .common import ASSETS, read_json, require, write_json, write_text


def bootstrap(workspace: Path, data_file: Path) -> dict:
    workspace = Path(workspace).expanduser().resolve()
    require(not (workspace / "baseline.json").exists(), "Baseline is already sealed")
    profile = read_json(workspace / "qualifications.json")
    require(profile.get("evidence") == [], "Candidate evidence already exists")
    require(profile.get("editable_blocks") == {}, "Candidate editable blocks already exist")
    require(isinstance(profile.get("person"), dict) and not any(profile["person"].values()),
            "Candidate person records already exist")
    require(not (workspace / "candidate-source.json").exists(), "Candidate source already exists")
    template = (ASSETS / "cv.html").read_text(encoding="utf-8")
    require((workspace / "cv.html").read_text(encoding="utf-8") == template,
            "Existing CV differs from the empty template; refusing to replace it")
    for name in ("candidate-source.json", "qualifications.json", "cv.html"):
        require(not (workspace / name).is_symlink(), f"Refusing symlink: {name}")
    data = read_json(Path(data_file).expanduser())
    validate(data)
    about = data["about-me"]
    evidence, blocks = [], {}

    def record(block_id, kind, text, locator, context=""):
        evidence_id = "ev-" + block_id
        evidence.append({"id": evidence_id, "text": f"{context}: {text}" if context else text,
                         "source": "candidate-source.json#" + locator, "verified": False})
        if kind == "fact":
            return ""
        blocks[block_id] = {"kind": kind, "evidence_ids": [evidence_id]}
        return f"<!-- cv:{block_id} -->{escape(text)}<!-- /cv:{block_id} -->"

    name = " ".join(about.get(key, "") for key in ("first-name", "last-name")).strip()
    header = ('<header class="about-me">'
              f'<h1 class="about-me__name">{escape(name)}</h1>'
              f'<p class="about-me__position">{escape(about.get("position", ""))}</p>'
              f'<p class="about-me__address">{escape(about.get("location", ""))}</p>')
    contacts = [about.get(key, "") for key in ("email", "mobile-display", "github", "website")]
    header += '<p class="about-me__social">' + " · ".join(escape(s) for s in contacts if s) + "</p></header>"
    html = re.sub(r'<header class="about-me">.*?</header>', lambda _: header, template, flags=re.S)
    summary = about.get("description", "")
    marked = record("summary", "summary", summary, "/about-me/description") if summary.strip() else ""
    html = html.replace("<p></p>", f"<p>{marked}</p>", 1)
    if not marked:
        html = re.sub(r'<section class="summary">.*?</section>', "", html, flags=re.S)
    for section in FIELDS:
        rendered = render_section(section, data.get(section, []), record)
        pattern = rf'<section class="{section}">.*?</section>'
        if re.search(pattern, html, flags=re.S):
            html = re.sub(pattern, lambda _: rendered, html, flags=re.S)
        else:
            html = html.replace("</main>", rendered + "\n</main>")
    profile["person"] = {"name": name, "email": about.get("email", ""),
                         "phone": about.get("mobile-display", ""), "location": about.get("location", "")}
    profile["evidence"], profile["editable_blocks"] = evidence, blocks
    write_json(workspace / "candidate-source.json", data)
    write_text(workspace / "cv.html", html)
    write_json(workspace / "qualifications.json", profile)
    return {"status": "pending-candidate-review", "evidence_count": len(evidence),
            "editable_block_count": len(blocks)}
