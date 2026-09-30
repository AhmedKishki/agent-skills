#!/usr/bin/env python3
"""Segment markdown into paragraphs, sentences and phrases; report each unit with nested context and mechanical facts.

    evaluate.py FILE [FILE ...] [--level all|sentence|phrase|paragraph]
                  [--lines 40-60,120-140] [--out REPORT.md] [--max-chars N]

A "phrase" here is a comma, colon, dash or conjunction delimited span inside one
sentence, which is the span that carries slop. Facts are properties of the text
(word counts, repeats, presence of a digit, path or named source), never verdicts:
the agent applies the guidelines. Verb and support detection are cues and can be
wrong. Skips front matter, fenced code, tables and link definitions; carries the
heading path on every unit.

Standard library only.
"""
from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from pathlib import Path

FENCE = re.compile(r"^\s*(```|~~~)")
HEADING = re.compile(r"^(#{1,6})\s+(.*)$")
TABLE_ROW = re.compile(r"^\s*\|")
LIST_ITEM = re.compile(r"^\s*(?:[-*+]|\d+[.)])\s+")

# Do not split after an abbreviation, an initial, or a lowercase letter.
ABBREV = (r"(?<!\be\.g)(?<!\bi\.e)(?<!\betc)(?<!\bcf)(?<!\bvs)(?<!\bpp)"
          r"(?<!\bno)(?<!\bFig)(?<!\bal)(?<!\bDr)(?<!\bMs)(?<!\bst)")
SENTENCE_END = re.compile(ABBREV + r"(?<=[.!?])[\"')\]]*\s+(?=[A-Z“‘(\[*])")
PHRASE_SPLIT = re.compile(
    r",\s+|\s*;\s+|\s*:\s+|\s+[—–]\s+|\s+[—–]\s*|\s+—\s*"
    r"|\s+(?:and|but|or|which|that|because|while|where|so|yet)\s+")

SUPPORT = re.compile(
    r"\d"                                        # any figure
    r"|`[^`]+`"                                  # code span: path, id, flag
    r"|\[\^\d+\]"                                # footnote marker
    r"|https?://"
    r"|\b[A-Z][a-z]+(?:\s+[A-Z][a-z]+)+\b")     # multi-word proper noun

VERB_CUE = re.compile(
    r"\b(?:is|are|was|were|be|been|being|has|have|had|do|does|did|"
    r"makes?|made|takes?|took|carries|carried|gives?|gave|holds?|held|"
    r"comes?|came|means?|meant|requires?|required|produces?|produced|"
    r"creates?|created|reports?|reported|states?|stated|remains?|"
    r"shows?|showed|records?|recorded|adds?|added|contains?|contained|"
    r"includes?|included|needs?|must|should|would|will|can)\b", re.I)

CONTRAST = re.compile(
    r"\bnot (?:just|only|merely|simply)\b|\brather than\b|\binstead of\b"
    r"|\bnot\b[^.]{0,60}\bbut\b", re.I)

HEDGE = [
    "it is important to note", "it should be noted", "it is worth noting",
    "in order to", "the fact that", "it is clear that", "clearly",
    "obviously", "essentially", "basically", "actually", "simply", "just",
    "arguably", "somewhat", "very", "really", "quite", "typically",
    "generally", "usually", "in many cases", "a range of", "a variety of",
    "various", "numerous", "the way in which", "plays a", "plays an",
    "key", "crucial", "vital", "pivotal", "seamless", "robust",
    "comprehensive", "holistic", "nuanced", "landscape", "realm",
    "testament", "leverage", "utilise", "utilize", "facilitate", "foster",
    "showcase", "underscore", "delve", "multifaceted", "paradigm",
    "in this section", "this section", "let us", "we will", "we now",
    "as discussed", "as noted", "the following", "that said", "in practice",
    "in principle", "to be clear", "as such", "in addition", "furthermore",
    "moreover", "therefore", "thus", "hence", "overall", "ultimately",
]


