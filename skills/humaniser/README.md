# Humaniser

Install it in Claude Code 2.1.275 or later with `/plugin install humaniser --marketplace AhmedKishki/agent-skills`; for other agents, see the [collection README](../../README.md#install).

Use this skill to evaluate Markdown prose for generic AI writing patterns, content defects and mechanical faults. It reports findings for review; automatic rewriting is not implemented.

## Typical usage

> Use humaniser to evaluate this README and its related instructions. Report the writing problems with quotations and locations; do not rewrite them.

## What to expect

- Context windows and text counts supplied by the evaluation script.
- Checklist-based judgements, with semantic findings taking priority over surface patterns.
- Wording and order checks: whether each noun can do its verb, passive voice, floating references, removable phrases, plain words, real examples and the order of ideas.
- Ranked findings identifying the location, quotation and failed test.
- Content and provenance faults reported separately from voice findings.

Scores summarise the findings, not the identity of the writer. Protected wording and source passages may be scored, but evaluation does not authorise changing them. The skill stops after reporting.

See [SKILL.md](SKILL.md) for the full workflow.
