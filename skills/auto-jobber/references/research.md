# Employer and project research

## Research with live agent tools

Resolve the employer's identity, official domain, relevant business/unit and role
location from the posting and official pages. Check namesakes and subsidiaries
before attributing a claim. Search the official project/product pages, newsroom,
engineering posts and dated announcements relevant to the vacancy.
Use reputable secondary reporting when primary material is missing or inaccessible;
identify it as secondary rather than presenting it as official confirmation.

Record queries, URLs checked, access failures and unresolved identity/status issues
in `search_log`. The CLI captures sources but does not browse intelligently,
research projects or judge whether a statement follows from a quotation.

## Capture and classify evidence

Use `source` to save parsed page text and metadata into `research.json`. For pages
the fetcher cannot read, use agent browsing to save faithful extracted text outside
the skill, then capture it with `--text-file` and the original URL/title.
Do not substitute an agent-written summary for the source snapshot.
Check each saved snapshot against the page before quoting it.

Create facts from exact quotations present in those snapshots. Keep a concise
`statement` separate from the `quote`; audit that the statement entails no stronger
claim. Use the source ID returned by `source`, not a fabricated ID or guessed hash.
Populate publication dates only when the source establishes them.

To mark a project `ongoing: true`, require a primary source explicitly establishing
active status, `kind: project`, `project_status: active` and a supported
`status_as_of` within the policy window (default 180 days). Retrieval today is not
evidence that an old project is still active. An announcement alone does not prove
ongoing work; distinguish announced, completed, historical and unknown status.
Where current status cannot be established, use `ongoing: false` and qualified
wording, or omit the project from the letter.

## Finish honestly

- `complete`: sources and relevant facts are captured and checked.
- `limited`: some research is usable, but coverage or current status is uncertain.
- `unavailable`: meaningful evidence could not be obtained; do not invent facts.

Set `project_search` to `found`, `not_found` or `unavailable` based on actual work.
Both fallback statuses require a nonempty search log. `pending` fails validation.
Explain limitations to the user; a supported candidate/intent-focused letter is
preferable to fabricated company knowledge. Keep employer facts in research and
candidate facts in qualifications, even when their wording overlaps.

For candidate public presence, inspect user-provided public portfolio/GitHub URLs
to corroborate specific work and discuss additions with the applicant. Do not
upload the CV or private profile, search private data, or infer ownership/skills
from an unrelated account. Route confirmed additions through baseline review.
