"""Create and retain every approved editable CV/profile baseline revision."""
import shutil
import uuid
from pathlib import Path

from .common import ASSETS, read_json, require, sha256, utc_now, write_json, write_text
from .html_safety import standalone
from .profile_checks import validate_profile
from .portrait_assets import prepare_assets, asset_name, regular_path
from .stylesheet import normalize_stylesheet

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


def seal(workspace, language=None, html_file=None, css_file=None, asset_root=None):
    from .freshness import require_current
    from .languages import markup_language, register_variant
    workspace = Path(workspace).expanduser().resolve()
    profile = read_json(workspace / "qualifications.json")
    explicit_css = css_file
    html_file, css_file = Path(html_file or workspace / "cv.html"), Path(css_file or workspace / "cv.css")
    html = html_file.read_text(encoding="utf-8")
    html = normalize_stylesheet(html, html_file, explicit_css)
    detected = markup_language(html)
    require(language is None or language == detected, "Requested CV language differs from HTML lang")
    language = detected
    validate_profile(profile, html)
    require_current(profile)
    standalone(html, css_file.read_text(encoding="utf-8"), html_file, asset_root)
    names = list(BASE_FILES) + [name for name in SOURCE_FILES if (workspace / name).exists()]
    identity = utc_now().replace(":", "").replace("+", "-") + "-" + uuid.uuid4().hex[:8]
    revision = workspace / "baselines" / identity
    revision.mkdir(mode=0o700, parents=True)
    for name in names:
        require(not (workspace / name).is_symlink(), f"Baseline symlink is forbidden: {name}")
        origin = html_file if name == "cv.html" else css_file if name == "cv.css" else workspace / name
        require(not origin.is_symlink(), "Baseline sources must not be symlinks")
        shutil.copyfile(origin, revision / name)
    frozen, assets = prepare_assets(html, html_file, asset_root, revision)
    write_text(revision / "cv.html", frozen)
    names.extend(assets)
    record = {"sealed_at": utc_now(), "revision": str(revision.relative_to(workspace)),
              "language": language,
              "files": {name: sha256(revision / name) for name in names}}
    if assets:
        record["assets"] = assets
    write_json(revision / "baseline.json", record)
    register_variant(workspace, revision, language)
    if not assets and html_file.resolve() == (workspace / "cv.html").resolve():
        write_json(workspace / "baseline.json", record)
    return record


def check_baseline(workspace):
    record = read_json(workspace / "baseline.json")
    names = set(record["files"])
    assets = record.get("assets", {})
    require(all(asset_name(name) for name in assets), "Invalid portrait manifest")
    require(all(item.get("sha256") == record["files"].get(name)
                and name.split("/")[1].split(".")[0] == item.get("sha256")
                for name, item in assets.items()), "Invalid portrait digest metadata")
    require(set(BASE_FILES) <= names <= set(BASE_FILES) | set(SOURCE_FILES) | set(assets)
            and set(assets) <= names,
            "Invalid baseline manifest")
    for name, digest in record["files"].items():
        regular_path(workspace / name)
        require(sha256(workspace / name) == digest, f"Baseline changed: {name}; review and reseal")
    return record
