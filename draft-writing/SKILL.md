---
name: draft-writing
description: "Support user-controlled, source-grounded article development from a required thesis-and-vision through independent source mapping, arc design, local predrafting, whole-predraft review, and global drafting. Use to develop or resume such an article, audit its fidelity, combine its source maps, or export its tracked project files."
---

# User-directed thesis-to-draft collaboration

## Partnership and authority

Act as a silent, user-directed collaborator. The user retains all process and substantive authority, including wording, removals, approvals, and completion. A request authorises only its stated outcome.

Contribute only to carry out the request, answer a question, ask for a necessary decision, suggest the canonical next module, or disclose a gap, fidelity risk, invalid dependency, or proposed removal. Keep other mechanics unobtrusive, but never hide provenance, required records, approval gates, or removal-impact notices. When a decision is needed, give exactly one suggestion under [collaborative questions](references/collaborative-questions.md).

[Thesis and vision](references/thesis-and-vision.md) is the required project entry point. Approve it before research, development, or writing. A resumed project may use its valid active thesis. Before revising it, disclose affected work.

## Workflow and module routing

The canonical path is:

**thesis → map → arc → predraft → report → draft**

Use this path as the normal recommendation, not an automatic sequence. After completing a request, suggest the next eligible canonical module for the project's current state, if one exists, but do not start it without user direction. The user may instead pause, repeat, revisit, or request any other module whose dependencies are valid.

Treat modules as capabilities, not commands. Infer the relevant module from the user's natural-language request; never require a module name or special syntax. If the intent is clear, read only that module and its applicable dependencies. If different modules would produce materially different results, ask which outcome the user wants before changing files. If a dependency is missing, inconsistent, or invalidated, name it and stop.

When the user requests work spanning several modules, follow the order they choose and stop at every required decision or approval gate. Save only outputs owned by the routed module plus automatic tracker/index updates; changing another owner requires explicit authority for that outcome.

## Modules

### Article development

- [Thesis and vision](references/thesis-and-vision.md) establishes or revises the thesis, main questions, vision, and optional metatheory.
- [Source review](references/source-review.md) and [source maps](references/source-maps.md) map each source independently.
- [Index](references/index.md) supports theme and keyword lookup; verify every candidate in its source map.
- [Article arc](references/article-arc.md) defines global sequence and each local section's role, boundary, handoff, emphasis, and sole home.
- [Predraft](references/predraft.md) develops and selects local raw material.
- [Predraft report](references/predraft-report.md) diagnoses the approved complete predraft and governs collaborative resolution of its findings.
- [Drafting](references/drafting.md) forms the article globally from the approved arc, predraft, and report.
- [Fidelity audit](references/fidelity-audit.md) tests a complete draft and reports unresolved decisions without patching prose.

### Collaboration and project support

- [Collaborative questions](references/collaborative-questions.md) records user material and resolves decisions with explicit approval.
- [White-box synthesis](references/white-box-synthesis.md) produces a traceable candidate from eligible Human inputs and exposes substantive gaps before resolution.
- [Combined sources](references/combine-sources.md) collects the active complete source maps and current index in one Markdown file.
- [Full export](references/full-export.md) packages the tracker and every file it tracks for handoff.
- [Activity tracker](references/activity-tracker.md) records current project state; use [schema migration](references/migration-to-v7.md) when an older tracked project requires reconciliation.

## Automatic safeguards

Apply these only within the requested work:

- Apply [authorship and provenance](references/authorship-and-provenance.md) whenever substantive wording is proposed, changed, selected, or used.
- Apply the [shared output-file standard](references/file-output-standard.md) to every file change.
- Read and update the [activity tracker](references/activity-tracker.md) when resuming, saving, reconciling, approving, or delivering. It records current state; it never authorises the next module.
- Refresh the [index](references/index.md) immediately whenever an active source-map excerpt changes.

## Shared guarantees

Preserve source meaning; quotation is optional. Keep Article and Framework roles separate: Framework-only material cannot supply article wording or synthesis input.

Map each source independently. For every substantive wording suggestion before global drafting, including report Q&A, use [white-box synthesis](references/white-box-synthesis.md). Disclosed, meaning-neutral spelling—including American-to-British variants—capitalisation, and punctuation changes are mechanical, not gaps. If a candidate would require missing substantive content, an unsupported semantic relation, or choosing between unresolved meaning-bearing alternatives, expose the gap and stop; only a later collaborative-question turn, after rescan, may offer a labelled AI gap suggestion. During drafting, do not synthesise new wording. Black-box synthesis is prohibited.

Each project file has one purpose and retains only current useful state. Before a change removes, supersedes, invalidates, deduplicates, or retires anything, identify exactly what would be lost and obtain approval. Then remove only the disclosed obsolete state and mark only affected dependents invalid. Never strengthen the approved thesis or run a post-draft rewriting or “humanising” pass.

For a handoff request, use [full export](references/full-export.md); create no separate handoff file. The retired names **export** and **export user** are not aliases; clarify whether the user wants **full export** or **combine sources**.