HEDGE_RE = re.compile(r"(?<!\w)(?:" + "|".join(re.escape(h) for h in HEDGE) + r")(?!\w)", re.I)
LABEL = re.compile(r"^\*\*[^*]{1,40}:\*\*")


def parse(path: Path):
    """Return (heading_path, blocks). Each block is (line_no, text) of prose."""
    text = path.read_text(encoding="utf-8")
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end != -1:
            text = text[end + 5:]
    headings, blocks, current, start = [], [], [], None
    fence = False

    def flush():
        nonlocal current, start
        if current:
            blocks.append((start, " ".join(current).strip()))
        current, start = [], None

    for i, line in enumerate(text.splitlines(), 1):
        if FENCE.match(line):
            flush()
            fence = not fence
            continue
        if fence or TABLE_ROW.match(line) or not line.strip():
            flush()
            continue
        head = HEADING.match(line)
        if head:
            flush()
            level = len(head.group(1))
            headings = headings[:level - 1] + [head.group(2).strip()]
            continue
        if LIST_ITEM.match(line):
            flush()
            start = i
            current.append(LIST_ITEM.sub("", line).strip())
            continue
        if not current:
            start = i
        current.append(line.strip())
    flush()
    return headings, blocks


def sentences(block: str):
    parts = [p.strip() for p in SENTENCE_END.split(block) if p.strip()]
    return [re.sub(r"\s+", " ", p) for p in parts] or [block]


def phrases(sentence: str):
    parts = [p.strip(" ,;:.—–") for p in PHRASE_SPLIT.split(sentence)]
    return [p for p in parts if p]


def words(text: str) -> int:
    return len(text.split())


def hedges(text: str):
    return sorted({m.group(0).lower() for m in HEDGE_RE.finditer(text)})


def repeats(blocks):
    """3-grams appearing in more than one block, with their locations."""
    seen = {}
    for line, text in blocks:
        for n in (text.split() for _ in (0,)):
            for i in range(len(n) - 2):
                g = " ".join(w.lower().strip(".,;:") for w in n[i:i + 3])
                seen.setdefault(g, set()).add(line)
    return {g: sorted(ls) for g, ls in seen.items() if len(ls) > 1}


def clip(text: str, limit: int) -> str:
    return text if not limit or len(text) <= limit else text[:limit] + " …"


def emit(out, tag, ident, text, facts, ctx, limit):
    out.write(f"\n#### {tag} · {ident}\n\n")
    out.write(f"> {clip(text, limit)}\n\n")
    if facts:
        out.write(f"facts: {facts}\n\n")
    for label, value in ctx:
        if value:
            out.write(f"{label}: {clip(value, limit)}\n\n")


