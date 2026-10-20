#!/usr/bin/env python3
"""Record one user-confirmed correction in a portable writing-pattern file.

The script stores the confirmed behavioural rule and hashes of the before/after
texts. It never stores the edited drafts themselves in the portable profile.
"""

from __future__ import annotations

import argparse
import difflib
import hashlib
import json
import re
from pathlib import Path
from typing import Any


START_MARKER = "<!-- WLM_CONFIRMED_CORRECTIONS_START -->"
END_MARKER = "<!-- WLM_CONFIRMED_CORRECTIONS_END -->"
MAX_PROFILE_CHARS = 100_000
MAX_DRAFT_CHARS = 200_000
MAX_RULE_CHARS = 240
MAX_CONTEXT_CHARS = 80
MAX_CORRECTIONS = 12


def read_limited(path: str, limit: int, label: str) -> str:
    value = Path(path).read_text(encoding="utf-8")
    if len(value) > limit:
        raise ValueError(f"{label} exceeds the {limit:,}-character limit.")
    return value


def text_hash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def diff_summary(original: str, edited: str) -> dict[str, int]:
    matcher = difflib.SequenceMatcher(a=original.split(), b=edited.split(), autojunk=False)
    counts = {"inserted_words": 0, "deleted_words": 0, "replaced_source_words": 0, "unchanged_words": 0}
    for tag, a_start, a_end, b_start, b_end in matcher.get_opcodes():
        if tag == "equal":
            counts["unchanged_words"] += a_end - a_start
        elif tag == "insert":
            counts["inserted_words"] += b_end - b_start
        elif tag == "delete":
            counts["deleted_words"] += a_end - a_start
        elif tag == "replace":
            counts["replaced_source_words"] += a_end - a_start
            counts["inserted_words"] += b_end - b_start
    return counts


def parse_existing(block: str) -> list[str]:
    return [
        line.strip()
        for line in block.splitlines()
        if line.strip().startswith("- [")
    ]


def update_profile(
    profile: str,
    *,
    rule: str,
    context: str,
    original: str,
    edited: str,
) -> tuple[str, dict[str, Any]]:
    clean_rule = " ".join(rule.split()).strip().rstrip(".")
    clean_context = " ".join(context.split()).strip() or "general"
    if not clean_rule:
        raise ValueError("A user-confirmed behavioural rule is required.")
    if len(clean_rule) > MAX_RULE_CHARS:
        raise ValueError(f"Rule exceeds the {MAX_RULE_CHARS}-character limit.")
    if len(clean_context) > MAX_CONTEXT_CHARS:
        raise ValueError(f"Context exceeds the {MAX_CONTEXT_CHARS}-character limit.")
    if original == edited:
        raise ValueError("The original and edited texts are identical; there is no correction to record.")

    rule_id = hashlib.sha256(f"{clean_context.casefold()}|{clean_rule.casefold()}".encode("utf-8")).hexdigest()[:12]
    original_hash = text_hash(original)
    edited_hash = text_hash(edited)
    measured_diff = diff_summary(original, edited)
    embedded_metadata = (
        f"original={original_hash[:16]};edited={edited_hash[:16]};"
        f"inserted={measured_diff['inserted_words']};"
        f"deleted={measured_diff['deleted_words']};"
        f"replaced={measured_diff['replaced_source_words']}"
    )
    entry = (
        f"- [{clean_context}] {clean_rule}. `confirmed:{rule_id}` "
        f"<!-- WLM_CORRECTION_META {embedded_metadata} -->"
    )
    block_pattern = re.compile(
        re.escape(START_MARKER) + r"(.*?)" + re.escape(END_MARKER),
        re.S,
    )
    existing_match = block_pattern.search(profile)
    existing = parse_existing(existing_match.group(1)) if existing_match else []
    existing = [line for line in existing if f"confirmed:{rule_id}" not in line]
    entries = [entry, *existing][:MAX_CORRECTIONS]
    replacement = (
        f"{START_MARKER}\n"
        "## Confirmed corrections\n\n"
        "These rules came from edits I explicitly confirmed. Apply them only in the named context.\n\n"
        + "\n".join(entries)
        + f"\n{END_MARKER}"
    )
    if existing_match:
        updated = block_pattern.sub(replacement, profile, count=1)
    else:
        updated = profile.rstrip() + "\n\n" + replacement + "\n"

    metadata = {
        "schema_version": "1.0",
        "rule_id": rule_id,
        "context": clean_context,
        "rule": clean_rule,
        "original_sha256": original_hash,
        "edited_sha256": edited_hash,
        "diff": measured_diff,
        "stored_correction_count": len(entries),
        "draft_text_stored_in_profile": False,
    }
    return updated, metadata


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", required=True, help="Existing MY_WRITING_PATTERN.md path.")
    parser.add_argument("--original", required=True, help="Original generated draft path.")
    parser.add_argument("--edited", required=True, help="User-edited draft path.")
    parser.add_argument("--rule", required=True, help="Behavioural correction explicitly confirmed by the user.")
    parser.add_argument("--context", default="general", help="Context where the rule applies, such as email or LinkedIn.")
    parser.add_argument("--output", help="Updated profile path. Defaults to replacing --profile.")
    parser.add_argument("--metadata-json", help="Optional correction metadata JSON path.")
    args = parser.parse_args()

    try:
        profile = read_limited(args.profile, MAX_PROFILE_CHARS, "Profile")
        original = read_limited(args.original, MAX_DRAFT_CHARS, "Original draft")
        edited = read_limited(args.edited, MAX_DRAFT_CHARS, "Edited draft")
        updated, metadata = update_profile(
            profile,
            rule=args.rule,
            context=args.context,
            original=original,
            edited=edited,
        )
        output_path = Path(args.output or args.profile)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(updated, encoding="utf-8")
        if args.metadata_json:
            metadata_path = Path(args.metadata_json)
            metadata_path.parent.mkdir(parents=True, exist_ok=True)
            metadata_path.write_text(json.dumps(metadata, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    except (OSError, UnicodeError, ValueError) as error:
        parser.error(str(error))

    print(f"Wrote {output_path}")
    print(f"Recorded confirmed correction {metadata['rule_id']}")


if __name__ == "__main__":
    main()
