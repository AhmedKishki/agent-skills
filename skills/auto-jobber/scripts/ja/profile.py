"""Create and retain every approved editable CV/profile baseline revision."""
import shutil
import uuid
from pathlib import Path

from .common import ASSETS, read_json, require, sha256, utc_now, write_json, write_text
from .html_safety import standalone
from .profile_checks import validate_profile

BASE_FILES = ("qualifications.json", "cv.html", "cv.css")
SOURCE_FILES = ("candidate-source.json", "intake-source.json")


def initialise(workspace):
    workspace = Path(workspace).expanduser().resolve()
    workspace.mkdir(mode=0o700, parents=True, exist_ok=False)
    (workspace / "applications").mkdir(mode=0o700)
    for name in BASE_FILES:
        write_text(workspace / name, (ASSETS / name).read_text(encoding="utf-8"))
    write_text(workspace / ".gitignore", "*\n")
    return {"workspace": str(workspace), "status": "needs-profile-intake-and-baseline-review"}


def seal(workspace, language=None, html_file=None, css_file=None):
    from .freshness import require_current
    from .languages import markup_language, register_variant
    workspace = Path(workspace).expanduser().resolve()
    profile = read_json(workspace / "qualifications.json")
    html_file, css_file = Path(html_file or workspace / "cv.html"), Path(css_file or workspace / "cv.css")
    html = html_file.read_text(encoding="utf-8")
    detected = markup_language(html)
    require(language is None or language == detected, "Requested CV language differs from HTML lang")
    language = detected
    validate_profile(profile, html)
    require_current(profile)
    standalone(html, css_file.read_text(encoding="utf-8"))
    names = list(BASE_FILES) + [name for name in SOURCE_FILES if (workspace / name).exists()]
    identity = utc_now().replace(":", "").replace("+", "-") + "-" + uuid.uuid4().hex[:8]
    revision = workspace / "baselines" / identity
    revision.mkdir(mode=0o700, parents=True)
    for name in names:
        require(not (workspace / name).is_symlink(), f"Baseline symlink is forbidden: {name}")
        origin = html_file if name == "cv.html" else css_file if name == "cv.css" else workspace / name
        require(not origin.is_symlink(), "Baseline sources must not be symlinks")
        shutil.copyfile(origin, revision / name)
    record = {"sealed_at": utc_now(), "revision": str(revision.relative_to(workspace)),
              "language": language,
              "files": {name: sha256(revision / name) for name in names}}
    write_json(revision / "baseline.json", record)
    register_variant(workspace, revision, language)
    if html_file.resolve() == (workspace / "cv.html").resolve():
        write_json(workspace / "baseline.json", record)
    return record


def check_baseline(workspace):
    record = read_json(workspace / "baseline.json")
    names = set(record["files"])
    require(set(BASE_FILES) <= names <= set(BASE_FILES) | set(SOURCE_FILES),
            "Invalid baseline manifest")
    for name, digest in record["files"].items():
        require(not (workspace / name).is_symlink(), f"Baseline symlink is forbidden: {name}")
        require(sha256(workspace / name) == digest, f"Baseline changed: {name}; review and reseal")
    return record
