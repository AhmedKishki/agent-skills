---
name: changelog.md
description: Records the enduring user-visible history of the humaniser skill.
---

# Changelog

This is the single enduring changelog for `humaniser`. `SKILL.md` sets the current behaviour; each entry describes the behaviour of its version. Versions before 4.1.0 have no entries.

## 4.1.0 — 2026-11-19

- Part A asks of every sentence whether its noun can do its verb, and the fix replaces the verb.
- A1f flags floating references: a name, symbol, abbreviation or code identifier whose target the text never gives, such as `dp` in a usage example that never creates it.
- A2 flags every figure of speech, and A3d every passive. A3e flags a verb of movement that leaves "from where?" open, such as "a divider that does not come out whole".
- A8 to A11, in `references/checklist-wording.md`, flag removable words, words plainer ones could replace, claims without a real example, invented examples, and ideas out of order or split apart.
- The checklist is split into three files to stay within the line limit: `references/checklist.md` (A1 to A7), `references/checklist-wording.md` (A8 to A11) and `references/checklist-surface.md` (Parts B and C, what to keep, sources).
- Tested on 38 lines of documentation for a TIMER2 time driver. Version 4.0.0 flagged "a divider that does not come out whole" only as a mild passive and missed the usage example that uses `dp` without creating it. Version 4.1.0 flagged both, the passive "are frozen", the bit names UPS, UPG and UPIF that the text never defines, and "the interrupt adds one", where the interrupt handler does the adding.
