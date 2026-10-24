"""Freeze artifact hashes and archive only previously checked output files."""
import shutil
import uuid
from pathlib import Path

from .common import read_json, require, safe_child, sha256, utc_now, write_json


def tree_files(folder):
    files = []
    for path in sorted(folder.rglob("*")):
        require(not path.is_symlink(), f"Symlinks are forbidden in builds: {path.name}")
        require(path.is_file() or path.is_dir(), f"Nonregular build entry: {path.name}")
        if path.is_file() and path != folder / "manifest.json":
            files.append(path)
    return files


def save_manifest(folder, metadata):
    files = {str(path.relative_to(folder)): sha256(path) for path in tree_files(folder)}
    record = {"schema_version": 1, "created_at": utc_now(), **metadata, "files": files}
    write_json(folder / "manifest.json", record)
    return record


def verify_manifest(folder):
    folder = Path(folder).expanduser()
    require(not folder.is_symlink(), "Build directory must not be a symlink")
    folder = folder.resolve()
    record = read_json(folder / "manifest.json")
    actual = {str(path.relative_to(folder)) for path in tree_files(folder)}
    require(actual == set(record["files"]), "Build file set changed")
    for name, digest in record["files"].items():
        require(sha256(safe_child(folder, name)) == digest, f"Build changed: {name}")
    return record


def archive(build):
    build = Path(build).expanduser().resolve()
    verify_manifest(build)
    require(build.parent.name == "builds", "Archive expects an application builds/<id> directory")
    target = build.parent.parent / "archive" / build.name
    target.parent.mkdir(mode=0o700, exist_ok=True)
    require(not target.exists(), "This build is already archived")
    stage = target.with_name(".archiving-" + uuid.uuid4().hex)
    try:
        shutil.copytree(build, stage, symlinks=True)
        verify_manifest(stage)
        stage.rename(target)
    finally:
        if stage.exists():
            shutil.rmtree(stage)
    return {"archive": str(target), "note": "Archived locally; no application was submitted"}
