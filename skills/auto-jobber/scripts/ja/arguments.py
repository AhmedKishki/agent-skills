"""Command syntax; profile confirmation and user-authored wording are explicit steps."""
import argparse
import os
from pathlib import Path


def parser():
    cli = argparse.ArgumentParser(description="Auto-jobber profile, CV and application workflow")
    default = os.environ.get("AUTO_JOBBER_HOME", "~/.local/share/auto-jobber")
    cli.add_argument("--workspace", type=lambda p: Path(p).expanduser(), default=Path(default).expanduser())
    commands = cli.add_subparsers(dest="command", required=True)
    for name in ("init", "doctor", "status"):
        commands.add_parser(name)
    for name in ("seal", "preview"):
        command = commands.add_parser(name)
        command.add_argument("--language", choices=("en", "de"))
        command.add_argument("--html", type=Path)
        command.add_argument("--css", type=Path)
    for name in ("bootstrap", "intake"):
        command = commands.add_parser(name)
        command.add_argument("--data", required=True, type=Path)
    extract = commands.add_parser("extract")
    extract.add_argument("--input", type=Path, required=True)
    extract.add_argument("--output", type=Path, required=True)
    current = commands.add_parser("confirm-current")
    current.add_argument("--note", required=True)
    current.add_argument("--confirmed-by-user", action="store_true", required=True)
    remember = commands.add_parser("remember-voice")
    remember.add_argument("--text-file", required=True, type=Path)
    remember.add_argument("--source", required=True)
    new = commands.add_parser("new", help="Snapshot approved source and complete vacancy")
    posting = new.add_mutually_exclusive_group(required=True)
    posting.add_argument("--job", type=Path)
    posting.add_argument("--url")
    new.add_argument("--language", choices=("en", "de"), required=True)
    for name in ("check", "build", "source", "wording", "approve-translation"):
        command = commands.add_parser(name)
        command.add_argument("--application", required=True, type=Path)
        if name == "build":
            command.add_argument("--html-only", action="store_true")
        if name == "source":
            command.add_argument("--url", required=True)
            command.add_argument("--title", required=True)
            command.add_argument("--kind", choices=("primary", "secondary"), required=True)
            command.add_argument("--text-file", type=Path)
            command.add_argument("--published-at")
        if name == "wording":
            command.add_argument("--text-file", required=True, type=Path)
            command.add_argument("--source", required=True)
            command.add_argument("--must-include", action="append")
            command.add_argument("--language", choices=("en", "de"))
        if name == "approve-translation":
            command.add_argument("--text-file", type=Path, required=True)
            command.add_argument("--source", required=True)
            command.add_argument("--language", choices=("en", "de"), required=True)
            command.add_argument("--confirmed-by-user", action="store_true", required=True)
    for name in ("archive", "verify"):
        command = commands.add_parser(name)
        command.add_argument("--build", required=True, type=Path)
    return cli
