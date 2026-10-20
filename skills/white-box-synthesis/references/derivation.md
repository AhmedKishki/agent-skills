# Derivation

- Write the derivation as a JSON file in a scratch location, never inside the skill directory.
- Run `python3 scripts/render.py <file>`. Exit 0 prints the four parts. Exit 1 prints the rejection.
- Fix a rejection in the derivation. If the rule it cites cannot be met, the step or link is a gap.

## Fields

| Field | Content |
|---|---|
| `query` | The query as given |
| `output_context` | Optional. Never rendered and never a source |
| `sources` | Object keyed by label. Each has `text` (exact) and optional `author`, `title`, `locator` and `note` |
| `normalisations` | Optional pairs the user supplied, such as `[{"from": "labor", "to": "labour"}]` |
| `ai_allowed` | Ids of steps whose gap the user allowed an AI link for, or `"all"`. Default `[]` |
| `conclusion` | Z in planning words |
| `steps` | The chain, in order |
| `sentences` | The synthesis, in chain order |
| `excluded` | Left-out sentences or clauses that bear on the query: `source`, `text` (exact) and `reason` (a sentence) |
| `conflicts` | Sentences naming each conflict and its effect on Z |
| `checks` | One `{"source", "result"}` for every supplied source |
| `notes` | Optional strings, such as a tense mismatch with the output context |

## Steps

- `id`: `A`, `B`, … or `Z` for a conclusion that a source states. A `Z` step takes only `id` and `claim`.
- `claim`: planning words for Reasoning.
- `supports`: the id of a later step, or `Z`.
- `relation`: cause, condition, consequence, sequence, contrast, means, example or evidence. Omit it for `part`.
- `status`: `part`, `stated`, `gap` or `ai`.
- `why`: a clause completing "needed because …".
- `licence`, for `stated`: `{"source", "text"}`, the exact span that states the link.
- `missing`, for `gap` and `ai`: `X → Y: what is missing`.
- `text`, for `ai`: the minimal link.

## Sentences

- `step`: the id of the step the sentence realises, or a list when it realises several.
- `paragraph`: optional `true` to start a new paragraph.
- `pieces`, in order. Each piece has `source`, `text` (exact whole words), optional `occurrence` (default 1) and optional `ops`.
- A connective piece adds `"link"`: the id of the step whose stated link it realises.
- `ops` apply in order. Add `occurrence` when the text appears more than once in the piece.
  - `{"op": "DELETE", "text": "…"}`
  - `{"op": "INFLECT", "kind": "agreement", "from": "rises", "to": "rise"}`
  - `{"op": "INFLECT", "kind": "antecedent", "from": "It", "to": "The library"}`
  - `{"op": "NORMALISE", "rule": "case", "to": "upper"}`, or `"to": "lower"`
  - `{"op": "NORMALISE", "rule": "quotes", "result": "…"}`
  - `{"op": "NORMALISE", "rule": "end-stop"}` and `{"op": "NORMALISE", "rule": "semicolon"}`
  - `{"op": "NORMALISE", "rule": "pair", "from": "…", "to": "…"}`

## Example: a licensed join

S1 (Mensah, p. 112) reads "In 2009 the cooperative dissolved and its warehouse was sold." S2 (field notes) reads "The cooperative dissolved because its members left." S2 states the cause between the same words, "the cooperative dissolved", so its connective may join the two.

```json
"steps": [
  {"id": "A", "claim": "members left", "supports": "B", "relation": "cause",
   "status": "stated", "why": "it is the only cause any source gives",
   "licence": {"source": "S2", "text": "The cooperative dissolved because its members left."}},
  {"id": "B", "claim": "the cooperative dissolved in 2009", "supports": "Z",
   "status": "part", "why": "it is the event the query asks about"}
],
"sentences": [
  {"step": ["A", "B"], "pieces": [
    {"source": "S1", "text": "In 2009 the cooperative dissolved and its warehouse was sold.",
     "ops": [{"op": "DELETE", "text": " and its warehouse was sold."}]},
    {"source": "S2", "text": "because", "link": "A"},
    {"source": "S2", "text": "its members left."}]}
]
```

The script renders: "In 2009 the cooperative dissolved because its members left [S1; S2]."

- Had S2 read "The cooperative failed because membership collapsed", the join would fail the licence test. Treating S2's "failed" as S1's "dissolved" would be the agent's identification, so the link would be a gap.
- The complete files are `tests/fixtures/coop.json` and `tests/fixtures/mill.json`.
