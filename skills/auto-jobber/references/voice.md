# The applicant owns the letter

## What a cover letter must achieve

Treat a cover letter as a motivation letter: it makes a personal case for this applicant in this job. Accurate qualifications alone are insufficient. Every complete letter must answer three questions:

1. **Why is this job interesting to the applicant?** Identify the actual work, problem or possibility that draws them to this opportunity, using their own reasons rather than generic praise of the employer.
2. **What is their personal connection to the field?** Connect the opportunity to a genuine interest, passion, feeling, opinion, personal project, experience or question they want to pursue. A practical reason is valid; do not demand a dramatic story or private disclosure.
3. **Why are they a good fit, and what will they bring?** Show how selected parts of their background and experience prepare them for specific work in this role. Explain the contribution they could make, distinguishing demonstrated capability from an area they intend to develop.

These are outcomes for one connected argument, not mandatory headings or three formulaic paragraphs. Use an order that makes the applicant's interest, personal connection and evidence of fit build on one another.

## Treat the job offer as authoritative

The offer defines the job. Whenever the letter refers to the position, its aims, tasks or requirements, use the offer's own terms and attribute to it only what it states. Do not paraphrase it into the applicant's framing, give it aims or emphases it does not have, or drop a qualifier it sets, such as the domain an aim applies to.

The applicant's interpretation stays theirs. Describe their experience and motives in their own terms, and connect them to the offer only where the two genuinely meet. Do not apply an offer term to experience it does not describe, because that redefines the term. Where the applicant's background does not reach part of the offer, name that part as new to them or leave it out.

Keep the letter relevant to the offer in every case. Each paragraph serves the case for this job, and every revision keeps it so: humanising the wording, adding a personal touch or reusing another letter's phrasing must not move the letter away from what the offer states.

## Get this job's words first

Before drafting, check the applicant's supplied goals, current-job motivation, examples and desired tone against the three outcomes above. If a personal reason or connection is missing, ask a targeted question and wait for that input instead of filling the gap with CV facts. Useful questions include “What about this work interests you?”, “Which experience, project or opinion connects you to it?” and “What would you want to contribute?” Ask only what is missing; do not make the applicant repeat current material.

If the applicant explicitly requests a factual skeleton before supplying motivation, provide supported qualifications and application intent without invented personal claims. Label it an incomplete skeleton awaiting personal input, not a completed cover or motivation letter. Identify which personal answers are still missing; do not conceal those gaps with a polished generic opening. Formatting or rendering it does not satisfy the three outcomes.

Consult relevant Entry notes and Personality entries before asking for examples again. Reuse applicant-authored context selectively when it fits this role; check job-specific motives rather than blindly carrying them between vacancies. A Personality entry gives the letter a personal touch, but it does not answer why this job interests the applicant. An approved draft, generated letter or approved translation is not raw applicant input: preserve its actual authorship and approval history and follow Languages for eligible translations.

Save the actual reply in the agreed application records with accurate provenance. Do not label agent-written motivation as user input or reuse another vacancy's motivation. With native helpers, use `wording` to create the application-bound snapshot and populate `plan.user_input`, with `--must-include` only for genuinely required phrases.

Keep the user's meaning, register and degree of directness. Work from their outline and wording before smoothing it, and show consequential changes for approval. Preserve explicitly required phrases; do not invent quirks, sentiment or a stock enthusiasm paragraph to make the letter sound personal. Faithful paraphrasing is allowed when that is what the applicant wants; raw quotations still remain exact.

The native wording check additionally requires meaningful excerpts of at least three words in `letter.wording_quotes` and at least one verbatim excerpt in a letter sentence. Follow that helper contract when using it; it is not a general rule that every manually drafted letter must quote the applicant. `check`/`build` reject missing, changed or cross-application wording snapshots. Whitespace normalization is not permission to rewrite quotes.

Current-job words can express intent; factual examples still require verified candidate evidence. Add newly confirmed facts through a reviewed profile update, not by treating the wording snapshot as automatic qualification evidence. Company-research outages may limit company claims, but never justify a generic invented-letter fallback: work from genuine user words or pause.

The native `wording`/`check`/`build` path requires job-specific user wording before completing its letter. Explain and satisfy that selected helper's gate, rather than claiming a factual draft made with other tools has passed it.

## Make the connection specific and the voice personal

Use a personal detail because it explains the applicant's interest or contribution, not merely to decorate the opening. Tie it to something concrete in the opportunity. A project name, an emotional adjective or “I am passionate about this field” does not establish that connection by itself.

Select CV evidence only where it advances the argument. Explain what an experience taught the applicant or enabled them to do, where supported, and how that matters for the advertised work. Give each selected fact this context instead of narrating facts: do not retell the CV's chronology, list tools and responsibilities, or restate the job offer to the people who wrote it. Replace vague claims such as “my background aligns with the role” with the actual relationship between experience, task and contribution.

Write directly and personally, in a human, non-formulaic tone that is neither overly formal nor dry, without ceremonial corporate language. Make the letter distinctive, creative and bold through the applicant's own perspective, a revealing example or a clear argument about what they can bring. Give it a personal touch in the applicant's own words, such as a relevant Personality entry. Calibrate the expression to their voice; do not force theatrical openings, slogans or an invented persona. Do not polish away a genuine feeling or opinion merely to sound conventional.

Keep opinions, hopes and hypotheses recognisable as such. Boldness can make a real point of view explicit; it cannot turn a possibility into a promised outcome or supply missing achievements. A feeling can explain motivation, but it is not evidence of a qualification.

## Review the argument before calling the letter complete

Point to the passages that substantively answer each of the three outcomes. If one is absent, obtain the missing applicant input or revise the argument before presenting the letter as complete; a correct CV recap does not pass.

Check every statement about the job against the offer's text, and every link between the offer and the applicant against both sources. Check that each selected example explains fit or contribution, that the personal connection has an applicant source, and that the paragraphs develop the same case. Apply a substitution test: if changing only the employer and job title leaves the letter equally convincing for an unrelated vacancy, its connection is too generic. Specificity comes from the reasoned connection, not extra employer names or praise. Review the tone against the applicant's words, not a default formal-business style. These are semantic checks; native provenance validation cannot perform them.

## Retain voice without inventing character

Keep `tone_preferences`, `character_notes`, `writing_preferences` and `avoid` based on explicit user statements or confirmed edits. Character notes must be user-confirmed descriptions, not inferred personality from a CV or writing style. Use retained samples as voice guidance only; they do not establish new skills, achievements, employer facts or current-job motivation.

Optional `remember-voice --text-file ... --source ...` retains the genuine raw sample in profile `voice.samples`. Persistent raw samples are intentional here; keep them private with accurate provenance. Retain user-approved edits as their voice only after confirmation; never silently store AI output as user authorship. This changes the profile and invalidates its seal; follow Onboarding for review. After an accepted letter, identify any genuine user wording or confirmed phrasing preferences worth keeping for future letters. Retain those with provenance rather than claiming silent learning; current-job originals already remain in the application.

After source checks, review the draft with the applicant for factual accuracy, authentic motivation, tone, required wording and unwanted filler. Code can check references and literal inclusion; only the applicant can approve their voice.
