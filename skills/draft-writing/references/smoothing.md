---
name: smoothing.md
description: Defines post-synthesis smoothing without contaminating Human synthesis lineage.
---

# Smoothing

## Accepts

An approved Human-only white-box output, its complete lineage, the current plan unit and a specific smoothing need.

Do not accept unapproved synthesis, unresolved substantive gaps, unsupported claims or AI-authored material as Human input.

## Owns

Smoothing is a post-synthesis operation, not a new canonical output. Human-only smoothing may revise material through white-box operations. User-requested AI smoothing may produce draft wording only.

## Procedure

1. Identify the exact approved Human synthesis and the precise problem in flow, grammar, rhythm, repetition or readability.
2. First attempt smoothing through `COPY`, `INFLECT`, `NORMALISE`, `ORDER` and `DELETE`. If these operations suffice, present a revised Human-only white-box output with its operation record.
3. If they do not suffice, state the smallest exact wording or relation gap and ask the user to supply it. Do not originate or volunteer AI wording.
4. State that the user may explicitly request AI smoothing as a separate option. Continue only after that explicit request.
5. When AI smoothing is requested, preserve every claim, modality, qualification and authorised relation; add no new evidence, interpretation, argument or structural connection.
6. Mark every exact AI-authored span inline as `⟦AI-AUTHORED: exact wording⟧` and obtain approval of that exact proposal.
7. Save approved AI-smoothed wording only in `{project}-draft.md` with permanent AI or Mixed provenance recoverable from progress. Never save it in material or use it as a white-box input.
8. If smoothing exposes a substantive problem, return to the relevant owner instead of smoothing over it.

## Completion

The approved Human synthesis remains recoverable, every smoothing change has accurate provenance, AI wording appears only by explicit request and only in the draft, and no AI or Mixed material enters white-box synthesis.