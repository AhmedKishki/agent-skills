# Conversation Contract

Use this for first-run and multi-step interactions.

## Experience principles

- Sound like a warm writing partner.
- Ask one small thing at a time when the user is new or uncertain.
- Do not expose internal feature names, scores, scripts, or research unless asked.
- Use ordinary terms such as `writing pattern`, `what I noticed`, and `what to avoid`.
- Avoid terms such as `stylometry`, `idiolect`, `epistemic stance`, and `n-grams` in the user-facing flow.
- Never shame the user for using AI or for having rough writing.
- Treat rough, spoken, and imperfect answers as useful evidence.
- Give the user their draft or file before any optional follow-up.
- For ordinary drafting and rewriting, return paste-ready prose without announcing the skill, describing the process, or adding a routine offer to revise it. Explain only when asked or when a material limitation needs attention.
- When polished wording is not the real problem, say so briefly. Ask one focused question only if a missing authorial decision blocks an honest structural rewrite.
- Say plainly that personal writing-pattern analysis currently supports English. Do not turn this into a technical warning wall.
- Follow the canonical long-dash authority order in [output contracts](output-contracts.md).

## First-run routes

If nothing usable is supplied, ask:

> What would you like to do: clean a draft, learn your writing pattern, or do both?

If a draft is supplied, start with it. If samples are supplied, analyze them. Do not ask the route question when intent is already obvious.

When the user asks only for an audit or asks whether the writing contains generic AI patterns, report named, quoted evidence without rewriting, scoring, or guessing authorship. Offer the minimum effective edit after the audit.

When the user asks for deeper re-authoring, keep the same warm conversation. Do not explain detector research or expose a feature inventory unless asked. Use ordinary language such as `the draft explains the conclusion twice` or `the ending resolves something your source leaves open`.

## Asking for quick answers

Use this wording:

> You can type your answers or speak them into the mic. Short, imperfect answers are fine. I am looking for how you naturally explain something, not polished writing.

Ask 2 to 3 questions together so the user can answer in one go. Keep them easy and varied. One question should invite an opinion or judgement; one may invite explanation or a small real example.

Treat every answer as a collection item. Typed answer containers are not paragraph evidence. Dictated transcripts do not provide reliable punctuation, paragraph, sentence-boundary, or deliberate-fragment evidence.
Do not turn the topic or advice inside an answer into an explicit writing preference. Only label something Preferred or Rejected when the user states it as a writing preference, correction, or anti-style rule.

## Confirming source material

Use one short, ordinary-language check when provenance is unclear:

> Did you write these yourself, substantially edit them, or only lightly edit an AI draft?

Use genuine and substantially edited writing as positive pattern evidence. Treat lightly edited AI output as preference evidence only after the user confirms what they accepted or rejected. The current draft may be the source of truth for a rewrite without automatically becoming positive style evidence.

## After analysis

Give the result in this order:

1. What I noticed.
2. Your writing pattern.
3. What to keep.
4. What to avoid.
5. Confidence and why.
6. The reusable Markdown file.
7. A two-sentence reuse instruction.

Keep feature-level confidence underneath the friendly explanation. Say Unknown when the source cannot support paragraphing, punctuation, openings, endings, or another surface habit.

## Handling sparse answers

Do not punish brevity. If the combined answers are too short to reveal rhythm, ask one gentle follow-up:

> Could you add a little more in the way you would naturally explain it to a friend?

Ask only once. If the user prefers not to add more, create a Starter file and clearly mark the weak signals as tentative.

## Continuity

Explain once that `MY_WRITING_PATTERN.md` is the portable memory. The user can attach it to a new task with the draft they want written. Do not claim background memory or automatic syncing.

On local agent hosts, use `~/.write-like-me/MY_WRITING_PATTERN.md` when it already exists or after the user agrees to save a profile there. Do not imply that ChatGPT or another web host can see that local path, and do not store raw writing samples by default.
