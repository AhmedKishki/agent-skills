#!/usr/bin/env python3
"""Build a full-export ZIP from a draft-writing activity tracker."""

from __future__ import annotations

import argparse
import hashlib
import os
import re
import stat
import sys
import tempfile
import zipfile
from dataclasses import dataclass
from pathlib import Path, PurePosixPath, PureWindowsPath
from typing import BinaryIO, Iterable, Optional, Sequence, Tuple


_HEADERS = {
    ("Tracked filename", "Role/state"),
    ("Active filename", "Role/state"),
}
_SEPARATOR = re.compile(r"^:?-{3,}:?$")
_CHUNK_SIZE = 1024 * 1024
_ZIP64_THRESHOLD = 2 * 1024 * 1024 * 1024
StatSignature = Tuple[int, int, int, int, int]


class ExportError(Exception):
    """A user-correctable full-export error."""


@dataclass(frozen=True)
class Member:
    archive_name: str
    source_path: Optional[Path]
    snapshot: Optional[bytes] = None
    snapshot_signature: Optional[StatSignature] = None


@dataclass(frozen=True)
class Fingerprint:
    size: int
    sha256: bytes


@dataclass(frozen=True)
class Capture:
    fingerprint: Fingerprint
    signature: StatSignature


def _markdown_row(line: str) -> Optional[list[str]]:
    """Return cells from a pipe table row, unescaping Markdown pipe escapes."""
    stripped = line.strip()
    if len(stripped) < 2 or not stripped.startswith("|") or not stripped.endswith("|"):
        return None

    cells: list[str] = []
    cell: list[str] = []
    index = 1
    end = len(stripped) - 1
    while index < end:
        character = stripped[index]
        if character == "\\" and index + 1 < end and stripped[index + 1] == "|":
            cell.append("|")
            index += 2
            continue
        if character == "|":
            cells.append("".join(cell).strip())
            cell = []
        else:
            cell.append(character)
        index += 1
    cells.append("".join(cell).strip())
    return cells


def _filename_from_cell(cell: str, row_number: int) -> str:
    value = cell.strip()
    if value.startswith("`") or value.endswith("`"):
        if len(value) < 2 or value[0] != "`" or value[-1] != "`" or "`" in value[1:-1]:
            raise ExportError(f"row {row_number} has malformed inline-code filename markup")
        value = value[1:-1]
    if not value:
        raise ExportError(f"row {row_number} has an empty tracked filename")
    if "\x00" in value:
        raise ExportError(f"row {row_number} filename contains a null byte")
    return value


def _tracked_filenames(tracker_text: str) -> list[tuple[str, int]]:
    lines = tracker_text.splitlines()
    headers: list[tuple[int, tuple[str, str]]] = []
    for index, line in enumerate(lines):
        cells = _markdown_row(line)
        if cells is not None and tuple(cells) in _HEADERS:
            headers.append((index, (cells[0], cells[1])))

    if not headers:
        raise ExportError(
            "activity tracker has no '| Tracked filename | Role/state |' table "
            "(legacy 'Active filename' is also accepted)"
        )
    if len(headers) != 1:
        raise ExportError("activity tracker contains more than one tracked-file table")

    header_index, _ = headers[0]
    separator_index = header_index + 1
    if separator_index >= len(lines):
        raise ExportError("tracked-file table is missing its separator row")
    separator_cells = _markdown_row(lines[separator_index])
    if (
        separator_cells is None
        or len(separator_cells) != 2
        or any(_SEPARATOR.fullmatch(cell) is None for cell in separator_cells)
    ):
        raise ExportError("tracked-file table has an invalid separator row")

    filenames: list[tuple[str, int]] = []
    for index in range(separator_index + 1, len(lines)):
        cells = _markdown_row(lines[index])
        if cells is None:
            break
        row_number = index + 1
        if len(cells) != 2:
            raise ExportError(f"tracked-file table row {row_number} must contain exactly two cells")
        filenames.append((_filename_from_cell(cells[0], row_number), row_number))
    return filenames


def _is_within(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root)
    except ValueError:
        return False
    return True


def _portable_relative_path(raw_name: str, row_number: int) -> tuple[str, tuple[str, ...]]:
    posix_path = PurePosixPath(raw_name)
    windows_path = PureWindowsPath(raw_name)
    if posix_path.is_absolute() or windows_path.is_absolute() or windows_path.drive or windows_path.root:
        raise ExportError(f"row {row_number} uses an absolute tracked path: {raw_name!r}")

    portable_name = raw_name.replace("\\", "/")
    parts = tuple(portable_name.split("/"))
    if any(part == ".." for part in parts):
        raise ExportError(f"row {row_number} uses path traversal: {raw_name!r}")
    if any(part in {"", "."} for part in parts):
        raise ExportError(f"row {row_number} uses a non-canonical tracked path: {raw_name!r}")

    archive_name = PurePosixPath(*parts).as_posix()
    return archive_name, parts


