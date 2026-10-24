# Retained profile and intake formats

Examples describe data shapes, not a fictional candidate. Edit private workspace
records, not assets. `qualifications.json` uses `schema_version: 1`, `person`,
`qualifications`, `interests`, `voice`, `last_reviewed_at`, `evidence`,
`editable_blocks` and `policy`; initialized assets supply empty lists and defaults.
`person` has `name`, `email`, `phone`, `location`; intake also uses optional `headline`.

## Normalized intake

`intake --data` accepts a JSON object with `person`, `qualifications`, optional
`summary`, `interests` (strings), `voice` and `document_language` (see Languages).
Use all eight qualification arrays:
`study`, `work`, `experience`, `certificates`, `expertise`, `languages`, `projects`,
`online_presence`. Every entry has a category-unique `id`, nonempty `title`,
`source` locator and `details` (string list):

```json
{"id":"project-one","title":"<actual project title>",
 "source":"/private/old-cv.txt#projects","details":["<source-backed detail>"]}
```

Optional entry fields are `organisation`, `location`, `start`, `end`, `updated_at`,
`level`, `url`. Use source-supported strings, ISO date/month/year where known;
leave missing values absent rather than guessing. Additional imported fields
remain in source/retained records; rendering uses supported fields only.
The converter also handles project `description` and education `gpa`.
Intake merges work/experience into CV experience, study into education, expertise
into skills, and adds certificates, languages and online presence sections.
Check that retained metadata and rendered facts agree; not all metadata is shown.

## Voice and review metadata

`voice` has list fields `tone_preferences`, `character_notes`, `writing_preferences`,
`avoid` (strings) and `samples` (objects). Each sample has `id`, raw `text`,
`source`, `authorship: "user"` and `recorded_at`. Use `remember-voice` to append it.
The Voice reference owns authorship/consent rules. `last_reviewed_at` begins null;
Freshness defines the confirmation process that writes it.

## Evidence and editable blocks

Import paths create evidence with `verified: false`, including entry metadata;
intake adds category entries and interests as additional evidence. Preserve IDs
and audit both converted and original-entry evidence before using them.

```json
{"id":"ev-summary","text":"<source-backed fact>",
 "source":"/private/old-cv.txt#profile","verified":false}
```

`editable_blocks` maps IDs to a `kind` (`summary`, `bullet`, `skills`) and support:

```json
{"summary":{"kind":"summary","evidence_ids":["ev-summary"]}}
```

Its matching HTML is `<!-- cv:summary -->escaped text<!-- /cv:summary -->`.
Marker IDs start with a lowercase letter and use lowercase letters/digits/hyphens.
Markers pair uniquely and exactly match registered IDs. Tailoring owns edit rules.
`policy` supplies edit/page/research budgets; use its initialized defaults unless
the user explicitly approves a baseline-policy change.

## Alternative upstream input

`bootstrap` accepts pinned awesome-cv-html `resume-data.json`, not JSON Resume.
`about-me` string keys: `first-name`, `last-name`, `position`, `location`, `email`,
`mobile-display`, `description`, `github`, `website`; a name is required.
Each optional array below contains objects with these fields and `list-items`
(a list of strings). GPA also accepts a number.

| Array | Fields |
|---|---|
| `experience` | `institution`, `title`, `location`, `date-range` |
| `education` | `institution`, `study`, `location`, `date-range`, `gpa` |
| `projects` | `title`, `description`, `url`, `date-range` |
| `extracurricular` | `role`, `organization`, `location`, `date-range` |
| `skills` | `heading` |

Unknown upstream fields stay in `candidate-source.json` but may not render.
