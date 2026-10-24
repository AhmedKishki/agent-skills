#!/usr/bin/env python3
"""Entry point: run with --help; no model credentials or server are required."""
import json
import os
import sys

from ja.cli import main

if __name__ == "__main__":
    os.umask(0o077)
    try:
        result = main()
        print(json.dumps(result, ensure_ascii=False, indent=2))
    except (OSError, ValueError, KeyError, TypeError, RuntimeError) as error:
        print(json.dumps({"error": str(error)}, ensure_ascii=False), file=sys.stderr)
        sys.exit(1)
