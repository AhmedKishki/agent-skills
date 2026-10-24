"""Stage a new build, preserving original inputs and all prior revisions."""
import difflib
import shutil
import uuid
from pathlib import Path

from .common import read_json, safe_child, utc_now, write_json, write_text
from .documents import cover_letter
from .html_safety import standalone
from .manifest import save_manifest
from .validate import check_application


def build_application(application, html_only=False):
    data = check_application(application)
    app, plan, profile = data["app"], data["plan"], data["profile"]
    identity = utc_now().replace(":", "").replace("+", "-") + "-" + uuid.uuid4().hex[:8]
    stage = app / "builds" / (".building-" + identity)
    stage.mkdir(mode=0o700)
    try:
        (stage / "input").mkdir(mode=0o700)
        # Copy the sealed inputs only, never stray files/symlinks.
        names = read_json(app / "input" / "baseline.json")["files"]
        for name in list(names) + ["baseline.json"]:
            shutil.copyfile(app / "input" / name, stage / "input" / name)
        write_text(stage / "posting.txt", (app / "posting.txt").read_text(encoding="utf-8"))
        write_json(stage / "plan.json", plan)
        write_json(stage / "research.json", data["research"])
        wording = plan["user_input"]["file"]
        destination = safe_child(stage, wording)
        destination.parent.mkdir(mode=0o700, parents=True)
        shutil.copyfile(safe_child(app, wording), destination)
        if plan["user_input"].get("translation"):
            translated = plan["user_input"]["translation"]["file"]
            shutil.copyfile(safe_child(app, translated), safe_child(stage, translated))
        (stage / "sources").mkdir(mode=0o700)
        for source in data["research"]["sources"]:
            origin = safe_child(app, source["file"])
            target = safe_child(stage, source["file"])
            target.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
            shutil.copyfile(origin, target)
        write_text(stage / "cv.css", data["css"])
        write_text(stage / "cv.html", standalone(data["tailored"], data["css"]))
        write_text(stage / "cover-letter.html", cover_letter(plan, profile["person"], data["css"]))
        diff = difflib.unified_diff(data["baseline"].splitlines(True),
                                    data["tailored"].splitlines(True),
                                    fromfile="approved-base.html", tofile="tailored.html")
        write_text(stage / "cv.patch", "".join(diff))
        render_report = {"passed": False, "status": "html-only; PDFs were not generated"}
        if not html_only:
            from .render import render_documents
            render_report = render_documents(stage, profile["policy"])
        report = {"validation": data["checks"], "render": render_report,
                  "review": plan.get("review", {}), "visual_review": "required",
                  "status": "draft-for-review", "submitted": False}
        write_json(stage / "report.json", report)
        save_manifest(stage, {"application_id": app.name, "status": "draft-for-review",
                              "pdf_generated": not html_only, "submitted": False})
        final = stage.with_name(identity)
        stage.rename(final)
        return {"build": str(final), "status": "draft-for-review", "checks": data["checks"]}
    except BaseException:
        write_text(stage / "FAILED.txt", "Build failed. Partial files are not deliverables.\n")
        raise
