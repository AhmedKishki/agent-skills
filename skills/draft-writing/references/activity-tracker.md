# Activity tracker

Maintain `{project}-activity-tracker.md` as the tracked working-set list and resume checkpoint. Read it before resuming, deciding, exporting, or delivering.

List every file needed to resume — accessible source originals, required conversions, one active map per source, one active file per applicable lineage, and every unresolved reconciliation input — plus the current request-only combined-sources file, if any. Use the role/state cell to distinguish active files from request artifacts and non-active inputs retained for reconciliation. Exclude trackers, full-export ZIPs, superseded or unused files, reserves, and history.

Create a tracker after each save and whenever the selected module, state, **Now**, or **Next** changes alone. Name omitted dependents in **Now** or **Next**. Full export is the sole exception: do not change these fields or create a tracker for that delivery-only request.

    # Activity tracker

    - **Workflow:** draft-writing · release: exact Git tag, abbreviated commit, or unversioned copy
    - **Project:** Project name
    - **Focus:** Module selected from the user's request | None—awaiting clarification or direction
    - **State:** Working | Awaiting approval | Approved | Complete
    - **Next source code:** A
    - **Now:** Self-contained current action, blocker, open question, or waiting state · consequence · governing reference
    - **Next:** One action inside the selected module, an awaited user decision, or the user's already-requested next outcome; when complete, **Suggested: next eligible canonical module for current project state—awaiting user direction** · governing reference
    - **Collaboration:** Infer the module from a clear request; ask on ambiguity; never infer substantive content or authority
    - **Process prose:** AI

    | Tracked filename | Role/state |
    |---|---|

Use archive-safe paths relative to the tracker's directory, readable headings, and the next never-used source code. Row order is the read order needed to reconstruct state during resumption, not a recommended drafting sequence. Every file required to continue must have a row; do not mention a needed file only in **Now** or **Next**. The tracker itself is never a row.

Use the exact matching annotated tag only for a clean checkout; otherwise the abbreviated commit, with `-dirty` when applicable. If Git metadata is unavailable, record **unversioned copy**. **Focus** records the module inferred from the user's natural-language request; ask before setting it when materially different modules fit. Artifact readiness and a suggested **Next** never authorise automatic progression. **Now** and **Next** retain only the current open state, with enough exact detail to re-ask an unresolved question or continue after handoff; record no past discussion. Timestamps never establish authority. Apply the [candidate test](file-output-standard.md); on failure keep the predecessor active, list every needed candidate or dependent with an accurate non-active role/state, name the discrepancy in **Now**, and omit invalid material from use.

During local predrafting, **Now** names the sole working unit — the passage or arc paragraph — and rescan state; **Next** names its one next question or action. During predraft-report Q&A, **Now** names the sole open finding, affected raw material, and consequence; **Next** names its one exact suggestion or decision. Global drafting may begin only when the tracked arc, complete predraft, and predraft report are mutually consistent and Approved.

The **combined sources** row names its exact source-map and index reuse basis and becomes stale when any basis changes; retire it through [cleanup](file-output-standard.md) and regenerate only on a new request. A **full export** requires a new request every time and is never a tracker row: the ZIP contains this tracker plus every row, so tracking the ZIP would create recursion.