def report(paths, level, lines, out, limit):
    blocks = []
    for p in paths:
        for line, text in parse(p)[1]:
            if not lines or any(a <= line <= b for a, b in lines):
                blocks.append((f"{p}:{line}", line, text))
    if not blocks:
        out.write("no prose blocks in range\n")
        return 0

    units = 0
    lens = []
    for ident, _, text in blocks:
        for s in sentences(text):
            lens.append(words(s))
    out.write("# Evaluate report\n\n")
    out.write(f"files: {', '.join(str(p) for p in paths)}\n\n")
    out.write(f"paragraphs {len(blocks)} · sentences {len(lens)} · "
              f"words {sum(lens)} · sentences/para "
              f"{len(lens) / len(blocks):.1f}\n\n")
    if lens:
        over = [n for n in lens if n > 30]
        out.write(f"sentence words: min {min(lens)} median "
                  f"{sorted(lens)[len(lens) // 2]} max {max(lens)} · "
                  f"over 30 words: {len(over)}\n\n")

    rep = repeats([(ln, tx) for _, ln, tx in blocks])
    if rep:
        out.write("## Repeated 3-grams across the range\n\n")
        for g, where in sorted(rep.items(), key=lambda kv: -len(kv[1])):
            out.write(f"- `{g}` — {', '.join(str(w) for w in where)}\n")
        out.write("\n")

    if level in ("all", "paragraph"):
        out.write("## Paragraphs\n")
        for i, (ident, line, text) in enumerate(blocks):
            units += 1
            emit(out, f"P{i:03}", ident, text,
                 f"{words(text)} words · {len(sentences(text))} sentences",
                 [("prev", blocks[i - 1][2] if i else ""),
                  ("next", blocks[i + 1][2] if i + 1 < len(blocks) else "")],
                 limit)

    if level in ("all", "sentence"):
        out.write("\n## Sentences\n")
        for i, (ident, line, text) in enumerate(blocks):
            sents = sentences(text)
            for j, s in enumerate(sents):
                units += 1
                f = [f"{words(s)} words"]
                f.append("verb" if VERB_CUE.search(s) else "no-verb?")
                f.append("support" if SUPPORT.search(s) else "no-support?")
                h = hedges(s)
                if h:
                    f.append("hedge: " + ", ".join(h))
                if CONTRAST.search(s):
                    f.append("contrast")
                emit(out, f"S{i:03}.{j}", f"{ident} ¶{j + 1}", s, " · ".join(f),
                     [("prev phrase", phrases(sents[j - 1])[-1] if j else ""),
                      ("next phrase", phrases(sents[j + 1])[0] if j + 1 < len(sents) else ""),
                      ("prev sentence", sents[j - 1] if j else ""),
                      ("next sentence", sents[j + 1] if j + 1 < len(sents) else ""),
                      ("paragraph", text),
                      ("prev paragraph", blocks[i - 1][2] if i else ""),
                      ("next paragraph", blocks[i + 1][2] if i + 1 < len(blocks) else "")],
                     limit)
    if level in ("all", "phrase"):
        out.write("\n## Phrases\n")
        for i, (ident, line, text) in enumerate(blocks):
            sents = sentences(text)
            for j, s in enumerate(sents):
                ph = phrases(s)
                for k, p in enumerate(ph):
                    units += 1
                    f = [f"{words(p)} words"]
                    h = hedges(p)
                    if h:
                        f.append("hedge: " + ", ".join(h))
                    if CONTRAST.search(p):
                        f.append("contrast")
                    emit(out, f"F{i:03}.{j}.{k}",
                         f"{ident} ¶{j + 1} phrase {k + 1}", p, " · ".join(f),
                         [("prev phrase", ph[k - 1] if k else ""),
                          ("next phrase", ph[k + 1] if k + 1 < len(ph) else ""),
                          ("sentence", s),
                          ("prev sentence", sents[j - 1] if j else ""),
                          ("next sentence", sents[j + 1] if j + 1 < len(sents) else ""),
                          ("paragraph", text),
                          ("prev paragraph", blocks[i - 1][2] if i else ""),
                          ("next paragraph", blocks[i + 1][2] if i + 1 < len(blocks) else "")],
                         limit)
    return units


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("files", nargs="+", type=Path)
    ap.add_argument("--level", default="all",
                    choices=("all", "sentence", "phrase", "paragraph"))
    ap.add_argument("--lines", default="",
                    help="comma separated ranges, e.g. 40-60,120-140")
    ap.add_argument("--out", type=Path, help="report path; default stdout")
    ap.add_argument("--max-chars", type=int, default=0,
                    help="truncate each unit and context field; 0 = no limit")
    args = ap.parse_args(argv)

    missing = [p for p in args.files if not p.is_file()]
    if missing:
        sys.exit("no such file: " + ", ".join(str(p) for p in missing))

    ranges = []
    for part in filter(None, args.lines.split(",")):
        a, _, b = part.partition("-")
        try:
            ranges.append((int(a), int(b or a)))
        except ValueError:
            sys.exit(f"bad --lines range: {part!r}")

    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        with args.out.open("w", encoding="utf-8") as fh:
            n = report(args.files, args.level, ranges, fh, args.max_chars)
    else:
        n = report(args.files, args.level, ranges, sys.stdout, args.max_chars)
    print(f"{n} units", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
