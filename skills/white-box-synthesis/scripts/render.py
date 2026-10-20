"""Render a white-box derivation: Synthesis, References, Provenance, Reasoning.

Usage: python3 scripts/render.py derivation.json. Exit 0 prints Markdown, 1 the rejection."""
import json
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from checks import check_argument, check_sources, coverage  # noqa: E402
from ops import Rejected  # noqa: E402
from pieces import build_sentence, load_sources  # noqa: E402


def link_text(step):
    kind = {"gap": ("GAP", "missing"), "ai": ("AI-AUTHORED", "text")}.get(step.get("status"))
    return f"⟦{kind[0]}: {step[kind[1]]}⟧" if kind else None


def render(d):
    sources = load_sources(d.get("sources"))
    steps = check_argument(d, sources)
    results = check_sources(d, sources)
    order, built, last, cursor = list(steps), [], {}, -1
    pairs = d.get("normalisations", [])
    for n, sentence in enumerate(d.get("sentences") or [], 1):
        ids = sentence.get("step")
        ids = ids if isinstance(ids, list) else [ids]
        if any(i not in steps for i in ids):
            raise Rejected(f"Sentence {n}: unknown step {ids}.")
        if (k := min(order.index(i) for i in ids)) < cursor:
            raise Rejected(f"Sentence {n}: sentences must follow the chain order of steps.")
        cursor = k
        built.append((n, sentence, ids, *build_sentence(sentence, steps, sources, pairs)))
        last.update({i: n for i in ids})
    if missing := [i for i in steps if i not in last]:
        raise Rejected(f"No source sentence for {', '.join(missing)}: drop it and mark a gap.")
    paras, prov, refs, spans = [[]], [], [], {}
    for n, sentence, ids, text, labels, line, used in built:
        if sentence.get("paragraph") and paras[-1]:
            paras.append([])
        paras[-1].append(text)
        prov.append(f"{n}. {line}")
        refs += labels
        for label, span in used:
            spans.setdefault(label, []).append(span)
        for sid in (i for i in steps if last[i] == n and link_text(steps[i])):
            paras[-1].append(mark := link_text(steps[sid]))
            refs += [r for r in sources if re.search(rf"\b{re.escape(r)}\b", mark)]
            kind = steps[sid]["status"].upper()
            prov.append(f"- After {n}: {kind} for {sid} → {steps[sid]['supports']}")
    out = ["**Synthesis**", ""] + [" ".join(p) + "\n" for p in paras]
    out += ["**References**", ""] + [reference(sources[r], r) for r in dict.fromkeys(refs)]
    out += ["", "**Provenance**", ""] + prov
    out += ["", "**Reasoning**", ""] + reasoning(d, steps, sources, results, spans, built)
    return "\n".join(out) + "\n"


def reference(src, label):
    parts = [src.get("author"), src.get("title") and f"*{src['title']}*", src.get("locator")]
    note = f" {src['note']}." if src.get("note") else ""
    return f"- [{label}] " + ", ".join(p or "not supplied" for p in parts) + "." + note


def reasoning(d, steps, sources, results, spans, built):
    lines = [f"- Z: {d['conclusion']}", "- Chain:"]
    for sid, step in steps.items():
        labels = sorted({lb for _, _, ids, _, lbs, _, _ in built if sid in ids for lb in lbs})
        head = f"  - {sid} [{'; '.join(labels)}] {step.get('claim', '')}".rstrip()
        if sid == "Z":
            lines.append(f"{head}. Stated conclusion.")
            continue
        lic = step.get("licence") or {}
        link = {"part": "none needed, part of the answer",
                "gap": "gap, marked in the synthesis",
                "stated": f"stated by {lic.get('source')} in “{lic.get('text')}”",
                "ai": f"AI-authored with permission, for {step.get('missing')}"}[step["status"]]
        lines.append(f"{head} → {step['supports']} ({step.get('relation', 'part')}),"
                     f" needed because {step['why'].rstrip('.')}. Link: {link}")
    n = sum(s.get("status") in ("gap", "ai") for s in steps.values())
    lines.append(f"- Gaps and AI links on the chain: {n}. The sources establish Z only at 0.")
    left = [f"  - {x.get('source')}: “{x.get('text')}”\n    - {x.get('reason')}"
            for x in d.get("excluded", [])]
    lines += ["- Left out:"] + left
    for label, src in sources.items():
        used, total = coverage(src, spans.get(label, []))
        lines.append(f"  - {label}: {used} of {total} sentences copied.")
    lines += ["- Conflicts:"] + ([f"  - {c}" for c in d.get("conflicts", [])] or ["  - None."])
    lines += ["- Source checks:"] + [f"  - {k}: {v}" for k, v in results.items()]
    lines += [f"- Note: {note}" for note in d.get("notes", [])]
    lines.append("- Wording check: passed by scripts/render.py. Meaning checks: best effort.")
    return lines


if __name__ == "__main__":
    try:
        derivation = json.loads(pathlib.Path(sys.argv[1]).read_text(encoding="utf-8"))
        print(render(derivation), end="")
    except (Rejected, KeyError, TypeError, IndexError, json.JSONDecodeError) as error:
        sys.exit(f"Rejected: {error}")
