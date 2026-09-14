# Argument formation

## Purpose

Define the unordered claims the article may need to establish and propose each definition together with its complete limited synthesis basis.

## Argument contents

Each `ARG-nnn` contains:

- one claim;
- essential qualifications only when the claim has them;
- actual dependencies only when the claim has them;
- a status only when it differs from the file's stated default.

Do not store source excerpts, user quotations, synthesized prose or article placement here. File order has no article meaning.

Keep all argument definitions in the canonical file. State each claim once; a concise claim may appear directly in its `ARG-nnn` heading. Do not create indexes and range files merely because repeated boilerplate made the canonical file large.

Keep only claim-specific qualifications with an argument. Put article-wide writing rules in draft direction and structural or passage-level constraints in the article arc. Link to a shared governing rule instead of repeating it across arguments.

## Procedure

1. Form one claim from the approved thesis, user interpretation or a gap exposed by later work.
2. Separate claims that require different evidence or could be accepted independently.
3. Select the complete limited basis under [Synthesis material](synthesis-material.md).
4. Present one package containing the exact ID and claim, any meaningful qualifications or dependencies, and every proposed synthesis input with its contribution and limit.
5. Ask whether the user approves the complete argument-and-basis package or what should change.
6. After approval, save the definition in `{project}-arguments.md` and its basis in `{project}-synthesis-material.md`. Do not ask for a second basis approval.
7. If a changed argument or basis affects an argument draft or article-arc use, mark those dependants for review.

## Format

```markdown
# Arguments

> **Editing note:** You may edit this file directly. Arguments are unordered; moving them does not change article order.

Approved is the default status. Exceptions are stated locally.

## ARG-001 — <One claim.>

**Qualifications:** <Essential claim-specific limit. Omit when none.>

**Depends on:** ARG-002
```

## Completion

The definition and complete limited basis were presented and approved as one package, then saved to their separate owners. Empty and default fields are absent. Prose synthesis is a separate approval stage.