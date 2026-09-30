---
name: humaniser
description: >-
  Find AI writing patterns in markdown and report them against a checklist. Use
  for AGENTS.md, plans, todos, arcs, progress files, supplements, skill files,
  READMEs and any prose a person or an agent reads. The script segments the
  document into context windows, the agent works a semantic-first checklist over
  them, and the result is a ranked list of findings for approval. Not for
  approved wording, quotations or source excerpts.
---

# Humaniser

A model writes whatever is most likely to come next, so by default it picks the choice that fits the widest range of readers. A person chooses for one reader and one subject, so their choices are uneven and specific. This skill finds the default choices.

Three things, kept separate on purpose:

| Layer | What it is | Who does it |
|---|---|---|
| **The loop** | `scripts/evaluate.py` segments the document into context windows and counts tokens | the script |
| **The standard** | [references/checklist.md](references/checklist.md) holds the semantic checks, the surface checks and the mechanical faults | the checklist |
| **The judgement** | whether a given sentence says anything | you |

The script never decides what is wrong with a sentence. It supplies the windows; you work the checklist against them. Rewriting the text on the strength of those findings is the next step and is not built yet.

## Files

| File | What it holds |
|---|---|
| [references/checklist.md](references/checklist.md) | Part A semantic checks, Part B surface checks, Part C mechanical and provenance faults, and what to keep. This is the instrument. |
| [references/scoring.md](references/scoring.md) | How to run the script, what its numbers mean, and how to report a result. |
| `scripts/evaluate.py` | Segmentation and counts. No thresholds, no scores, no opinions. |

Read the checklist before judging anything. It is the standard; this file is the procedure.

## Scope

In: `AGENTS.md`, plans, todos, arcs, progress files, supplements, skill files, READMEs, and any prose an agent or a person reads.

Out: approved wording, quotations, source excerpts, and the article's own prose, because rewriting those breaks provenance. Scoring them is allowed; changing them without approval is not. If a document mixes both, say which passages are in scope before starting.

## Part 1 — Evaluate

Read the document once before running the script, so the first reading is not the report's.

```bash
python3 scripts/evaluate.py FILE [FILE ...] --out /tmp/evaluate.md
```

The report gives every block, sentence and phrase with the units around it. A judgement is made in the window a sentence sits in, not from a string in isolation.

Work Part A on the `## Sentences` section. These are the checks that decide: the sentence either says something or it does not, and the surface cannot settle it. Pass every related file in one invocation, because the 3-gram list is computed across all of them and it is the only way to see a rule restated in three places.

Work Part B on the blocks and the 3-grams. These cannot decide anything alone. A generated passage passes all of them. They matter when a semantic check has already found the sentence thin.

Work Part C on one whole read. These are the mechanical and provenance faults, they are not voice, and they must not be folded into a voice figure. They concentrate in edited files, which is why a working draft carries more of them than a generated one.

For each finding give the item number, the location, a quotation, and the test it failed. Order by consequence: a wrong figure outranks a tell, because one is a defect in the content and the other in the surface.


## Part 2 — Humanise

Not built yet. When it is, it takes the findings from Part 1 and produces a table of replacements for approval — location, before, after, item number — and applies only what the user approves. A diagnosis, a report, or silence is never approval. It will never change a claim, an instruction, a path, an identifier, a scope or a date without asking.

Until then, report findings and stop. A finding is a proposal about wording, not a change to wording.

## Reporting

Give the pattern score as a summary of the item-by-item verdicts, never as a measurement of the writer, and never as a bare figure without the findings behind it. Where an item is a judgement call, say so and give the reason. Report the script's counts as facts about the text and say what they show.

Describe the writing problems as writing problems. Never claim or imply who wrote a passage.

## What survives the pass

A checklist that removes every tell also removes the writer. Keep:

- a specific, unusual detail: a real address, an odd quote, a named person with a role
- mixed feelings and unresolved tension
- dated, era-bound references: slang, memes, in-jokes that map to a year
- a first-person choice the writer can explain
- a genuine aside, parenthetical or self-correction

First person is not evidence of a human writer. A document can be written in the author's first person as a device, and the rate says nothing about who held the pen.