def _resolve_output(raw_output: str) -> Path:
    output_argument = Path(raw_output)
    if output_argument.suffix.lower() != ".zip":
        raise ExportError("output filename must end in .zip")
    try:
        output_directory = output_argument.parent.resolve(strict=True)
    except FileNotFoundError as error:
        raise ExportError(f"output directory does not exist: {output_argument.parent}") from error
    if not output_directory.is_dir():
        raise ExportError(f"output parent is not a directory: {output_argument.parent}")
    return output_directory / output_argument.name


def _stat_signature(file_stat: os.stat_result) -> StatSignature:
    return (
        file_stat.st_dev,
        file_stat.st_ino,
        file_stat.st_size,
        file_stat.st_mtime_ns,
        file_stat.st_ctime_ns,
    )


def _copy_and_fingerprint(source: Path, destination: BinaryIO) -> Capture:
    digest = hashlib.sha256()
    size = 0
    with source.open("rb") as input_file:
        before = os.fstat(input_file.fileno())
        if not stat.S_ISREG(before.st_mode):
            raise ExportError(f"tracked input is not a regular file: {source}")
        while True:
            chunk = input_file.read(_CHUNK_SIZE)
            if not chunk:
                break
            destination.write(chunk)
            digest.update(chunk)
            size += len(chunk)
        after = os.fstat(input_file.fileno())
    if _stat_signature(before) != _stat_signature(after) or size != before.st_size:
        raise ExportError(f"tracked input changed while it was being archived: {source}")
    return Capture(
        fingerprint=Fingerprint(size=size, sha256=digest.digest()),
        signature=_stat_signature(after),
    )


def _fingerprint(stream: BinaryIO) -> Fingerprint:
    digest = hashlib.sha256()
    size = 0
    while True:
        chunk = stream.read(_CHUNK_SIZE)
        if not chunk:
            break
        digest.update(chunk)
        size += len(chunk)
    return Fingerprint(size=size, sha256=digest.digest())


def _write_archive(temporary_path: Path, members: Sequence[Member]) -> list[Capture]:
    captures: list[Capture] = []
    with zipfile.ZipFile(
        temporary_path,
        mode="w",
        compression=zipfile.ZIP_DEFLATED,
        allowZip64=True,
    ) as archive:
        for member in members:
            if member.snapshot is not None:
                if member.snapshot_signature is None:
                    raise ExportError(f"snapshot member has no file signature: {member.archive_name}")
                archive.writestr(member.archive_name, member.snapshot)
                captures.append(
                    Capture(
                        fingerprint=Fingerprint(
                            size=len(member.snapshot),
                            sha256=hashlib.sha256(member.snapshot).digest(),
                        ),
                        signature=member.snapshot_signature,
                    )
                )
                continue
            if member.source_path is None:
                raise ExportError(f"archive member has no input: {member.archive_name}")

            source_size = member.source_path.stat().st_size
            with archive.open(
                member.archive_name,
                mode="w",
                force_zip64=source_size >= _ZIP64_THRESHOLD,
            ) as destination:
                captures.append(_copy_and_fingerprint(member.source_path, destination))
    return captures


def _verify_archive(
    temporary_path: Path,
    members: Sequence[Member],
    expected_captures: Sequence[Capture],
) -> None:
    expected_names = [member.archive_name for member in members]
    with zipfile.ZipFile(temporary_path, mode="r") as archive:
        actual_names = [info.filename for info in archive.infolist()]
        if actual_names != expected_names:
            raise ExportError("ZIP verification failed: member names differ from the tracked set")
        for member, expected in zip(members, expected_captures):
            with archive.open(member.archive_name, mode="r") as archived_file:
                actual = _fingerprint(archived_file)
            if actual != expected.fingerprint:
                raise ExportError(f"ZIP verification failed for member: {member.archive_name}")


def _capture_current_input(source: Path) -> Capture:
    with source.open("rb") as input_file:
        before = os.fstat(input_file.fileno())
        if not stat.S_ISREG(before.st_mode):
            raise ExportError(f"tracked input is no longer a regular file: {source}")
        fingerprint = _fingerprint(input_file)
        after = os.fstat(input_file.fileno())
    if _stat_signature(before) != _stat_signature(after) or fingerprint.size != before.st_size:
        raise ExportError(f"tracked input changed during final verification: {source}")
    return Capture(fingerprint=fingerprint, signature=_stat_signature(after))


def _verify_inputs_unchanged(members: Sequence[Member], expected: Sequence[Capture]) -> None:
    for member, archived_capture in zip(members, expected):
        if member.source_path is None:
            raise ExportError(f"archive member has no input for final verification: {member.archive_name}")
        current_capture = _capture_current_input(member.source_path)
        if current_capture != archived_capture:
            raise ExportError(f"tracked input changed during export: {member.archive_name}")


