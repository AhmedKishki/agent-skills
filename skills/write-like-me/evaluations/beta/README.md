# Private beta: blind baseline protocol

This protocol answers one question before a wider release:

> Does Write Like Me create a visible advantage over a genuinely strong plain prompt for ordinary writers?

The study is directional product evidence, not a publishable scientific claim. Recruit 10 to 20 writers and aim for two unseen writing tasks per writer.

## The two arms

Use the same platform, model version, settings, target draft, audience, purpose, and output format within each pair.

### Strong plain prompt

- Start a fresh conversation without Write Like Me or `MY_WRITING_PATTERN.md`.
- Use `strong-plain-prompt.md`.
- Supply the target draft and the same raw evidence originally available to Write Like Me: genuine samples or quick answers.
- Do not weaken this prompt or omit its safety instructions.

### Write Like Me

- Build `MY_WRITING_PATTERN.md` before the unseen trial.
- Start a fresh conversation with Write Like Me enabled.
- Supply the target draft and portable file, but do not supply the raw samples again.
- Ask for the same audience, purpose, context, and output format.

This is deliberately a hard baseline. It tests whether the portable profile can match or beat direct access to the raw evidence while requiring less repeated setup.

For a draft-only first-clean trial, neither arm receives samples. The baseline receives the current draft through `strong-plain-prompt.md`; Write Like Me receives the same draft through its clean-draft route.

## Keep the target unseen

The target draft must not reuse the topic, story, facts, names, or distinctive phrases in the samples used to make the profile. A user's real new writing task is best. If that is unavailable, ask them to draft a short piece about a new topic before either arm is run.

## Run order

1. Give the participant the plain-language privacy and consent note.
2. Record a participant ID, never their name, in study files.
3. Complete Write Like Me onboarding and create the portable file.
4. Ask for two new drafts in supported contexts. Do not use either draft as profile evidence.
5. Run both arms in fresh chats. Keep the model and settings identical within each pair.
6. Copy only the primary rewritten artifact into `beta-cases.json`. Remove explanations and system labels that could reveal the arm.
7. Prepare randomized A/B packets with `run_blind_beta.py prepare`.
8. Let each writer judge their own A/B outputs. Do not reveal the answer key.
9. Record one trial ballot per comparison and one participant outcome row per writer.
10. Score only after all ballots for the batch are locked.

Do not let the person who generated the outputs coach the writer during blind judging. If assistance is unavoidable, record it in the notes and do not count that trial as clean preference evidence.

## Prepare blinded packets

Copy `beta-cases.example.json` to a private working file and replace the placeholder outputs.

```bash
python3 scripts/run_blind_beta.py prepare \
  --cases evaluations/beta/beta-cases.json \
  --pack evaluations/beta/blinded-review-pack.json \
  --key evaluations/beta/private-answer-key.json
```

Keep `private-answer-key.json` away from participants and reviewers until ballots are locked. The preparer alternates which system appears as A within each participant, with a randomized starting arm, so two-trial participants see each system first once.

## Trial ballot

Use `trial-ballots-template.csv`. Allowed values:

- `sounds_like_me`, `preserves_meaning`, `less_editing`, `overall_preference`: `A`, `B`, or `TIE`.
- `edit_burden_a`, `edit_burden_b`: `0` send as-is; `1` tiny edits; `2` light edits; `3` substantial edits; `4` rewrite it.
- `critical_failure_a`, `critical_failure_b`: `NONE` or one or more of the codes below, separated with `+`.

Critical failure codes:

- `MEANING`: changed thesis, polarity, or causal relationship.
- `FACT`: changed a name, number, date, quotation, or factual relationship.
- `UNCERTAINTY`: removed or increased uncertainty without permission.
- `BIOGRAPHY`: invented lived experience, emotion, client, meeting, or achievement.
- `SAMPLE_LEAKAGE`: transferred a fact or anecdote from a sample.
- `PHRASE_COPY`: copied a distinctive unrelated sample phrase.
- `CONFIDENCE`: made an unsupported Strong or equivalent evidence claim.
- `MODE`: claimed a mode without sufficient evidence.
- `DICTATION_SURFACE`: treated dictated punctuation or paragraphing as a personal habit.

Write the reason the rejected output felt wrong in plain language. Those comments are product evidence, especially when the aggregate choice is a tie.

## Participant outcome

Use `participant-outcomes-template.csv` once per writer. Boolean fields accept `YES`, `NO`, or `N/A`.

Test fresh-chat reuse in front of the participant. `reused_without_help` is `YES` only if they attach or paste the portable file, provide a new draft, and obtain a useful result without procedural help.

For comprehension, ask the person to explain `Starter` and `Unknown` in their own words. Do not ask whether they understand the terms and accept a yes.

## Score the batch

```bash
python3 scripts/run_blind_beta.py score \
  --key evaluations/beta/private-answer-key.json \
  --ballots evaluations/beta/trial-ballots.csv \
  --participants evaluations/beta/participant-outcomes.csv \
  --result evaluations/beta/beta-result.json
```

The result keeps critical failures outside the preference average and reports a Wilson interval to show how uncertain a small beta remains.

## Pre-registered directional decision

The script reports:

- `blocked_safety_failure` if Write Like Me has any critical failure;
- `collect_more_data` below 10 writers or 20 comparisons;
- `directional_product_advantage` at 60% or more Write Like Me preference among non-tied overall choices;
- `tie_or_positioning_shift` from 45% to below 60%;
- `baseline_advantage` below 45%.

Supporting targets are 70% fresh-chat reuse without help and 80% comprehension of Starter and Unknown. These targets diagnose the product; they do not override a safety blocker.

Interpretation:

- A product advantage supports a v0.4 public candidate.
- A tie means the defensible value may be portability and safety rather than superior prose. Reposition before widening release.
- A baseline advantage means pause release expansion and investigate why the portable profile loses useful evidence or constrains the model badly.

Do not publish a preference percentage from 10 to 20 writers. Preserve the protocol, model versions, raw ballots, exclusions, and result file so a later claim can be audited.

## Privacy minimum

- Use participant IDs instead of names in filenames and study tables.
- Keep raw samples, target drafts, outputs, answer keys, and ballots in a private folder.
- Tell participants which model provider receives their text.
- Do not use their text for model training, marketing, or public examples without separate explicit permission.
- Delete raw text on request and record the deletion.
- Keep only de-identified aggregate results by default after the evaluation window.
