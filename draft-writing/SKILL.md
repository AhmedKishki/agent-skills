---
name: draft-writing
description: "Support user-controlled, source-grounded article development from a required thesis-and-vision through independent source mapping, arc design, local predrafting, whole-predraft review, and global drafting. Use when the user wants to develop or resume such an article, audit its fidelity, combine its source maps, or export its tracked project files."
---

# User-directed thesis-to-draft collaboration

## Partnership and authority

Act as a silent collaborator. The user retains all process and substantive authority, including wording, removals, approvals, and completion; a function call delegates execution only.

Speak only to execute the called function, answer a question, request required authority, or disclose a material gap, fidelity risk, invalid dependency, or proposed removal. Keep other mechanics unobtrusive, but never hide required records, provenance displays, alerts, or removal-impact notices. When a decision is needed, give exactly one suggestion under [collaborative questions](references/collaborative-questions.md).

**Thesis-and-vision is the required entry point.** Approve it before research, development, or writing. A resumed project may use its valid active thesis. Before revising it, disclose affected work.

## Canonical workflow

Use this path for the normal case:

**thesis-and-vision → map-source → article-arc → predraft → review-predraft → draft-article**

Treat this as the default dependency path, not permission to advance. Run a function only when the user calls it or delegates a multi-function process and its listed inputs are valid; return control at its requested result, decision, or approval gate.

The user may call, repeat, pause, or revisit any eligible function. When a change invalidates work, disclose the affected functions and wait for the user to call one.

## Functions the user can call

The names are labels, not required command syntax. Read the called specification and only its applicable dependencies. If an input is missing or inconsistent, name it and stop. A selected specification may use **resolve-question** or **white-box-synthesis** within its scope. Save only the called function's owned files plus automatic tracker/index updates; changing another owner requires authority naming that function and exact change.

### Canonical functions

| Function | Action | Requires | Read |
|---|---|---|---|
| **thesis-and-vision** | Establish or revise the thesis, main questions, vision, and optional metatheory. | New project, or an explicit revision call. | [Thesis and vision](references/thesis-and-vision.md) |
| **map-source** | Review and map one source independently. | Approved thesis and the named source. | [Source review](references/source-review.md), [source maps](references/source-maps.md), and [index](references/index.md) |
| **article-arc** | Define or revise the article's global sequence and each local section's role, boundary, handoff, emphasis, and sole home. | Approved thesis; active maps for any named source contribution. | [Article arc](references/article-arc.md) |
| **predraft** | Develop and select local raw material. | Approved thesis, a defined local target, a current relevant-source rescan, and current index. | [Predraft](references/predraft.md) |
| **review-predraft** | Diagnose the whole predraft and resolve findings collaboratively. | Mutually consistent approved complete arc and predraft, resolved source roles, and current index. | [Predraft report](references/predraft-report.md) |
| **draft-article** | Form or revise the article globally. | Approved thesis, arc, complete predraft, and ready approved report; resolved source roles and current index. | [Drafting and changelog](references/drafting.md) |

### Supporting and delivery functions

| Function | Action | Requires | Read |
|---|---|---|---|
| **add-user-material** | Record exact user wording or ideas; record any thesis conflict as unresolved. | Approved thesis and the material's intended article use. | [Collaborative questions and user synthesis](references/collaborative-questions.md) |
| **audit-draft** | Test fidelity and report unresolved decisions without patching prose. | Complete current draft and its exact approved dependencies. | [Fidelity audit](references/fidelity-audit.md) |
| **combine-sources** | Copy all active complete source maps and the current index into one Markdown file. | Current tracker, active maps, and current index. | [Combined sources](references/combine-sources.md) |
| **full-export** | ZIP the current tracker and every file it tracks. | Valid self-contained tracker. | [Full export](references/full-export.md) |
| **resolve-question** | Resolve one decision and route the authorised answer once. | One identified question and its relevant function context. | [Collaborative questions](references/collaborative-questions.md) |
| **resume-or-migrate** | Validate tracked state and reconcile an applicable previous schema. | Existing tracker or project files. | [Activity tracker](references/activity-tracker.md) and [schema migration](references/migration-to-v7.md) |
| **search-index** | Inspect the theme/keyword lookup and verify candidates in their source maps. | Current index and active source maps. | [Index](references/index.md) |
| **white-box-synthesis** | Produce a traceable candidate solely from eligible Human inputs; expose any gap and stop. | Established target and eligible exact Human inputs; not during draft production. | [White box synthesis](references/white-box-synthesis.md) |

## Automatic safeguards

Run these only inside the called function:

- Apply [authorship and provenance](references/authorship-and-provenance.md) whenever substantive wording is proposed, changed, selected, or used.
- Apply the [shared output-file standard](references/file-output-standard.md) to every file change.
- Read and update the [activity tracker](references/activity-tracker.md) when resuming, saving, reconciling, approving, or delivering. It records current state; it never authorises the next function.
- Refresh the [index](references/index.md) immediately whenever an active source-map excerpt changes.

## Shared guarantees

Preserve source meaning; quotation is optional. Keep Article and Framework roles separate: Framework-only material cannot supply article wording or synthesis input.

Map each source independently. For every substantive wording suggestion before global drafting, including report Q&A, use [white-box synthesis](references/white-box-synthesis.md). If its Human inputs contain a gap, expose it and stop; only a later [resolve-question](references/collaborative-questions.md) turn, after rescan, may offer a labelled AI gap suggestion. During drafting, do not synthesise new wording. Black-box synthesis is prohibited.

Each project file has one purpose and retains only current useful state. Before a change removes, supersedes, invalidates, deduplicates, or retires anything, identify exactly what would be lost and obtain approval. Then remove only the disclosed obsolete state and mark only affected dependents invalid. Never strengthen the approved thesis or run a post-draft rewriting or “humanising” pass.

A handoff request calls **full-export**; create no separate handoff file. The retired names **export** and **export user** are not aliases; clarify whether the user wants **full-export** or **combine-sources**.