def _members_for_export(tracker_argument: str, output: Path) -> list[Member]:
    tracker_lexical = Path(tracker_argument).absolute()
    if tracker_lexical.suffix.lower() != ".md":
        raise ExportError("activity tracker filename must end in .md")
    try:
        tracker_path = tracker_lexical.resolve(strict=True)
    except FileNotFoundError as error:
        raise ExportError(f"activity tracker does not exist: {tracker_argument}") from error
    if not tracker_path.is_file():
        raise ExportError(f"activity tracker is not a regular file: {tracker_argument}")

    tracker_root = tracker_lexical.parent.resolve(strict=True)
    tracker_archive_name = tracker_lexical.name
    if tracker_archive_name in {"", ".", ".."} or "\\" in tracker_archive_name:
        raise ExportError("activity tracker filename is not safe for a ZIP member")
    if tracker_path == output:
        raise ExportError("output path is also the activity tracker input")

    before_read = tracker_path.stat()
    try:
        tracker_bytes = tracker_path.read_bytes()
    except OSError as error:
        raise ExportError(f"cannot read activity tracker: {tracker_argument}: {error}") from error
    after_read = tracker_path.stat()
    if _stat_signature(before_read) != _stat_signature(after_read):
        raise ExportError("activity tracker changed while it was being read")
    try:
        tracker_text = tracker_bytes.decode("utf-8-sig")
    except UnicodeDecodeError as error:
        raise ExportError("activity tracker is not valid UTF-8 Markdown") from error

    tracker_signature = _stat_signature(after_read)
    members = [Member(tracker_archive_name, tracker_path, tracker_bytes, tracker_signature)]
    archive_names = {tracker_archive_name}
    resolved_inputs = {tracker_path}
    for raw_name, row_number in _tracked_filenames(tracker_text):
        archive_name, parts = _portable_relative_path(raw_name, row_number)
        if archive_name in archive_names:
            raise ExportError(f"duplicate ZIP member name in row {row_number}: {archive_name}")
        archive_names.add(archive_name)

        lexical_source = tracker_root.joinpath(*parts)
        prospective_source = lexical_source.resolve(strict=False)
        if not _is_within(prospective_source, tracker_root):
            raise ExportError(f"row {row_number} resolves outside the tracker directory: {raw_name!r}")
        if prospective_source == output:
            raise ExportError(f"row {row_number} lists the output ZIP as an input: {raw_name!r}")
        try:
            source_path = lexical_source.resolve(strict=True)
        except FileNotFoundError as error:
            raise ExportError(f"tracked input does not exist in row {row_number}: {raw_name!r}") from error
        if not _is_within(source_path, tracker_root):
            raise ExportError(f"row {row_number} resolves outside the tracker directory: {raw_name!r}")
        if not source_path.is_file():
            raise ExportError(f"tracked input is not a regular file in row {row_number}: {raw_name!r}")
        if source_path in resolved_inputs:
            raise ExportError(f"row {row_number} resolves to an input already listed: {raw_name!r}")
        resolved_inputs.add(source_path)
        members.append(Member(archive_name, source_path))
    return members


def build_full_export(tracker_argument: str, output_argument: str) -> tuple[Path, int]:
    output = _resolve_output(output_argument)
    members = _members_for_export(tracker_argument, output)
    if os.path.lexists(output):
        raise ExportError(f"output path already exists: {output}")

    descriptor, raw_temporary_path = tempfile.mkstemp(
        prefix=f".{output.name}.",
        suffix=".tmp",
        dir=output.parent,
    )
    os.close(descriptor)
    temporary_path = Path(raw_temporary_path)
    published = False
    try:
        captures = _write_archive(temporary_path, members)
        _verify_archive(temporary_path, members, captures)
        with temporary_path.open("rb") as temporary_file:
            os.fsync(temporary_file.fileno())
        _verify_inputs_unchanged(members, captures)
        try:
            os.link(temporary_path, output)
        except FileExistsError as error:
            raise ExportError(f"output path appeared during export: {output}") from error
        except OSError as error:
            raise ExportError(f"could not publish the ZIP atomically: {error}") from error
        published = True
    finally:
        try:
            temporary_path.unlink()
        except FileNotFoundError:
            pass
    if not published:
        raise ExportError("full export was not published")
    return output, len(members)


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Zip an activity tracker and every file in its tracked-file table.",
    )
    parser.add_argument("tracker", metavar="TRACKER.md")
    parser.add_argument("output", metavar="OUTPUT.zip")
    return parser


def main(argv: Optional[Iterable[str]] = None) -> int:
    parser = _parser()
    arguments = parser.parse_args(argv)
    try:
        output, member_count = build_full_export(arguments.tracker, arguments.output)
    except (ExportError, OSError, zipfile.BadZipFile, zipfile.LargeZipFile) as error:
        print(f"error: {error}", file=sys.stderr)
        return 1
    print(f"Created full export: {output} ({member_count} files)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
