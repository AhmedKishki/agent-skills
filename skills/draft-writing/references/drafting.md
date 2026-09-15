---
name: drafting.md
description: Defines composition and verification of reader-facing article prose.
---

# Drafting

## Accepts

The current thesis, an approved unit of the plan, its assigned arguments and material, relevant user material and source maps, and direct user prose or revisions.

Do not accept unsupported claims, unapproved structural invention, undisclosed AI wording, superseded plans or unresolved contradictions affecting the unit.

## Owns

`{project}-draft.md` owns current reader-facing article prose. Arguments own claims and bases, material owns synthesized passages, and the plan owns structure.

## Procedure

1. Work from the current plan, one complete user-approved unit at a time.
2. Present the unit's purpose, assigned arguments, synthesized material and unresolved needs before composing.
3. Use white-box-synthesis where its Human inputs suffice. Relevant user material must be included unless the user explicitly authorises exclusion.
4. Ask the user for missing wording or connections before offering AI material.
5. Mark every AI-authored span inline in the proposal as `⟦AI-AUTHORED: exact wording⟧`, including every connector, transition, join, framing phrase and conclusion. Apply it only after explicit approval of that exact span and never label it Human or white-box synthesis. A general disclosure elsewhere is insufficient; the user must never be expected to detect AI material.
6. Save approved prose in the live draft and update progress.
7. If drafting exposes a thesis, argument, basis, material or structural problem, return to its owner and revise only affected dependants.
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

The draft contains only reader-facing prose. Keep current working questions in progress, claim and basis records in arguments, and synthesized passages in material. The exact section structure and prose remain flexible under the approved plan.

## Citation verification

Identify each support-dependent claim and reopen its source. Check identity, locator, date, scope, modality and qualification. Propose footnotes or other citations in the style set by the thesis. If support fails, report the defect and return to arguments; do not silently qualify prose. Create a separate citation work file only when the user requests it or the scale of unresolved citation work gives it a distinct current purpose.

## Completion

Every unit is approved, the prose conforms to the current thesis and plan, support-dependent claims are verified, no prose was added during assembly, and the user approves the current complete article.
