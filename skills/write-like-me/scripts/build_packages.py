#!/usr/bin/env python3
"""Build lean runtime artifacts plus a separate source and evaluation bundle."""

from __future__ import annotations

import argparse
import hashlib
import json
import zipfile
from pathlib import Path


RUNTIME_SCRIPTS = {
    "build_starter_voice_file.py",
    "update_writing_pattern.py",
    "verify_rewrite.py",
}
EXCLUDED_DIRECTORIES = {
    ".git",
    ".next",
    ".wrangler",
    "__pycache__",
    "dist",
    "node_modules",
    "out",
}
FIXED_ZIP_TIMESTAMP = (2026, 1, 1, 0, 0, 0)


def included(path: Path, *, package: str) -> bool:
    if any(part in EXCLUDED_DIRECTORIES for part in path.parts):
        return False
    if path.suffix in {".pyc", ".pyo", ".zip"}:
        return False
    if path.name == ".DS_Store":
        return False
    if package == "claude":
        allowed_roots = {"SKILL.md", "references", "scripts"}
        if path.parts[0] not in allowed_roots:
            return False
        if path.parts[0] == "scripts" and path.name not in RUNTIME_SCRIPTS:
            return False
    if package == "openai":
        if path.parts == (".codex-plugin", "plugin.json"):
            return True
        if path.parts[:2] == (".codex-plugin", "assets"):
            return True
        if path.parts in {
            ("ACKNOWLEDGEMENTS.md",),
            ("LICENSE",),
            ("PRIVACY.md",),
            ("README.md",),
            ("TERMS.md",),
        }:
            return True
        skill_prefix = ("skills", "write-like-me")
        if path.parts[:2] != skill_prefix:
            return False
        skill_relative = path.parts[2:]
        if not skill_relative:
            return False
        allowed_roots = {"SKILL.md", "agents", "references", "scripts"}
        if skill_relative[0] not in allowed_roots:
            return False
        if skill_relative[0] == "scripts" and path.name not in RUNTIME_SCRIPTS:
            return False
    return True


def write_zip(source: Path, target: Path, *, package: str) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    root_name = "write-like-me"
    with zipfile.ZipFile(target, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(source.rglob("*")):
            if not path.is_file():
                continue
            relative = path.relative_to(source)
            if included(relative, package=package):
                archive_path = (Path(root_name) / relative).as_posix()
                info = zipfile.ZipInfo(archive_path, date_time=FIXED_ZIP_TIMESTAMP)
                info.compress_type = zipfile.ZIP_DEFLATED
                permissions = 0o755 if path.stat().st_mode & 0o111 else 0o644
                info.external_attr = permissions << 16
                archive.writestr(info, path.read_bytes())


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def validate_archive(path: Path, *, package: str) -> None:
    with zipfile.ZipFile(path) as archive:
        names = set(archive.namelist())
    if package == "claude":
        required = {"write-like-me/SKILL.md"}
    else:
        required = {
            "write-like-me/.codex-plugin/assets/composer-icon.png",
            "write-like-me/.codex-plugin/assets/logo.png",
            "write-like-me/.codex-plugin/plugin.json",
            "write-like-me/ACKNOWLEDGEMENTS.md",
            "write-like-me/LICENSE",
            "write-like-me/PRIVACY.md",
            "write-like-me/README.md",
            "write-like-me/TERMS.md",
            "write-like-me/skills/write-like-me/SKILL.md",
        }
    missing = required - names
    if missing:
        raise ValueError(f"Archive {path.name} is missing: {', '.join(sorted(missing))}")
    if package == "openai":
        with zipfile.ZipFile(path) as archive:
            manifest = json.loads(
                archive.read("write-like-me/.codex-plugin/plugin.json").decode("utf-8")
            )
        interface = manifest.get("interface", {})
        expected_assets = {
            "composerIcon": "./.codex-plugin/assets/composer-icon.png",
            "logo": "./.codex-plugin/assets/logo.png",
        }
        for field, expected_path in expected_assets.items():
            if interface.get(field) != expected_path:
                raise ValueError(
                    f"OpenAI manifest {field} must reference {expected_path}."
                )
    if any("__pycache__" in name or name.endswith(".pyc") for name in names):
        raise ValueError(f"Archive {path.name} contains Python cache files.")
    if package == "claude" and any(name.startswith("write-like-me/agents/") for name in names):
        raise ValueError("Claude archive contains OpenAI-only agent metadata.")
    if package == "openai" and any(
        segment in name
        for name in names
        for segment in ("/tests/", "/evaluations/", "run_blind_beta.py", "evaluate_scenarios.py", "build_packages.py")
    ):
        raise ValueError("OpenAI production archive contains development or evaluation material.")
    if package == "source" and "write-like-me/skills/write-like-me/tests/test_package_contract.py" not in names:
        raise ValueError("Source archive is missing the evaluation and test suite.")


def build(output_dir: Path, *, include_source: bool = True) -> dict[str, dict[str, str]]:
    script_path = Path(__file__).resolve()
    skill_root = script_path.parents[1]
    plugin_root = script_path.parents[3]
    manifest = json.loads((plugin_root / ".codex-plugin" / "plugin.json").read_text(encoding="utf-8"))
    version = manifest["version"]

    artifacts = {
        "claude": output_dir / f"write-like-me-claude-skill-{version}.zip",
        "openai": output_dir / f"write-like-me-openai-plugin-{version}.zip",
    }
    if include_source:
        artifacts["source"] = output_dir / f"write-like-me-source-evaluation-{version}.zip"
    write_zip(skill_root, artifacts["claude"], package="claude")
    write_zip(plugin_root, artifacts["openai"], package="openai")
    validate_archive(artifacts["claude"], package="claude")
    validate_archive(artifacts["openai"], package="openai")
    if include_source:
        write_zip(plugin_root, artifacts["source"], package="source")
        validate_archive(artifacts["source"], package="source")

    return {
        name: {"path": str(path), "sha256": sha256(path)}
        for name, path in artifacts.items()
    }


def public_manifest(result: dict[str, dict[str, str]]) -> dict[str, dict[str, str]]:
    return {
        name: {
            "file": Path(details["path"]).name,
            "sha256": details["sha256"],
        }
        for name, details in result.items()
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", required=True, help="Directory for built ZIP files and checksums.")
    parser.add_argument(
        "--runtime-only",
        action="store_true",
        help="Build only the Claude and OpenAI runtime packages.",
    )
    args = parser.parse_args()
    result = build(
        Path(args.output_dir).expanduser().resolve(),
        include_source=not args.runtime_only,
    )
    output_dir = Path(args.output_dir).expanduser().resolve()
    checksum_lines = [
        f"{details['sha256']}  {Path(details['path']).name}"
        for details in result.values()
    ]
    (output_dir / "SHA256SUMS.txt").write_text(
        "\n".join(checksum_lines) + "\n",
        encoding="utf-8",
    )
    (output_dir / "BUILD-MANIFEST.json").write_text(
        json.dumps(public_manifest(result), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    for name, details in result.items():
        print(f"{name}: {details['path']}")
        print(f"{name} sha256: {details['sha256']}")


if __name__ == "__main__":
    main()
