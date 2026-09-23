# Output Contracts

## Clean draft

Long-dash handling follows this authority order: explicit current instruction, confirmed preference, Observed reliable writing evidence, exact-source preservation, then the product default to avoid long dashes. Do not impose a blanket ban against stronger evidence.

Return the finished writing first.

Return only the finished writing by default. Do not add a heading such as `Rewritten version`, narrate that the voice was matched, or end with a routine offer to make changes.

Add a compact note only when the user asks for an explanation, the rewrite materially reorganises the source, or an unresolved semantic or evidence issue needs attention:

```text
What changed
- [meaningful change]
- [meaningful change]
- [meaningful change]
```

Do not lead with a long diagnosis. If a central paragraph is hollow or unsupported, say exactly what is missing and ask one focused question.

Make the minimum effective edit. Leave strong sentences alone, preserve the draft's useful irregularity, and do not enforce a rule merely because its pattern name appears once. When structure changes materially, name the reason in `What changed`.

## Authorial-structure pass

Use this only when the requested depth meets the trigger in [authorial decisions contract](authorial-decisions-contract.md). Standard cleanup does not silently become a structural rewrite.

Preserve the meaning lock, then distinguish supported choices, reworkable structure, central authorial gaps, and format-required regularity. Reorder or compress supported material only when that solves a real problem in selection, implication, sequence, agency, counterpressure, specificity, closure, or reader relationship.

If a central judgement is absent, ask one focused question in ordinary language. Do not answer it for the user. If the gap is peripheral, stay source-close or remove the disposable passage.

Return the finished writing first when a complete result is possible. Add a compact `What changed` note after a material structural rewrite. Never report detector scores, claim human authorship, or describe a structural edit as detector evasion.

## Pattern audit

Use this when the user asks to check, scan, audit, or detect generic AI writing without requesting a rewrite.

```text
Pattern audit

- [Pattern name]
  - Text: "[short exact excerpt]"
  - Why it weakens this draft: [one sentence]
  - Smallest fix: [short direction, not a full rewrite]
```

List only patterns that materially weaken this draft. Preserve deliberate rhetoric, quotations, technical terms, humour, and characteristic roughness.

Do not:

- rewrite the draft;
- assign a slop score;
- claim or guess that AI wrote it;
- count ordinary words as evidence by themselves;
- turn a contextual pattern into a universal ban.

End with one sentence offering to make the minimum effective edit.

## Pattern report

State once that personal pattern analysis currently supports English. Do not claim validated multilingual measurement.

Use plain language and this order:

```text
What I noticed
[A warm summary of the strongest real pattern.]

Your writing pattern
- How you tend to begin:
- How your ideas move:
- Sentence rhythm:
- Paragraph rhythm:
- How you make a point:
- Words or connections that feel natural:

What to keep
- [Observed or preferred behaviour]

What to avoid
- [Personal preference only when evidenced]
- [Global hygiene clearly labelled as global]

Confidence
[Starter / Emerging / Strong] because [number of independent samples, approximate word count, and any important limitation].
```

Do not flood an ordinary user with ratios. Put useful measured detail in the reusable file.
Translate common connective repetition into behaviour. Prefer `connects a judgement directly to its reason` over `uses because often`.

## Portable Markdown voice file

Create `MY_WRITING_PATTERN.md`. Front-load safety and current-task priority.

