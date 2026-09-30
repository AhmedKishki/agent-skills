#!/usr/bin/env python3
"""Segment markdown into paragraphs, sentences and phrases; print each unit with its context window.

    evaluate.py FILE [FILE ...] [--level all|sentence|phrase|paragraph]
                  [--lines 40-60,120-140] [--out REPORT.md] [--max-chars N]

Segmentation only. The script cuts the text into units, counts tokens and
prints the units around each one, so an agent can read a sentence next to its
phrases and its paragraph and decide what the guidelines say about it. It
classifies nothing: no word list, no claim detection, no score, no threshold.
Word counts and repeated 3-grams are arithmetic on tokens, reported because
they are tedious to check by eye, not because they are faults.

Front matter, fenced code, tables and link definitions are skipped. Every unit
carries its file, line and paragraph position.

Standard library only.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

FENCE = re.compile(r"^\s*(```|~~~)")
HEADING = re.compile(r"^(#{1,6})\s+(.*)$")
TABLE_ROW = re.compile(r"^\s*\|")
LIST_ITEM = re.compile(r"^\s*(?:[-*+]|\d+[.)])\s+")
FOOTNOTE = re.compile(r"^\[\^\d+\]:\s")

# Do not split after an abbreviation, an initial, or a lowercase letter.
ABBREV = (r"(?<!\be\.g)(?<!\bi\.e)(?<!\betc)(?<!\bcf)(?<!\bvs)(?<!\bpp)"
          r"(?<!\bno)(?<!\bFig)(?<!\bal)(?<!\bDr)(?<!\bMs)(?<!\bst)")
SENTENCE_END = re.compile(ABBREV + r"(?<=[.!?])[\"')\]]*\s+(?=[A-Z“‘(\[*])"
                         r"|(?<=\])\s+(?=[A-Z“‘])")
PHRASE_SPLIT = re.compile(
    r",\s+|\s*;\s+|\s*:\s+|\s+[—–]\s+|\s+[—–]\s*|\s+—\s*"
    r"|\s+(?:and|but|or|which|that|because|while|where|so|yet)\s+")

# Surface features, counted per 1000 words. Counts only: what they mean is
# the agent's call, and the thresholds live in the skill, not here.
SEMI = re.compile(r";")
DASH = re.compile(r"—")
PAREN = re.compile(r"\([^)]*\)")
QUES = re.compile(r"\?")
CURLY = re.compile(r"[“”]")





def parse(path: Path):
    """Return (heading_path, blocks). Each block is (line_no, text) of prose.

    Line numbers stay true to the file, so skipping front matter must not
    renumber: front matter and fences are dropped by flag, never by slicing.
    """
    blocks, headings, current, start = [], [], [], None
    fence = front = False

    def flush():
        nonlocal current, start
        if current:
            blocks.append((start, " ".join(current).strip()))
        current, start = [], None

    for i, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if i == 1 and line.strip() == "---":
            front = True
            continue
        if front:
            front = line.strip() != "---"
            continue
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
        if FOOTNOTE.match(line):
            flush()
            start = i
            current.append(line.strip())
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


def repeats(blocks):
    """3-grams occurring in more than one block, with their locations."""
    seen = {}
    for line, text in blocks:
        n = text.split()
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
    # A citation is not prose. Footnote entries are listed so a finding can cite
    # one, but they are kept out of every statistic below.
    prose = [b for b in blocks if not FOOTNOTE.match(b[2])]
    notes = [b for b in blocks if FOOTNOTE.match(b[2])]
    lens = [words(s) for _, _, text in prose for s in sentences(text)]
    out.write("# Context report\n\n")
    out.write(f"files: {', '.join(str(p) for p in paths)}\n\n")
    out.write(f"prose blocks {len(prose)} · sentences {len(lens)} · words "
              f"{sum(lens)} · sentences/block "
              f"{len(lens) / len(prose) if prose else 0:.1f}"
              + (f" · footnote entries excluded {len(notes)}\n\n" if notes else "\n\n"))
    if lens:
        mean = sum(lens) / len(lens)
        var = (sum((n - mean) ** 2 for n in lens) / len(lens)) ** 0.5
        out.write(f"sentence words: min {min(lens)} · median "
                  f"{sorted(lens)[len(lens) // 2]} · max {max(lens)} · "
                  f"mean {mean:.1f} · sd {var:.1f} · cv {var / mean:.2f}\n\n")

    body = " ".join(t for _, _, t in prose)
    labels = sum(1 for _, _, t in prose if re.match(r"\*\*[^*]{1,60}[:.]\*\*", t))
    nw = len(body.split()) or 1
    out.write("surface counts per 1000 words: "
              + " · ".join(
                  f"{name} {len(rx.findall(body)) / nw * 1000:.1f}"
                  for name, rx in (("semicolons", SEMI), ("em-dashes", DASH),
                                   ("parentheses", PAREN), ("questions", QUES)))
              + f"\nbold label openings: {labels} of {len(prose)} prose blocks · "
              + f"curly quotes: {len(CURLY.findall(body))}\n\n")

    rep = repeats([(ln, tx) for _, ln, tx in blocks])
    if rep:
        out.write("## 3-grams occurring in more than one block\n\n")
        for g, where in sorted(rep.items(), key=lambda kv: -len(kv[1])):
            out.write(f"- `{g}` — lines {', '.join(str(w) for w in where)}\n")
        out.write("\n")

    if level in ("all", "paragraph"):
        out.write("## Blocks\n")
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
                emit(out, f"S{i:03}.{j}", f"{ident} sentence {j + 1}", s,
                     f"{words(s)} words",
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
                    emit(out, f"F{i:03}.{j}.{k}",
                         f"{ident} sentence {j + 1} phrase {k + 1}", p,
                         f"{words(p)} words",
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
