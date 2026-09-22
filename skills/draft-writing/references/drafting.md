---
name: drafting.md
description: Defines composition and verification of reader-facing article prose.
---

# Drafting

## Accepts

The current thesis, an approved unit of the plan, its assigned eligible arguments and material, relevant user material and source maps, direct user prose or revisions, and any separately approved user-requested AI smoothing for this draft unit.

Do not accept unsupported claims, unapproved structural invention, unsolicited or undisclosed AI wording, explicitly AI-authored or AI-marked spans presented as synthesis, superseded plans or unresolved contradictions affecting the unit. Approved Mixed synthesis is eligible unless the user excludes it and must retain Mixed provenance.

## Owns

`draft-section-n.md` owns one section’s reader-facing prose and `{project}-draft.md` owns the combined article once the user asks for it. Arguments own claims and bases, material owns synthesized passages, and the plan owns structure.

## Procedure

1. Work from the current plan, one complete user-approved section at a time, composing it into its own `draft-section-n.md`. Each section is gated by the user’s approval before the next is drafted, though the user may instead review sections at any later point, and each section carries its own review content.
2. Present the unit's purpose, assigned arguments, eligible synthesized material, its provenance and unresolved needs before composing.
3. Assemble or revise prose through white-box synthesis first. Relevant user material must be included unless the user explicitly authorises exclusion.
4. Apply the post-synthesis smoothing procedure. Do not originate or volunteer AI wording; when provenance-preserving operations cannot fill a gap, specify it and ask the user to supply it.
5. Produce AI smoothing only after the user explicitly requests it. Mark every exact AI-authored span inline as `⟦AI-AUTHORED: exact wording⟧`, obtain exact approval and keep its provenance permanently AI or Mixed. Never move the marked span into material or use it in white-box synthesis.
6. Save approved prose in the live draft and update progress with any AI-smoothed span whose provenance must remain recoverable.
7. If drafting exposes a thesis, argument, basis, material or structural problem, return to its owner and revise only affected dependants.
8. Assemble the approved sections into `{project}-draft.md` only on the user’s request, without adding prose, then verify citations against accessible originals and the user’s citation requirements. Smoothing, consolidation and citation-checking are performed per section and are user-mediated.

## Standard structure

```markdown
---
name: "draft-section-n.md"
description: Holds one section’s reader-facing prose.
---

# <Article title or working title>

<Reader-facing article prose in the current plan order.>
```

The draft contains only reader-facing prose. Keep current working questions in progress, claim and basis records in arguments, and synthesized passages in material. The exact section structure and prose remain flexible under the approved plan.

## Citation verification

Identify each support-dependent claim and reopen its source. Check identity, locator, date, scope, modality and qualification. Propose footnotes or other citations in the style set by the thesis. If support fails, report the defect and return to arguments; do not silently qualify prose. Create a separate citation work file only when the user requests it or the scale of unresolved citation work gives it a distinct current purpose.

## Completion

Every unit is approved, the prose conforms to the current thesis and plan, support-dependent claims are verified, no prose was added during assembly, and the user approves the current complete article.
