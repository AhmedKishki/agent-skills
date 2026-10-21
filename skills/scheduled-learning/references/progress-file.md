# Progress file format

One progress file per track, named `progress-<track-slug>.md` (for example `progress-bhaskar-possibility-of-naturalism.md`). It holds the plan, the record of what each finished run covered, and the log of plan changes. The next run depends on it, so keep it exact and plain.

## Template

```markdown
---
track: <track-slug>
plan_status: approved        # draft | approved
status: in-progress          # in-progress | complete
explanation_language: <language chosen at setup>
word_limit: 2000
created: <YYYY-MM-DD>
---

# <Track title>

## Sources
| ID | Source | File (relative to this folder, or full path) | Notes |
|----|--------|----------------------------------------------|-------|
| S1 | <Author, Title> | <file name> | <e.g. leave out index and bibliography> |

## Plan
| Run | Source | Covers | Size (approx.) | Status | Done on |
|-----|--------|--------|----------------|--------|---------|
| 1 | S1 | <exact section titles / page range> | <e.g. ~4,500 words> | pending | |
| 2 | S1 | ... | ... | pending | |

## Coverage log
(One entry per finished run, newest last.)

### Run 1 — <YYYY-MM-DD>
- Covered: <exact location: chapter / section / pages>
- Ends at: <the precise stopping point: the last sentence or paragraph covered, located by page or section, with at most a few words quoted>
- Main claim: <one sentence, as the author states it>
- Concepts introduced: <the author's terms, comma-separated>
- Notes: <anything the next run needs to know, such as a unit left half-covered; leave out if nothing>

## Plan changes
(One entry per change, newest last. Empty until a run changes the plan.)

- Run <N> (<YYYY-MM-DD>): <what changed, for example "'Chapter 2 §3' split: Run 4 covers pp. 40–52, Run 5 covers pp. 52–64; later runs renumbered (old 5→6, old 6→7)">. Reason: <why>.
```

## Updating rules

- **Status values** in the plan table are `pending` or `done`. Fill in "Done on" when a run is finished.
- **Coverage entries** record what the author said, in neutral terms. "Ends at" is what makes a split unit resumable, so be precise about it. "Concepts introduced" is what lets later runs avoid redefining terms.
- **Splitting a unit:** change the run's "Covers" cell to the part actually covered, insert new pending row(s) for the remainder directly after it, renumber the rows below, and add a plan-changes entry listing old and new numbers.
- **Done rows are frozen.** Never renumber or rewrite a row that is `done`.
- **Completion:** when the last row is `done`, set `status: complete` in the frontmatter.
- Keep each cell short. The coverage log carries the detail.
