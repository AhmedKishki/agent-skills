# Shared output-file standard

## One owner

| Information or requested artifact | Sole owner or output |
|---|---|
| Thesis, durable vision, operative metatheory | Thesis-and-vision |
| User article content outside the thesis | User-synthesis |
| One source's argument path, excerpts, roles, and qualifications | Its coded source map |
| Theme/keyword retrieval | Index |
| Section/paragraph structure, source contributions, placement, repetition | Article arc |
| Exact non-final article wording selected as raw material | Predraft |
| Current article and authorship metrics | Draft |
| Current draft's changes | Changelog |
| Complete resume working set and resume/migration state | Activity tracker |
| Requested handoff package of the complete tracked working set | Full export |
| Requested verbatim combination of complete source maps and index | Combined sources |

Questions stay in chat; the activity tracker records only the current self-contained resume question or decision, never Q&A history. Store each substantive item once and reference it elsewhere; only predraft, exact draft assembly, combined sources, and the full-export archive deliberately copy canonical material. Every field must add information not already supplied by its filename, header, reference, or inherited provenance. Omit repeated context, labels, explanations, empty sections, unchanged status, and superseded reasoning.

Create only the outputs above, durable sources, and necessary conversions. Never create Q&A, brief, evidence-map, provenance, source-addition, thesis-impact, fidelity-status, migration, or general-note files. Retire a legacy workflow file only after [migration](migration-to-v6.md) validates every governing item elsewhere.

Each replacement is the lean current state, not history. After an authorised replacement validates, omit its disclosed withdrawn wording, rationale, alternatives, and former status. Retain only current useful information and its minimum traceable basis.

## Novelty and removal impact

Before adding or changing canonical content, compare the candidate with every active canonical home it could overlap. Information is repeated when meaning, function, scope, qualification, provenance/authority, and use are already represented; reference its owner instead of saving it again. A distinct source, role, use, qualification, or governing decision is new information even when wording overlaps. Apply the stricter within-source excerpt test in [per-source maps](source-maps.md).

Then identify every active span, row, item, use, dependent, or file that the change would supersede, omit, invalidate, deduplicate, replace, or retire. Before making any such removal, give the user one plain-language removal-impact notice containing:

- the net-new addition or change;
- exactly what would be removed or cease to govern, including routine predecessor-file cleanup;
- why each removal follows and what unaffected work remains; and
- any dependent work that would be reopened, omitted, or retired.

Keep semantic active state unchanged until the user authorises the combined change after seeing that notice. A direct request to remove exact named material authorises only that material; disclose and obtain authority for any additional consequence. Never infer supersession from recency, similarity, or a new addition. If an undisclosed removal appears during validation, stop, preserve the active predecessor, and alert the user again.

Lossless lineage cleanup is the only no-confirmation exception: after prospective notice, a timestamped predecessor or previous tracker may be retired without separate assent when the candidate test proves that no governing content, use, authority, dependency, or unresolved state is lost. The underlying substantive change must already be authorised. A tracker-only replacement may use this exception to record a newly disclosed pause or gap. Any semantic omission, invalidation, or retirement still waits for explicit authority.

Once the disclosed successor and dependents validate, remove the authorised obsolete information rather than retaining history. This protocol governs semantic omissions and physical file deletion; it does not turn request-only combinations or archives into canonical history.

## Change authority

A change is substantive when it alters meaning, thesis/vision, metatheory, source role, arc structure/boundary, passage wording/use, authorship basis, or a dependent's validity. Before it follow [collaborative questions](collaborative-questions.md) and leave canonical content unchanged until the post-alert answer authorises that exact change. Report the resulting direction and reopened work in chat only.

**Faithful routing** is unchanged Human wording placed in its already-established thesis, user-synthesis, source-map, or arc function without changing meaning, role, or use. It excludes new functions, thesis/vision revision, predraft selection, and draft placement. **Authorised cleanup** removes only an exact span or file named in the user's direct removal request or an approved removal-impact notice, plus lossless lineage cleanup under the exception above. Human-preserving operations, faithful routing, and authorised cleanup are non-substantive; cleanup still cannot exceed the disclosed scope.

Work is unaffected only if its thesis basis, meaning, Article/Framework role, boundary, placement/use, provenance, and metatheory fit all remain unchanged. Otherwise omit it from use until decided or revalidated.

## Save and cleanup

Name every created or changed file `{stem}-YYYY-MM-DD-HHMMSS.ext` in the user's timezone, or system timezone if unknown; add `-01`, `-02`, and so on on collision. Keep supplied source names. Never overwrite.

After each authorised change, save and read-check the complete candidate. Compare it with its active predecessor: every governing item must be retained, traceably changed/removed within the disclosed scope, or validated in another canonical home; required fields and dependencies must resolve. If valid, create a tracker listing the candidate and omitting its predecessor, then delete only the predecessor and previous tracker covered by authority or the lossless-cleanup exception. If invalid, keep the predecessor active, list the candidate as a reconciliation input, name the discrepancy in tracker **Now**, omit invalid dependents from active use while retaining any needed for reconciliation, and ask. While a substantive decision is pending, change no canonical content; save a tracker only if **Now** or **Next** changes. Never save a partial or unchanged copy; tracker creation does not recurse.

Creating or delivering a full-export ZIP is the sole save exception: it changes no workflow state, is not tracked, and creates no replacement tracker. Combined sources is tracked normally.

After the required notice and authority, delete an invalidated dependent as soon as its useful material is transferred or revalidated; while needed for reconciliation, keep it in the tracked working set with a non-active role/state and name it in **Now** or **Next**. Apply the same notice to stale combined-sources files, retained full-export ZIPs, retired legacy request artifacts, and unused conversions. Never delete supplied sources or non-workflow inputs, active files, unresolved migration inputs, or sole governing copies. An uploaded legacy workflow file is deletable only after complete migration. Before deleting a tracked file without a replacement, save one tracker that omits it; deletion creates no second tracker. Keep one active version per lineage.

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
| Combined sources | {project}-combined-sources |
| Full export | {project}-full-export |

## Lean header

Every canonical workflow file states **Collaboration: Ask when uncertain; never infer**. Specialised headers retain it. Combined sources preserves each embedded file's complete header; the full-export ZIP adds no document header.

    - **Project:** Project name
    - **Status:** Working | Awaiting approval | Approved | Complete
    - **Depends on:** Exact active filenames
    - **Collaboration:** Ask when uncertain; never infer
    - **Process prose:** AI

Omit optional absent fields. Ordinary files carry no predecessor history; unresolved migration relationships stay in the tracker. **Process prose** covers administrative scaffolding only; apply [provenance](authorship-and-provenance.md) to substantive content. The tracker replaces **Depends on** with resume fields.

**Working** means unresolved work remains. **Awaiting approval** means the complete current file and one named decision are before the user. **Approved** means the user explicitly approved that complete file for its stage. **Complete** means the user declared the final draft and workflow complete. Status never selects predraft or draft use.

Create a conversion only when access or provenance requires it; record its source and retire it through authorised cleanup when unused.
