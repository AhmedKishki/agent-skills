---
name: humaniser
description: >-
  Find AI writing patterns in markdown and report them against a checklist. Use
  for AGENTS.md, plans, todos, arcs, progress files, supplements, skill files,
  READMEs and any prose a person or an agent reads. The script segments the
  document into context windows, the agent works the 31-item checklist over them,
  and the result is a ranked list of findings for approval. Not for approved
  wording, quotations or source excerpts.
---

# Humaniser

A model writes whatever is most likely to come next, so by default it picks the choice that fits the widest range of readers. A person chooses for one reader and one subject, so their choices are uneven and specific. This skill finds the default choices.

Three things, kept separate on purpose:

| Layer | What it is | Who does it |
|---|---|---|
| **The loop** | `scripts/evaluate.py` segments the document into context windows and counts tokens | the script |
| **The standard** | [references/checklist.md](references/checklist.md) holds 31 concrete tells | the checklist |
| **The judgement** | whether a given window exhibits a given tell | you |

The script never decides what is wrong with a sentence. It supplies the windows; you work the checklist against them. Rewriting the text on the strength of those findings is the next step and is not built yet.

## Files

| File | What it holds |
|---|---|
| [references/checklist.md](references/checklist.md) | The 31 checks, each with what to look for, why it is a tell, and an example. This is the instrument. |
| [references/scoring.md](references/scoring.md) | How to run the script, what its numbers mean, and how to report a result. |
| `scripts/evaluate.py` | Segmentation and counts. No thresholds, no scores, no opinions. |

Read the checklist before judging anything. It is the standard; this file is the procedure.

## Scope

In: `AGENTS.md`, plans, todos, arcs, progress files, supplements, skill files, READMEs, and any prose an agent or a person reads.

Out: approved wording, quotations, source excerpts, and the article's own prose, because rewriting those breaks provenance. Scoring them is allowed; changing them without approval is not. If a document mixes both, say which passages are in scope before starting.

## Part 1 — Evaluate

```bash
python3 scripts/evaluate.py FILE [FILE ...] --out /tmp/evaluate.md
```

The report prints every block, sentence and phrase with the units around it: a phrase with its neighbouring phrases, its sentence and the surrounding sentences and blocks; a sentence with the phrases beside it and its block; a block with the blocks before and after it. A tell is judged in the window it sits in, not from a string in isolation.

Pass several files in one invocation. The repeated 3-gram list is computed across all of them, and it is the only way to see a rule restated in three places.

Then work the checklist in order, strongest first. For each finding give the item number, the location, a quotation, and what the pattern does to the reader.

Read the whole document once before deciding anything. §27 to §31 are document-scale, and a frame repeated across eighty blocks cannot be seen from inside one of them.

Order findings by consequence. A contradiction between two blocks outranks a one-line closer: one is a defect in the content, the other in the surface.

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
