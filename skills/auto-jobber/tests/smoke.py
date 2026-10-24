"""Create reviewable synthetic artifacts outside the installed skill directory."""
import argparse
import json
import tempfile
from pathlib import Path

from support import fixture
from ja.build import build_application
from bilingual_fixture import german_fixture


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--language", choices=("en", "de"), default="en")
    args = parser.parse_args()
    root = args.output or Path(tempfile.mkdtemp(prefix="auto-jobber-smoke-"))
    if args.output:
        root.mkdir(mode=0o700, parents=True, exist_ok=False)
    _, app = german_fixture(root) if args.language == "de" else fixture(root)
    result = build_application(app)
    print(json.dumps({"fixture": "Fictional candidate and employer; not a real application",
                      "root": str(root), **result}, indent=2))


if __name__ == "__main__":
    main()
