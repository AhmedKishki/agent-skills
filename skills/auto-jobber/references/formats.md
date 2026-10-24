# Data contracts

Edit initialized JSON records in the private workspace, not the bundled templates. Examples below are shapes to fill from actual sources, not candidate credentials.

## Application research

`research.json` contains `status`, `project_search`, `search_log`, `sources`, `facts`. The Research reference owns status rules. `source` creates each source's `id`, `url`, `title`, `kind`, `published_at`, timezone-bearing `retrieved_at`, relative `file` and `sha256`; preserve these fields and captured text unchanged. Add facts referencing returned IDs:

```json
{"id":"f-project","source_id":"<returned-source-id>",
 "statement":"<claim supported by quote>","quote":"<exact snapshot words>",
 "kind":"project","project_status":"unknown","ongoing":false,
 "status_as_of":null}
```

Fact kinds: `company`, `project`. Statuses: `active`, `announced`, `completed`, `historical`, `unknown`. Use ISO `YYYY-MM-DD` for supported status dates.

## Application plan

`plan.json` uses `schema_version: 1`; fill `job.company`, `job.role`, retain the selected `job.language` (`en`/`de`) and `job.url`. Add requirements and edits:

```json
{"id":"r-one","text":"<posting requirement>","importance":"required",
 "status":"supported","evidence_ids":["ev-summary"]}
```

```json
{"block_id":"summary","before":"<exact decoded baseline text>",
 "after":"<minimal source-supported replacement>","evidence_ids":["ev-summary"],
 "requirement_ids":["r-one"],"reason":"<why this change serves the requirement>"}
```

Requirements use `importance` required/preferred and `status` supported/partial/gap/unknown; supported/partial require verified evidence. `edits: []` is valid. The Tailoring reference owns editing limits. `letter` has ISO `date` (not future), `greeting`, `closing` and `paragraphs`:

```json
{"sentences":[{"kind":"candidate","text":"<supported sentence>",
 "evidence_ids":["ev-summary"],"company_fact_ids":[]}]}
```

Each paragraph has `sentences`; Tailoring defines sentence kinds and support rules. `letter.wording_quotes` is a string list; Voice owns quote-selection rules. `wording` populates `plan.user_input` with `file`, resolved `application`, `sha256`, `source`, `authorship: "user"`, `captured_at`, `language` and `must_include` (string list). Preserve that generated record and snapshot; do not handcraft provenance. Languages describes the optional separate `user_input.translation` record. Keep `review.open_questions` and `review.notes` as lists of unresolved questions and audit notes. These are review metadata, not automatic approval gates.
