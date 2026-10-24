"""Show the editable CV draft before approval; never fabricate a companion letter."""
import uuid
from pathlib import Path

from .common import read_json, require, utc_now, write_json, write_text
from .html_safety import standalone
from .render import render_documents
from .languages import markup_language


def preview_baseline(workspace, language=None, html_file=None, css_file=None):
    workspace = Path(workspace).expanduser().resolve()
    profile = read_json(workspace / "qualifications.json")
    require(profile["person"].get("name", "").strip(), "Provide candidate details before previewing")
    identity = utc_now().replace(":", "").replace("+", "-") + "-" + uuid.uuid4().hex[:8]
    folder = workspace / "previews" / identity
    folder.mkdir(mode=0o700, parents=True)
    css = (css_file or workspace / "cv.css").read_text(encoding="utf-8")
    source = (html_file or workspace / "cv.html").read_text(encoding="utf-8")
    require(language is None or markup_language(source) == language, "Preview language differs from HTML lang")
    write_text(folder / "cv.html", standalone(source, css))
    write_text(folder / "cv-source.html", source)
    write_text(folder / "cv.css", css)
    write_json(folder / "qualifications.json", profile)
    report = render_documents(folder, profile["policy"], stems=("cv",))
    write_json(folder / "report.json", report)
    return {"preview": str(folder), "status": "baseline-draft-for-user-review", "render": report}
