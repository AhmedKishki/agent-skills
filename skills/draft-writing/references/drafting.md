---
name: drafting.md
description: Defines composition and verification of reader-facing article prose.
---

# Drafting

## Accepts

The current user thesis, an approved unit of the plan, its assigned material, relevant user material and source maps, and direct user prose or revisions.

Do not accept unsupported claims, unapproved structural invention, undisclosed AI wording, superseded plans or unresolved contradictions affecting the unit.

## Owns

`{project}-draft.md` owns current reader-facing article prose. Material remains the owner of underlying claims, bases and developing synthesis; the plan remains the owner of structure.

## Procedure

1. Work from the current plan, one complete user-approved unit at a time.
2. Present the unit's purpose, assigned material and unresolved needs before composing.
3. Use white-box-synthesis where its Human inputs suffice. Relevant user material must be included unless the user explicitly authorises exclusion.
4. Ask the user for missing wording or connections before offering AI material.
5. Apply AI-authored wording or relations only after approval of the exact bounded proposal and never label them Human or white-box synthesis.
6. Save approved prose in the live draft and update progress.
7. If drafting exposes a thesis, argument, evidence or structural problem, return to its owner and revise only affected dependants.
8. Assemble approved units without adding prose, then verify citations against accessible originals and the user's citation requirements.

## Standard structure

```markdown
---
name: "{project}-draft.md"
description: Holds the current reader-facing article prose.
---

# <Article title or working title>

<Reader-facing article prose in the current plan order.>
```

The draft contains only reader-facing prose. Keep current working questions in progress and underlying records in material. The exact section structure and prose remain flexible under the approved plan.

## Citation verification

Identify each support-dependent claim and reopen its source. Check identity, locator, date, scope, modality and qualification. Propose footnotes or other citations in the style set by the user thesis. If support fails, report the defect and return to material; do not silently qualify prose. Create a separate citation work file only when the user requests it or the scale of unresolved citation work gives it a distinct current purpose.

## Completion

Every unit is approved, the prose conforms to the current user thesis and plan, support-dependent claims are verified, no prose was added during assembly, and the user approves the current complete article.
