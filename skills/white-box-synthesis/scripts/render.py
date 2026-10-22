"""Render a white-box derivation: Synthesis, References, Provenance, Reasoning.

Usage: python3 scripts/render.py derivation.json. Exit 0 prints Markdown, 1 the rejection."""
import json
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from checks import check_argument, check_sources  # noqa: E402
from ops import Rejected, load_sources  # noqa: E402
from pieces import build_sentence  # noqa: E402
from reasoning import reasoning, reference  # noqa: E402


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
        late = (k := min(order.index(i) for i in ids)) < cursor
        if late and not sentence.get("deviation"):
            raise Rejected(f"Sentence {n}: sentences must follow the chain order of steps. "
                           "Fix it, or give the sentence a deviation saying why.")
        cursor = max(cursor, k)
        text, labels, line, used, waived = build_sentence(sentence, steps, sources, pairs)
        waived = ["Sentences must follow the chain order of steps."] * late + waived
        built.append((n, sentence, ids, text, labels, line, used, waived))
        last.update({i: n for i in ids})
    if missing := [i for i in steps if i not in last]:
        raise Rejected(f"No source sentence for {', '.join(missing)}: drop it and mark a gap.")
    paras, prov, refs, spans = [[]], [], [], {}
    for n, sentence, ids, text, labels, line, used, waived in built:
        if sentence.get("paragraph") and paras[-1]:
            paras.append([])
        paras[-1].append(text)
        prov.append(f"{n}. {line}" + (f" · DEVIATION: {sentence['deviation']}" if waived else ""))
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


if __name__ == "__main__":
    try:
        derivation = json.loads(pathlib.Path(sys.argv[1]).read_text(encoding="utf-8"))
        print(render(derivation), end="")
    except (Rejected, KeyError, TypeError, IndexError, json.JSONDecodeError) as error:
        sys.exit(f"Rejected: {error}")
