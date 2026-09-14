# Synthesis material

## Purpose

Select and store the exact user and source material proposed with an argument definition and approved as part of the same package.

## Procedure

1. Select one proposed argument definition.
2. Propose a limited set of exact user-material IDs, source-excerpt IDs and approved Human argument-draft spans with it.
3. For each item, show or link the exact span and state its contribution and limits in plain language.
4. Resolve source–user conflicts before approval.
5. Present the complete input set in the same proposal as the argument definition.
6. Ask once whether the user approves the complete argument-and-basis package.
7. After approval, record the set here and the definition in the arguments file. A change to either part requires approval of the complete revised package.

Do not treat an argument's broad research possibilities as an approved synthesis set. Do not synthesize prose in this file.

Never store broad inventories, candidate source lists, completed workflow history, migration reports or archival reconstruction records in this file. Git retains completed history. If uncertain provenance still affects current work, state the minimum actionable warning once beside the affected argument draft; do not preserve the report that discovered it.

After an argument draft is approved, retain its synthesis record only while its exact input or construction record is needed for provenance or revision. Do not duplicate provenance and basis metadata already owned by the argument draft. Omit empty sections, `None` fields, default statuses and repeated editing notes.

## Format

```markdown
# Synthesis material

> **Editing note:** You may edit this file directly. Each section contains the exact input set proposed or approved for one argument.

Approved for synthesis is the default status. Exceptions are stated locally.

## ARG-001

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

```

## Completion

The complete limited input set is explicit, Human and conflict-free, and was approved in the same package as its argument definition.