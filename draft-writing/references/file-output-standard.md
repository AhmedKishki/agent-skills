# Shared output-file standard

## One owner

| Information | Canonical home |
|---|---|
| Thesis, durable vision, operative metatheory | Thesis-and-vision |
| User article content outside the thesis | User-synthesis |
| One source's argument path, excerpts, roles, and qualifications | Its coded source map |
| Theme/keyword retrieval | Index |
| Section/paragraph structure, source contributions, placement, repetition | Article arc |
| Exact non-final article wording selected as raw material | Predraft |
| Current article and authorship metrics | Draft |
| Current draft's changes | Changelog |
| Active files and resume/migration state | Activity tracker |
| Requested resume snapshot | Hand-off |
| Requested portable source material | Source export |
| Requested portable current project content | User export |

Questions stay in chat except the current unanswered question/suggestion set copied by a requested user export. Store each substantive item once and reference it elsewhere; only predraft, exact draft assembly, source export, and user export deliberately copy canonical material. Every field must add information not already supplied by its filename, header, reference, or inherited provenance. Omit repeated context, labels, explanations, empty sections, unchanged status, and superseded reasoning.

Create only the outputs above, durable sources, and necessary conversions. Never create Q&A, brief, evidence-map, provenance, source-addition, thesis-impact, fidelity-status, migration, or general-note files. Retire a legacy workflow file only after [migration](migration-to-v6.md) validates every governing item elsewhere.

Each replacement is the lean current state, not history. After safely replacing a withdrawn direction, omit its wording, rationale, alternatives, and former status. Retain only current useful information and its minimum traceable basis.

## Change authority

A change is substantive when it alters meaning, thesis/vision, metatheory, source role, arc structure/boundary, passage wording/use, authorship basis, or a dependent's validity. Before it follow [collaborative questions](collaborative-questions.md) and leave canonical content unchanged until the post-alert answer authorises that exact change. Report the resulting direction and reopened work in chat only.

**Faithful routing** is unchanged Human wording placed in its already-established thesis, user-synthesis, source-map, or arc function without changing meaning, role, or use. It excludes new functions, thesis/vision revision, predraft selection, and draft placement. **Already-authorised cleanup** removes only the exact span or file rejected, withdrawn, or replaced by a validated successor. Human-preserving operations, faithful routing, and that cleanup are non-substantive.

Work is unaffected only if its thesis basis, meaning, Article/Framework role, boundary, placement/use, provenance, and metatheory fit all remain unchanged. Otherwise omit it from use until decided or revalidated.

## Save and cleanup

Name every created or changed file `{stem}-YYYY-MM-DD-HHMMSS.ext` in the user's timezone, or system timezone if unknown; add `-01`, `-02`, and so on on collision. Keep supplied source names. Never overwrite.

After each authorised change, save and read-check the complete candidate. Compare it with its active predecessor: every governing item must be retained, traceably changed/removed, or validated in another canonical home; required fields and dependencies must resolve. If valid, create a tracker listing the candidate and omitting its predecessor, then delete the predecessor and previous tracker. If invalid, keep the predecessor active, name the candidate and discrepancy in tracker **Now**, omit dependents, ask, and retain the candidate only until reconciliation. While a substantive decision is pending, change no canonical content; save a tracker only if **Now** or **Next** changes. Never save a partial or unchanged copy; tracker creation does not recurse.

Delete an invalidated dependent as soon as its useful material is transferred or revalidated; while needed for reconciliation, omit it from the active table and name it in **Now** or **Next**. Also delete stale exports/hand-offs and unused conversions. Never delete supplied sources or non-workflow inputs, active files, unresolved migration inputs, or sole governing copies. An uploaded legacy workflow file is deletable only after complete migration. Before deleting a tracked file without a replacement, save one tracker that omits it; deletion creates no second tracker. Keep one active version per lineage.

| Output | Filename stem |
|---|---|
| Thesis and vision | {project}-thesis-and-vision |
| User synthesis | {project}-user-synthesis |
| Source map | {project}-source-map-{code}-{author-short-title} |
| Arc | {project}-article-arc |
| Predraft | {project}-predraft |
| Draft | {project}-draft-vN |
| Changelog | {project}-draft-vN-changelog |
| Activity tracker | {project}-activity-tracker |
| Index | {project}-index |
| Hand-off | {project}-handoff |
| Source export | {project}-export |
| User export | {project}-user-export |

## Lean header

Every workflow file states **Collaboration: Ask when uncertain; never infer**. Specialised headers retain it; exports are reader-facing.

    - **Project:** Project name
    - **Status:** Working | Awaiting approval | Approved | Complete
    - **Depends on:** Exact active filenames
    - **Collaboration:** Ask when uncertain; never infer
    - **Process prose:** AI

Omit optional absent fields. Ordinary files carry no predecessor history; unresolved migration relationships stay in the tracker. **Process prose** covers administrative scaffolding only; apply [provenance](authorship-and-provenance.md) to substantive content. The tracker replaces **Depends on** with resume fields.

**Working** means unresolved work remains. **Awaiting approval** means the complete current file and one named decision are before the user. **Approved** means the user explicitly approved that complete file for its stage. **Complete** means the user declared the final draft and workflow complete. Status never selects predraft or draft use.

Create a conversion only when access or provenance requires it; record its source and delete it when unused.
