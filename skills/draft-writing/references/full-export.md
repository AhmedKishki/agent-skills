# Requested full export

Create `{project}-full-export.zip` only when the user explicitly requests a **full export** or a handoff package. Never infer the request from a pause, approval milestone, or conversation change.

The ZIP is the sole handoff output. It is a byte-preserving transport package, not a canonical file, drafting input, approval, history, or tracker row. Create no separate hand-off document, manifest, summary, or transformed copy.

## Archive set

Read and validate the sole current [activity tracker](activity-tracker.md). Its **Now** and **Next** must be self-contained enough to resume without chat history. Include exactly:

1. the current activity tracker itself; and
2. every file in its **Tracked filename** table, once, in table order.

Preserve each relative path and file's extracted bytes. Include active canonical files, source originals, conversions, current combined sources, and non-active reconciliation inputs when they have tracker rows. Add no untracked file, prior tracker, superseded/history file, or full-export ZIP.

Every tracked path must be relative to the tracker's directory and archive-safe. Stop without creating a partial ZIP if the tracker is stale or ambiguous, a row is duplicated, a file is missing/unreadable/not a regular file, a path is absolute or escapes the tracker directory, or the output would collide with an input.

## Build and verify

Use the stable output name. Run the bundled [build_full_export.py](../scripts/build_full_export.py) with the exact tracker and output paths; if Python is unavailable, use an equivalent ZIP implementation that enforces every rule above.

Before delivery, verify that the archive member set is exactly the tracker plus its rows, every member path is safe and unique, and every archived file matches its input byte-for-byte. On any mismatch, delete only the invalid new archive and report the discrepancy; change no canonical file or tracker state.

Deliver the ZIP without adding it to the tracker or creating a new tracker. A later full export always requires a new request. Any locally retained earlier ZIP is a stale delivery artifact after project state changes and may be retired only under the shared removal-impact rules.