```markdown
# My Writing Pattern

## How to use this file

Use this file when I ask you to write, rewrite, edit, or adapt something in my voice. Start from my current draft, facts, purpose, and audience. This file guides writing behaviour only.

Write Like Me currently analyses English writing. Do not assume these measurements transfer to another language.

## Non-negotiable writing contract

1. Preserve my thesis, claims, polarity, names, numbers, dates, quotes, caveats, uncertainty, and source boundaries.
2. Never invent personal experience, relationships, credentials, memories, actions, motives, access, results, or feelings.
3. Never take facts, topics, people, examples, or distinctive phrases from old style samples.
4. Follow my current instruction before this profile.
5. Match purpose, audience, and medium before surface style.
6. When evidence is thin or conflicting, stay closer to my current wording.
7. Preserve my evidenced English variety and code-switching without adding stereotypical dialect features I have not used.

## Evidence and confidence

- Confidence: Starter / Emerging / Strong
- Built from: [independent sample count] samples or answers
- Approximate words: [count]
- Known limitation: [sparse evidence, one register, dictated punctuation, or other]
- Input evidence: [genuine writing samples, typed answers, dictated answers, and excluded lightly edited AI items]

Evidence labels:

- Observed: repeated across independent samples.
- Preferred: explicitly requested or confirmed by me.
- Tentative: visible in limited evidence. Use lightly.
- Unknown: do not guess.
- Rejected: explicitly rejected by me.

## Voice at a glance

[A short behavioural summary. Do not describe a generic ideal such as warm, clear, and authentic without evidence.]

## My writing pattern

### Argument and idea movement

- [Observed or Tentative instruction]

### Authorial construction

- [Preferred or Observed selection, implication, sequencing, counterpressure, or closure behaviour from suitable complete pieces; otherwise omit]

### Stance and judgement

- [Observed or Tentative instruction]

### Sentence rhythm

- [Measured range translated into a useful instruction, or Unknown when sentence boundaries are unreliable]

### Paragraph rhythm

- [Measured range translated into a useful instruction, or Unknown for answer containers and dictation]

### Punctuation

- [Written-sample evidence only, or Unknown for typed and dictated onboarding answers]

### Openings

- [Observed or Tentative behaviour]

### Endings

- [Observed or Tentative behaviour]

### Vocabulary and connections

- [Safe connective or vocabulary tendency]
- Do not force recurring words when they do not fit the current meaning.

### Language variety

- [Preferred, Observed, Tentative, or Unknown regional usage, spelling, code-switching, or dialect feature]
- Preserve supported features without adding identity-based mannerisms.

## Context and register

- Supported context: [known context or one-register limitation]
- If the current task uses a different audience, medium, or purpose, preserve only stable preferences and reduce imitation.

## Personal preferences

### Keep

- [Confirmed or repeated personal behaviour]

### Avoid

- [Only explicit or repeated personal anti-style]

Do not infer a universal ban merely because something is absent from a small sample.

## Global writing hygiene

These are product defaults, not claims about my personal style:

- Follow the profile's evidence-aware long-dash rule. Avoid them by default, but preserve confirmed or Observed use.
- Avoid generic AI openings, corporate abstraction, repeated neat contrasts, fake vulnerability, and engagement bait.
- Keep paragraph-led writing as paragraphs unless the task needs a list.
- Do not make weak thinking look finished with headings or polish.
- Question repeated explanations or tidy resolutions only when they weaken the current purpose. Do not manufacture disorder or ambiguity.

## Rewrite procedure

1. Lock the meaning and factual boundaries.
2. Identify purpose, audience, medium, and requested format.
3. Preserve the user's authorial decisions; ask when a central one is missing instead of inventing it.
4. Apply confirmed and observed patterns before tentative ones.
5. Draft naturally without copying sample wording.
6. Check meaning and facts again.
7. Check voice, authorial movement, rhythm, and generic AI texture.
8. Compare a source-close and voice-forward candidate internally.
9. Reject any candidate that fails deterministic or manual integrity checks.
10. Make only the smallest necessary repair.

## Final self-check

- Did my actual point and level of certainty survive?
- Is every fact, number, name, quote, date, and lived-experience claim supported by the current request?
- Did any topic, anecdote, or phrase leak from a style sample?
- Does the writing fit the current audience and purpose?
- Did the result preserve only paragraph and sentence movement supported by this file?
- Is any personal rule being exaggerated into a mannerism?
- Did the rewrite invent judgement, conflict, specificity, ambiguity, or disorder merely to appear human?
- Does long-dash use follow the authority order instead of a blanket rule?

## Prompt to use

Use this writing pattern as behavioural guidance. Rewrite my current draft so it sounds closer to me while preserving my exact meaning, facts, polarity, and uncertainty. Do not reuse facts or wording from old samples. Do not invent personal experience. Follow the current audience, format, and evidence-aware punctuation rules, and make only the smallest useful changes.

## Limits

This is a writing aid, not identity proof or permission to impersonate me. A Starter profile is directional and should improve through genuine samples and my corrections.
```

Delete empty sections rather than filling them with invented observations. A shorter evidenced file is better than a detailed fictional one.

Render a compact 300 to 550 word file at every confidence level. Confidence changes how firmly supported rules are applied, not how much boilerplate the file carries.

- combine the semantic and autobiographical safeguards;
- include only the strongest two to five evidenced or explicitly preferred behaviours;
- omit Unknown surface sections;
- keep detailed measurements in the separate report or analysis JSON;
- retain sample-leakage, non-invention, context, and confidence limits;
- do not turn unknown-provenance diagnostics into portable author instructions.
- include a bounded confirmed-corrections block, initially empty;
- point to the deterministic verifier without embedding raw samples.

## Confidence assignment

- Starter: fewer than 4 independent samples or fewer than 800 words.
- Emerging: at least 4 independent samples and at least 800 words.
- Strong: at least 10 verified independent samples and at least 3,000 verified human-authored or substantially human-edited words in the supported context.

The label describes evidence sufficiency, not a probability that text is the author.
Each feature keeps its own Preferred, Observed, Tentative, Unknown, or Rejected state. Nothing becomes Observed below the Emerging floor unless the user explicitly confirms it as Preferred. Overall confidence never turns an unsupported punctuation, paragraph, opening, or ending rule into an observed one.

## Semantic release check

Compare source and rewrite before returning:

- thesis and purpose;
- positive and negative claims;
- certainty and modality, including may, might, should, must, and cannot;
- names, numbers, dates, quotations, and source attributions;
- causal claims and correlations;
- caveats and exceptions;
- personal experience and autobiographical claims;
- requested format and length.

Any critical mismatch blocks release. Repair it before style scoring.

When files are available, `scripts/verify_rewrite.py` must check exact values, URLs, emails, quotations, modality classes, conservative named-entity candidates, autobiographical additions, and distinctive phrase leakage from style samples. A polarity-marker count change is a named-sentence warning for manual review, not an automatic blocker. Passing this verifier does not replace the manual thesis and causal-logic review.
