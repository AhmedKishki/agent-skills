---
name: changelog.md
description: Records the enduring user-visible history of the human-writing skill.
---

# Changelog

This is the single enduring changelog for `human-writing`. `SKILL.md` sets the current behaviour; each entry describes the behaviour of its version.

## 1.1.0 — 2026-11-19

- Rules 8 to 13 check the words and the order. The noun must be able to do its verb, otherwise the agent replaces the verb; a metaphor or a verb of movement without a path fails. The agent writes the simplest exact words in the active voice, gives every reference a target the reader can find, cuts every phrase that changes no meaning, and gives concrete claims with examples from the subject, never invented ones. Ideas build in one direction, grouped by kind, then time, then place.
- The justification has a `words` line for rules 8 to 12.
- `references/semantic-tests.md` adds tests for the active voice, the simplest words and removable words; `references/argument-order.md` adds the grouping order.
- The test record moved from the README to `test-record.md`.

## 1.0.0 — 2026-10-21

- Rules 1 to 7, the justification format, and the check and rewrite modes for supplied text.
