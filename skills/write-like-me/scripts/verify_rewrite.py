#!/usr/bin/env python3
"""Block a Write Like Me rewrite when deterministic integrity checks fail.

This verifier is deliberately narrow. It catches exact-value drift, changed
modality classes, likely named-entity omissions, obvious unsupported
autobiographical claims, and phrase leakage from style samples. Polarity-marker
movement is a warning for named-sentence review, not a release blocker. The
verifier does not prove full semantic equivalence, so a language-model meaning
review remains required.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from collections import Counter
from pathlib import Path
from typing import Any, Iterable


MAX_TEXT_CHARS = 200_000
TOKEN_RE = re.compile(r"[^\W\d_]+(?:['-][^\W\d_]+)*|\d+(?:[.,:/-]\d+)*%?", re.UNICODE)
EXACT_VALUE_RE = re.compile(
    r"""
    (?<![\w])
    (?:
        \d{1,4}(?:[-/]\d{1,2}){1,2}
        |
        (?:[$£€¥₹]\s*)?\d+(?:,\d{3})*(?:\.\d+)?(?:\s*%)?
    )
    (?![\w])
    """,
    re.VERBOSE,
)
URL_RE = re.compile(r"\bhttps?://[^\s<>()\[\]{}]+", re.I)
EMAIL_RE = re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.I)
QUOTE_RE = re.compile(r"[\"“]([^\"”\n]{2,500})[\"”]")
AUTOBIOGRAPHY_PATTERNS = (
    re.compile(r"\bI (?:remember|met|worked with|spoke to|talked to|saw|felt|experienced|witnessed|learned)\b", re.I),
    re.compile(r"\bmy (?:client|customer|team|colleague|friend|family|partner|manager|employee|experience|story)\b", re.I),
    re.compile(r"\bwhen I was\b|\bin my (?:career|job|life|childhood|experience)\b", re.I),
    re.compile(
        r"\b(?:having|after|before)\s+(?:personally\s+)?"
        r"(?:run|ran|led|managed|built|founded|launched|shipped|worked|served|joined|left|delivered)\b",
        re.I,
    ),
    re.compile(
        r"\bat my (?:last|former|previous|current|first) "
        r"(?:company|job|employer|workplace|startup|agency|firm|organisation|organization)\b",
        re.I,
    ),
    re.compile(
        r"\bI (?:have|had) (?:personally )?"
        r"(?:run|led|managed|built|founded|launched|shipped|worked|served|delivered)\b",
        re.I,
    ),
)
CONTRACTION_EXPANSIONS = {
    "can't": "can not",
    "cannot": "can not",
    "couldn't": "could not",
    "didn't": "did not",
    "doesn't": "does not",
    "don't": "do not",
    "hadn't": "had not",
    "hasn't": "has not",
    "haven't": "have not",
    "isn't": "is not",
    "mightn't": "might not",
    "mustn't": "must not",
    "shouldn't": "should not",
    "wasn't": "was not",
    "weren't": "were not",
    "won't": "will not",
    "wouldn't": "would not",
}
MODAL_CLASS_PATTERNS = (
    ("possibility", re.compile(r"\b(?:may|might|could)\b")),
    ("recommendation", re.compile(r"\b(?:should|ought\s+to)\b")),
    (
        "requirement",
        re.compile(r"\b(?:must|have\s+to|has\s+to|had\s+to|need\s+to|needs\s+to|needed\s+to)\b"),
    ),
    ("capability", re.compile(r"\b(?:can|able\s+to)\b")),
    ("commitment", re.compile(r"\b(?:will|going\s+to)\b")),
    ("conditional", re.compile(r"\bwould\b")),
)
NEGATION_RE = re.compile(r"\b(?:not|never|no|neither|nor)\b")
NEGATIVE_CONCEPT_RE = re.compile(
    r"\b(?:avoid|avoids|avoided|avoiding|deny|denies|denied|exclude|excludes|excluded|"
    r"fail|fails|failed|lack|lacks|lacked|prevent|prevents|prevented|refuse|refuses|"
    r"refused|reject|rejects|rejected|stop|stops|stopped|without)\b"
)
SENTENCE_BOUNDARY_RE = re.compile(r"(?<=[.!?])\s+|\n+")
COMMON_CAPITALIZED = {
    "A", "An", "And", "As", "At", "But", "For", "From", "He", "Her", "His",
    "How", "I", "If", "In", "It", "Its", "My", "No", "Not", "On", "Or",
    "Our", "She", "So", "That", "The", "Their", "Then", "There", "They",
    "This", "Those", "To", "We", "What", "When", "Where", "Which", "Who",
    "Why", "With", "You", "Your",
}
STOP_WORDS = {
    "a", "an", "and", "are", "as", "at", "be", "because", "but", "by", "for",
    "from", "had", "has", "have", "he", "her", "his", "i", "if", "in", "is",
    "it", "its", "me", "my", "not", "of", "on", "or", "our", "she", "so",
    "that", "the", "their", "them", "then", "there", "they", "this", "to",
    "us", "was", "we", "were", "what", "when", "which", "who", "will",
    "with", "you", "your",
}


def normalize(text: str) -> str:
    return unicodedata.normalize("NFKC", text).translate(
        str.maketrans({"’": "'", "‘": "'", "ʼ": "'", "＇": "'"})
    )


def normalize_semantics(text: str) -> str:
    normalized = normalize(text).casefold()
    for contraction, expansion in CONTRACTION_EXPANSIONS.items():
        normalized = re.sub(rf"\b{re.escape(contraction)}\b", expansion, normalized)
    return normalized


def read_text(path: str) -> str:
    text = Path(path).read_text(encoding="utf-8")
    if len(text) > MAX_TEXT_CHARS:
        raise ValueError(f"{Path(path).name} exceeds the {MAX_TEXT_CHARS:,}-character verifier limit.")
    return text


def normalized_tokens(text: str) -> list[str]:
    return [token.casefold() for token in TOKEN_RE.findall(normalize(text))]


def exact_values(text: str) -> Counter[str]:
    return Counter(match.group(0).replace(" ", "") for match in EXACT_VALUE_RE.finditer(normalize(text)))


def exact_strings(pattern: re.Pattern[str], text: str) -> Counter[str]:
    return Counter(match.group(0) for match in pattern.finditer(text))


def quoted_strings(text: str) -> Counter[str]:
    return Counter(match.group(1).strip() for match in QUOTE_RE.finditer(text))


def modal_signature(text: str) -> dict[str, int]:
    normalized = normalize_semantics(text)
    return {name: len(pattern.findall(normalized)) for name, pattern in MODAL_CLASS_PATTERNS}


def polarity_sentences(text: str) -> list[str]:
    sentences = [
        re.sub(r"\s+", " ", sentence).strip()
        for sentence in SENTENCE_BOUNDARY_RE.split(normalize(text))
        if sentence.strip()
    ]
    return [
        sentence
        for sentence in sentences
        if NEGATION_RE.search(normalize_semantics(sentence))
        or NEGATIVE_CONCEPT_RE.search(normalize_semantics(sentence))
    ]


def named_entity_candidates(text: str) -> set[str]:
    normalized = normalize(text)
    entities = set(re.findall(r"\b[A-Z]{2,}(?:\s+[A-Z]{2,})*\b", normalized))
    entities.update(
        match.group(0)
        for match in re.finditer(r"\b[A-Z][\w'-]+(?:[ \t]+[A-Z][\w'-]+)+\b", normalized)
        if match.group(0) not in COMMON_CAPITALIZED
    )
    entities.update(
        match.group(0)
        for match in re.finditer(r"\b[A-Z][\w'-]{2,}\b", normalized)
        if match.group(0) not in COMMON_CAPITALIZED
    )
    return entities


def distinctive_shingles(text: str, size: int = 6) -> set[tuple[str, ...]]:
    tokens = normalized_tokens(text)
    shingles: set[tuple[str, ...]] = set()
    for index in range(0, max(0, len(tokens) - size + 1)):
        shingle = tuple(tokens[index:index + size])
        content_count = sum(token not in STOP_WORDS for token in shingle)
        if content_count >= 4:
            shingles.add(shingle)
    return shingles


def counter_diff(expected: Counter[str], actual: Counter[str]) -> tuple[list[str], list[str]]:
    missing = sorted((expected - actual).elements())
    added = sorted((actual - expected).elements())
    return missing, added


def add_issue(
    issues: list[dict[str, Any]],
    code: str,
    message: str,
    *,
    severity: str = "critical",
    expected: Any = None,
    actual: Any = None,
) -> None:
    item: dict[str, Any] = {"severity": severity, "code": code, "message": message}
    if expected is not None:
        item["expected"] = expected
    if actual is not None:
        item["actual"] = actual
    issues.append(item)


def verify(
    source: str,
    candidate: str,
    *,
    style_samples: Iterable[str] = (),
    required_entities: Iterable[str] = (),
) -> dict[str, Any]:
    issues: list[dict[str, Any]] = []

    source_values = exact_values(source)
    candidate_values = exact_values(candidate)
    missing, added = counter_diff(source_values, candidate_values)
    if missing or added:
        add_issue(issues, "exact_value_drift", "Numbers, dates, percentages, or currency values changed.", expected=dict(source_values), actual=dict(candidate_values))

    for label, pattern in (("url", URL_RE), ("email", EMAIL_RE)):
        expected = exact_strings(pattern, source)
        actual = exact_strings(pattern, candidate)
        missing, added = counter_diff(expected, actual)
        if missing or added:
            add_issue(issues, f"{label}_drift", f"{label.upper()} values changed.", expected=dict(expected), actual=dict(actual))

    source_quotes = quoted_strings(source)
    candidate_quotes = quoted_strings(candidate)
    missing, added = counter_diff(source_quotes, candidate_quotes)
    if missing or added:
        add_issue(issues, "quote_drift", "Quoted wording changed or new quoted wording was introduced.", expected=dict(source_quotes), actual=dict(candidate_quotes))

    source_modals = modal_signature(source)
    candidate_modals = modal_signature(candidate)
    if source_modals != candidate_modals:
        add_issue(issues, "modality_drift", "Words that control certainty or obligation changed.", expected=source_modals, actual=candidate_modals)

    source_negative_sentences = polarity_sentences(source)
    candidate_negative_sentences = polarity_sentences(candidate)
    if len(source_negative_sentences) != len(candidate_negative_sentences):
        add_issue(
            issues,
            "polarity_drift",
            "Polarity markers moved. Review the named source and candidate sentences manually.",
            severity="warning",
            expected={"source_sentences": source_negative_sentences},
            actual={"candidate_sentences": candidate_negative_sentences},
        )

    required = set(required_entities) | named_entity_candidates(source)
    missing_entities = sorted(entity for entity in required if entity and entity not in candidate)
    if missing_entities:
        add_issue(issues, "entity_omission", "Named entities from the source are missing.", expected=missing_entities)

    unsupported_biography: list[str] = []
    for pattern in AUTOBIOGRAPHY_PATTERNS:
        source_count = len(pattern.findall(source))
        candidate_matches = [match.group(0) for match in pattern.finditer(candidate)]
        if len(candidate_matches) > source_count:
            unsupported_biography.extend(candidate_matches[source_count:])
    unsupported_biography = sorted(set(unsupported_biography))
    if unsupported_biography:
        add_issue(issues, "unsupported_biography", "The rewrite introduced autobiographical language absent from the source.", actual=unsupported_biography)

    source_shingles = distinctive_shingles(source)
    leaked_phrases: set[str] = set()
    candidate_shingles = distinctive_shingles(candidate)
    for sample in style_samples:
        for shingle in candidate_shingles & distinctive_shingles(sample):
            if shingle not in source_shingles:
                leaked_phrases.add(" ".join(shingle))
    if leaked_phrases:
        add_issue(
            issues,
            "style_sample_leakage",
            "The rewrite reused a distinctive phrase from a style sample that was not in the source draft.",
            actual=sorted(leaked_phrases)[:10],
        )

    critical_issues = [issue for issue in issues if issue["severity"] == "critical"]
    warning_issues = [issue for issue in issues if issue["severity"] == "warning"]
    return {
        "schema_version": "1.1",
        "passed": not critical_issues,
        "critical_issue_count": len(critical_issues),
        "warning_count": len(warning_issues),
        "issues": issues,
        "checks": {
            "exact_values": True,
            "urls": True,
            "emails": True,
            "quotes": True,
            "modality": True,
            "polarity_sentence_warning": True,
            "named_entities": True,
            "autobiographical_additions": True,
            "style_sample_phrase_leakage": True,
        },
        "manual_review_required": [
            "Thesis, causal logic, caveats, and implied meaning still match.",
            "Purpose, audience, requested format, and length still match.",
            "No unsupported factual or personal claim escaped the narrow deterministic checks.",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", required=True, help="Original draft path.")
    parser.add_argument("--candidate", required=True, help="Rewritten candidate path.")
    parser.add_argument("--sample", action="append", default=[], help="Style-sample path. Repeat as needed.")
    parser.add_argument("--required-entity", action="append", default=[], help="Entity that must remain verbatim. Repeat as needed.")
    parser.add_argument("--output", help="Optional JSON report path. Defaults to stdout.")
    args = parser.parse_args()

    try:
        result = verify(
            read_text(args.source),
            read_text(args.candidate),
            style_samples=[read_text(path) for path in args.sample],
            required_entities=args.required_entity,
        )
    except (OSError, UnicodeError, ValueError) as error:
        parser.error(str(error))

    payload = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        target = Path(args.output)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(payload, encoding="utf-8")
    else:
        sys.stdout.write(payload)
    raise SystemExit(0 if result["passed"] else 1)


if __name__ == "__main__":
    main()
