# Activity tracker

Maintain `{project}-activity-tracker-YYYY-MM-DD-HHMMSS.md` as the complete tracked working-set list and resume checkpoint. Read it before resuming, deciding, exporting, or delivering.

List every file needed to resume—accessible source originals, required conversions, one active map per source, one active file per applicable lineage, and every unresolved migration or reconciliation input—plus the current request-only combined sources file, if any. Use the role/state cell to distinguish active files from request artifacts and non-active inputs retained for reconciliation. Exclude trackers, full-export ZIPs, superseded or unused files, reserves, and history.

Create a tracker after each save and whenever focus, state, **Now**, or **Next** changes alone. Name omitted dependents in **Now** or **Next**.

    # Activity tracker

    - **Workflow:** draft-writing · schema v7 · release: exact Git tag, abbreviated commit, or unversioned copy
    - **Project:** Project name
    - **Focus:** Thesis and vision | Source review | Article arc | Local predrafting | Predraft report | Global drafting | Fidelity audit
    - **State:** Working | Awaiting approval | Approved | Complete
    - **Next source code:** A
    - **Now:** Self-contained current action, blocker, open question, or waiting state · consequence · governing reference
    - **Next:** One concrete action or awaited user decision, stated so work can resume without chat history · governing reference
    - **Collaboration:** Ask when uncertain; never infer
    - **Process prose:** AI

    | Tracked filename | Role/state |
    |---|---|

Use archive-safe paths relative to the tracker's directory, readable headings, Git-derived release identity, and next never-used source code. Row order is the recommended open/read order for resumption. Every file required to continue must have a row; do not mention a needed file only in **Now** or **Next**. The tracker itself is never a row.

Use the exact matching annotated tag only for a clean checkout; otherwise use the abbreviated commit with `-dirty` when applicable. If Git metadata is unavailable, record **unversioned copy**. The schema label describes project-file compatibility, not the release version. **Now** and **Next** retain only the current open state, with enough exact detail to re-ask an unresolved question or continue after handoff; record no past discussion. Timestamps never establish authority. Apply the [candidate test](file-output-standard.md); on failure keep the predecessor active, list every needed candidate/dependent with an accurate non-active role/state, name the discrepancy in **Now**, and omit invalid material from use.

During local predrafting, **Now** names the sole argument and rescan state; **Next** names its one next question or action. During predraft-report Q&A, **Now** names the sole open finding, affected raw material, and consequence; **Next** names its one exact suggestion/decision. Global drafting may begin only when the tracked arc, complete predraft, and predraft report are mutually consistent and Approved.

The **combined sources** row names its exact source-map and index reuse basis and becomes stale when any basis changes; retire it through [cleanup](file-output-standard.md) and regenerate only on a new request. A **full export** requires a new request every time and is never a tracker row: the ZIP contains this tracker plus every row, so tracking the ZIP would create recursion.

For v6 migration append **migration v6 → v7** to the workflow line and add **Migration remaining:**. For v7 reconciliation append **reconciliation v7** and add **Reconciliation remaining:**. List every exact remaining governing legacy or reconciliation input; use the plain workflow line only when none remains.
