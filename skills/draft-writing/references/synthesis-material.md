# Synthesis material

## Purpose

Collect the exact user and source material approved for synthesizing one argument in the synthesis-material file family.

## Procedure

1. Select one approved argument.
2. Propose a limited set of exact user-material IDs, source-excerpt IDs and approved Human argument-draft spans.
3. For each item, show or link the exact span and state its contribution and limits in plain language.
4. Resolve source–user conflicts before approval.
5. Ask whether the user approves this complete input set.
6. Record only the approved set in `synthesis-material/{project}-synthesis-{ARG-nnn}.md` and link it from `{project}-synthesis-material.md`. A changed set requires approval again.

Do not treat an argument's broad research possibilities as an approved synthesis set. Do not synthesize prose in this file.

The root synthesis-material file is a short index only. Never store broad inventories, candidate source lists, completed workflow history, migration reports or archival reconstruction records in this family. Git retains completed history. If uncertain provenance still affects current work, state the minimum actionable warning once beside the affected argument draft; do not preserve the report that discovered it.

After an argument draft is approved, retain its synthesis file only while its exact input or construction record is needed for provenance or revision. Do not duplicate provenance and basis metadata already owned by the argument draft.

## Format

```markdown
# Synthesis material — ARG-001

> **Editing note:** You may edit this file directly. This file contains the exact input set proposed or approved for one argument.

**Status:** Approved for synthesis

### User material

#### U-003 — Short description

> Exact approved span.

**Contribution:** <What it supplies.>

**Limit:** <What it does not establish.>

### Source material

#### A4 — Short description

**Source map:** `sources/source-maps/{project}-source-map-a-author-title.md`, excerpt `A4`

**Contribution:** <What the source establishes.>

**Limit:** <Qualification.>

### Approved argument material

- None.
```

## Completion

The complete limited input set is explicit, Human, conflict-free and approved for one argument.