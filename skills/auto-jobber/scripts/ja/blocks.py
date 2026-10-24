"""Patch plain-text marker regions without reserialising the surrounding HTML."""
import difflib
import html
import re

from .common import require

MARKER = r"<!--\s*cv:([a-z][a-z0-9-]*)\s*-->"
PAIR = re.compile(MARKER + r"(.*?)<!--\s*/cv:\1\s*-->", re.S)


def read_blocks(source):
    matches = list(PAIR.finditer(source))
    result = {}
    for match in matches:
        key, raw = match.group(1, 2)
        require(key not in result, f"Duplicate CV block: {key}")
        require("<" not in raw, f"CV block {key} must contain plain escaped text")
        result[key] = {"text": html.unescape(raw), "span": match.span(2)}
    # Each complete block has exactly two marker comments.
    require(2 * len(matches) == len(re.findall(r"<!--\s*/?cv:", source)),
            "Unpaired, nested or malformed CV markers")
    return result


def apply_edits(source, edits):
    blocks, replacements, seen = read_blocks(source), [], set()
    for edit in edits:
        key = edit["block_id"]
        require(key in blocks and key not in seen, f"Unknown or repeated CV block: {key}")
        require(edit["before"] == blocks[key]["text"], f"Stale before-text for {key}")
        after = edit["after"]
        require(isinstance(after, str) and after.strip(), f"Cannot erase CV block {key}")
        require(after != edit["before"], f"No-op edit for {key}")
        start, end = blocks[key]["span"]
        replacements.append((start, end, html.escape(after, quote=False)))
        seen.add(key)
    for start, end, after in sorted(replacements, reverse=True):
        source = source[:start] + after + source[end:]
    return source


def changed_words(before, after):
    left, right = before.split(), after.split()
    return sum(max(i2 - i1, j2 - j1) for kind, i1, i2, j1, j2 in
               difflib.SequenceMatcher(None, left, right, autojunk=False).get_opcodes()
               if kind != "equal")
