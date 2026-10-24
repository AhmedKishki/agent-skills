# The applicant owns the letter

## Get this job's words first

Before drafting every letter, check whether the user has already supplied their
own motivation, wording, relevant examples and desired tone for this specific job.
If not, ask for that input and wait. A useful prompt is: “What draws you to this
role, which experience would you mention, and how would you say it in your own
words? What tone and phrases should I keep or avoid?” Do not make the applicant
answer twice when the current-job material is already present in the conversation.

Save the actual reply as a private text file. Use `wording` with its conversation
source to create a hashed, application-bound snapshot and populate `plan.user_input`.
Use repeated `--must-include` options for phrases the user explicitly requires.
Do not label agent-written motivation as user input or reuse another vacancy's
motivation. A raw voice sample from a previous job cannot satisfy this gate.

Choose meaningful exact excerpts of at least three words from the eligible input
(original or approved translation under Languages) for
`letter.wording_quotes`; preserve at least one verbatim in a letter sentence and
preserve every required phrase. Keep the user's meaning, character and phrasing
through the rest of the draft, asking about consequential edits rather than
replacing their motivation with generic corporate filler or invented enthusiasm.
Work from their outline and phrasing before smoothing it. Preserve their register
and degree of directness; do not add fake quirks, sentiment or a stock enthusiasm
paragraph to make the letter sound personal. Show consequential changes for approval.
Whitespace normalization is a code convenience, not permission to rewrite quotes.
`check`/`build` refuse missing, changed or cross-application wording snapshots.

Current-job words can express intent; factual examples still require verified
candidate evidence. Add newly confirmed facts through a reviewed profile update,
not by treating the wording snapshot as automatic qualification evidence.
Company-research outages may limit company claims, but never justify a generic
invented-letter fallback: work from genuine user words or pause.

## Retain voice without inventing character

Keep `tone_preferences`, `character_notes`, `writing_preferences` and `avoid`
based on explicit user statements or confirmed edits. Character notes must be
user-confirmed descriptions, not inferred personality from a CV or writing style.
Use retained samples as voice guidance only; they do not establish new skills,
achievements, employer facts or current-job motivation.

Optional `remember-voice --text-file ... --source ...` retains the genuine raw
sample in profile `voice.samples`. Persistent raw samples are intentional here;
keep them private with accurate provenance. Retain user-approved edits as their
voice only after confirmation; never silently store AI output as user authorship.
This changes the profile and invalidates its seal; follow Onboarding for review.
After an accepted letter, identify any genuine user wording or confirmed phrasing
preferences worth keeping for future letters. Retain those with provenance rather
than claiming silent learning; current-job originals already remain in the application.

After source checks, review the draft with the applicant for factual accuracy,
authentic motivation, tone, required wording and unwanted filler. Code can check
references and literal inclusion; only the applicant can approve their voice.
