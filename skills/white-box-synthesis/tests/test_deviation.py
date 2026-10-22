"""Run: python3 tests/test_deviation.py. A stated deviation waives a form rule, never copying."""
import copy
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from ops import Rejected  # noqa: E402
from render import render  # noqa: E402

BASE = json.loads((ROOT / "tests/fixtures/mill.json").read_text(encoding="utf-8"))
WHY = "The source's own wording reads better whole."


def sentence(d, n, why=WHY):
    d["sentences"][n]["deviation"] = why
    return d["sentences"][n]


def piece(d, n):
    return d["sentences"][n]["pieces"][0]


CASES = [
    ("a split word waived", lambda d: (sentence(d, 1), piece(d, 1).update(
        ops=[{"op": "DELETE", "text": "hold"}])), None),
    ("a splice waived", lambda d: sentence(d, 1)["pieces"].append(
        {"source": "S1", "text": "after the mill closed in 1990."}), None),
    ("a late sentence waived", lambda d: (d["sentences"].reverse(), sentence(d, 1)), None),
    ("a lowercase start waived", lambda d: (sentence(d, 0), piece(d, 0)["ops"].pop()), None),
    ("a tense change still refused", lambda d: (sentence(d, 0), piece(d, 0)["ops"].append(
        {"op": "INFLECT", "kind": "agreement", "from": "rose", "to": "rise"})), "agreement list"),
    ("an invented span still refused", lambda d: (sentence(d, 1), piece(d, 1).update(
        text="Household incomes in the town rose.", ops=[])), "not found"),
    ("a changed letter still refused", lambda d: (sentence(d, 1), piece(d, 1).update(ops=[
        {"op": "NORMALISE", "rule": "quotes", "result": piece(d, 1)["text"].replace("fell", "felt")}])),
     "punctuation only"),
    ("a deviation without a reason", lambda d: (sentence(d, 1, ""), piece(d, 1).update(
        ops=[{"op": "DELETE", "text": "hold"}])), "deviation saying why"),
]

failed = 0
for name, mutate, expected in CASES:
    d = copy.deepcopy(BASE)
    mutate(d)
    try:
        out, outcome = render(d), None
    except Rejected as error:
        out, outcome = "", str(error)
    ok = outcome is None if expected is None else (outcome is not None and expected in outcome)
    if ok and expected is None:
        ok = f"DEVIATION: {WHY}" in out and f"- Deviations:\n  - Sentence" in out
    failed += not ok
    print(("PASS" if ok else "FAIL"), name, "" if ok else f"-> {outcome}")
sys.exit(1 if failed else 0)
