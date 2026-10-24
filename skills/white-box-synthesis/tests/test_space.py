"""Run: python3 tests/test_space.py. NORMALISE space repairs words an extraction ran together."""
import copy
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from ops import Rejected  # noqa: E402
from render import render  # noqa: E402

BASE = json.loads((ROOT / "tests/fixtures/mill.json").read_text(encoding="utf-8"))
MERGED = "Household incomesin the town fell by a third between 1990 and 1992."


def merged(spaced):
    d = copy.deepcopy(BASE)
    d["sources"]["S2"]["text"] = MERGED
    d["sentences"][1]["pieces"][0].update(text=MERGED, ops=[
        {"op": "NORMALISE", "rule": "space", "from": "incomesin", "to": spaced}])
    return d


out = render(merged("incomes in"))
assert "Household incomes in the town" in out, out
assert 'NORMALISE space "incomesin" → "incomes in"' in out, out
for spaced in ("incomes on", "incomes  in", "incomesin"):
    try:
        render(merged(spaced))
    except Rejected as error:
        assert "only insert spaces" in str(error), error
    else:
        sys.exit(f"FAIL {spaced!r} rendered")
print("PASS merged word spaced and recorded; a changed letter, a double space and no change refused")
