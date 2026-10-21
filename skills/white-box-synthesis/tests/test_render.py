"""Run: python3 tests/test_render.py. Each case mutates the worked example."""
import copy
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from ops import Rejected  # noqa: E402
from render import render  # noqa: E402

BASE = json.loads((ROOT / "tests/fixtures/mill.json").read_text(encoding="utf-8"))
S3 = {"author": "Okafor", "title": "Town Notes", "locator": "p. 9",
      "text": "Incomes fell because the mill had closed."}


def piece(d, n, k=0):
    return d["sentences"][n]["pieces"][k]


def join(d, connective="because", source="S3"):
    """Licensed join: B's link is stated by S3 and realised by its own connective."""
    d["sources"]["S3"] = S3
    d["checks"].append({"source": "S3", "result": "States the cause used for B."})
    d["steps"][1].update(status="stated", licence={"source": "S3", "text": S3["text"]})
    d["steps"][1].update(supports="A", relation="cause")
    d["steps"][0], d["steps"][1] = d["steps"][1], d["steps"][0]
    d["sentences"] = [{"step": ["B", "A"], "pieces": [
        {"source": "S2", "text": "Household incomes in the town fell by a third between 1990 and 1992.",
         "ops": [{"op": "DELETE", "text": "."}]},
        {"source": source, "text": connective, "link": "B"},
        {"source": "S1", "text": "the mill closed in 1990."}]}]


CASES = [
    ("worked example renders", lambda d: None, None),
    ("documented join renders", lambda d: (d.clear(), d.update(json.loads(
        (ROOT / "tests/fixtures/coop.json").read_text(encoding="utf-8")))), None),
    ("splice without connective", lambda d: d["sentences"][1]["pieces"].append(
        {"source": "S1", "text": "after the mill closed in 1990."}), "without a licensed connective"),
    ("licensed join renders", join, None),
    ("connective from another source", lambda d: join(d, "after", "S1"), "licence's source"),
    ("connective outside licence", lambda d: join(d, "sharply", "S3"), "not found"),
    ("tense change refused", lambda d: piece(d, 0)["ops"].append(
        {"op": "INFLECT", "kind": "agreement", "from": "rose", "to": "rise"}), "agreement list"),
    ("number agreement allowed", lambda d: piece(d, 1).update(ops=[
        {"op": "INFLECT", "kind": "agreement", "from": "fell", "to": "fells"}]), None),
    ("punctuation outside list", lambda d: piece(d, 1).update(ops=[
        {"op": "NORMALISE", "rule": "quotes", "result": piece(d, 1)["text"][:-1] + "?"}]), "quote glyphs"),
    ("unknown normalise rule", lambda d: piece(d, 1).update(ops=[
        {"op": "NORMALISE", "rule": "punctuation"}]), "closed list"),
    ("undeclared pair", lambda d: piece(d, 1).update(ops=[
        {"op": "NORMALISE", "rule": "pair", "from": "third", "to": "half"}]), "not declared"),
    ("delete splits a word", lambda d: piece(d, 1).update(ops=[
        {"op": "DELETE", "text": "hold"}]), "splits a word"),
    ("ai link not allowed", lambda d: d["steps"][1].update(status="ai", text="This followed."),
     "not allowed here"),
    ("ai link with a date", lambda d: (d.update(ai_allowed=["B"]), d["steps"].append(
        {"id": "Z", "claim": "c"}), d["steps"][1].update(supports="Z", status="ai",
        text="This began in 1990.")), "figure, date"),
    ("ai link to unstated Z", lambda d: (d.update(ai_allowed="all"), d["steps"][1].update(
        status="ai", text="Over the same years,")), "stated steps only"),
    ("stated Z step renders", lambda d: (d["steps"].pop(), d["sentences"].pop(),
        d["steps"].insert(0, {"id": "Z", "claim": "prices rose"}), d["steps"].pop(),
        d["sentences"][0].update(step="Z")), None),
    ("step off the chain", lambda d: d["steps"][1].update(supports="Q"), "unknown step"),
    ("loop", lambda d: (d["steps"][0].update(supports="B", status="gap", missing="A → B: x"),
                        d["steps"][1].update(supports="A")), "loops"),
    ("missing source check", lambda d: d["checks"].pop(), "contradiction check"),
    ("conflict as an object", lambda d: d.update(conflicts=[{"a": 1}], notes="One note."), "list of sentences"),
    ("sentences out of order", lambda d: d["sentences"].reverse(), "chain order"),
    ("step with no sentence", lambda d: d["sentences"].pop(), "No source sentence"),
    ("copy from AI-authored span", lambda d: (d["sources"]["S2"].update(
        text=d["sources"]["S2"]["text"] + " ⟦AI-AUTHORED: The closure caused it.⟧"),
        piece(d, 1).update(text="The closure caused it.")), "AI-authored or gap marker"),
    ("antecedent from same source", lambda d: (d["sources"]["S2"].update(
        text="Household incomes fell. They fell by a third."), piece(d, 1).update(
        text="They fell by a third.", ops=[{"op": "INFLECT", "kind": "antecedent",
                                           "from": "They", "to": "Household incomes"}])), None),
    ("antecedent from another source", lambda d: (d["sources"]["S2"].update(
        text="They fell by a third."), piece(d, 1).update(text="They fell by a third.", ops=[
        {"op": "INFLECT", "kind": "antecedent", "from": "They", "to": "Prices"}])), "same source"),
    ("end-stop on a question", lambda d: (d["sources"]["S2"].update(
        text="Did incomes fall by a third?"), piece(d, 1).update(text="incomes fall by a third",
        ops=[{"op": "NORMALISE", "rule": "end-stop"}])), "full stop"),
]

failed = 0
for name, mutate, expected in CASES:
    d = copy.deepcopy(BASE)
    mutate(d)
    try:
        render(d)
        outcome = None
    except Rejected as error:
        outcome = str(error)
    ok = outcome is None if expected is None else (outcome is not None and expected in outcome)
    failed += not ok
    print(("PASS" if ok else "FAIL"), name, "" if ok else f"-> {outcome}")
sys.exit(1 if failed else 0)
