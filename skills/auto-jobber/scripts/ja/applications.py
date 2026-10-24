"""Create immutable application inputs without changing the master profile."""
import shutil
import uuid
from datetime import datetime, timezone
from pathlib import Path

from .common import ASSETS, read_json, require, sha256, utc_now, write_json, write_text
from .profile import check_baseline
from .freshness import require_current
from .languages import choose_variant


def new_application(workspace, job_file=None, url=None, language="en"):
    workspace = Path(workspace).expanduser().resolve()
    require_current(read_json(workspace / "qualifications.json"))
    baseline_folder, record = choose_variant(workspace, language)
    require(bool(job_file) != bool(url), "Supply exactly one of --job or --url")
    if job_file:
        path = Path(job_file).expanduser()
        require(path.stat().st_size <= 2 * 1024 * 1024, "Posting exceeds 2 MiB")
        text = path.read_text(encoding="utf-8")
    else:
        from .network import fetch_text
        text = fetch_text(url)
    require(text.strip(), "Posting is empty; supply the complete vacancy text")
    identity = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S-") + uuid.uuid4().hex[:8]
    app = workspace / "applications" / identity
    app.mkdir(mode=0o700)
    (app / "input").mkdir(mode=0o700)
    (app / "sources").mkdir(mode=0o700)
    (app / "builds").mkdir(mode=0o700)
    for name in record["files"]:
        shutil.copyfile(baseline_folder / name, app / "input" / name)
    write_json(app / "input" / "baseline.json", record)
    write_text(app / "posting.txt", text)
    metadata = {"id": identity, "created_at": utc_now(), "job_url": url or "", "language": language,
                "posting_sha256": sha256(app / "posting.txt"), "baseline": record}
    write_json(app / "application.json", metadata)
    plan = read_json(ASSETS / "plan.json")
    plan["job"]["url"] = url or ""
    plan["job"]["language"] = language
    plan["letter"]["date"] = datetime.now(timezone.utc).date().isoformat()
    write_json(app / "plan.json", plan)
    write_json(app / "research.json", read_json(ASSETS / "research.json"))
    return {"application": str(app), "status": "needs-research-and-plan"}


def check_snapshot(app):
    app = Path(app).expanduser().resolve()
    record = read_json(app / "application.json")
    actual = check_baseline(app / "input")
    require(actual == record["baseline"], "Application baseline manifest changed")
    require(sha256(app / "posting.txt") == record["posting_sha256"],
            "Original posting changed; create a new application rather than overwriting it")
    return app
