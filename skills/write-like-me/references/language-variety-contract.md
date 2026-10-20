# Language Variety Contract

Use this contract when learning or applying a personal writing pattern in English.

## Core rule

Treat regional English, dialect, sociolect, code-switching, and community usage as possible voice evidence, not defects to normalise automatically.

Preserve only features supported by one of these authorities, in order:

1. the user's explicit current instruction;
2. a confirmed preference or correction;
3. repeated use across eligible independent samples in the relevant context;
4. a tentative feature used lightly when evidence is sparse.

Never add a construction merely because it is associated with an identity, nationality, location, ethnicity, age, profession, or community. A dialect reference is a preservation aid, not a phrase bank.

## What may count as evidence

Eligible evidence may include:

- spelling and punctuation conventions;
- regional vocabulary and idiom;
- function words, discourse particles, and tag questions;
- characteristic prepositions, tense choices, agreement patterns, or emphasis;
- code-switching and untranslated terms;
- directness, politeness, formality, and relationship marking;
- context-specific differences between public, professional, and private writing.

Keep every feature bounded by its source reliability. Dictation may support wording and discourse particles but not punctuation or deliberate sentence boundaries. One vivid phrase does not establish a dialect rule.

The deterministic starter-profile builder does not identify a writer's dialect. The host model applies this contract contextually and may add a variety rule to the portable profile only when the evidence above supports it.

## Preservation without performance

- Do not silently convert eligible Indian, Australian, British, American, Singaporean, Nigerian, Kenyan, Caribbean, or other English usage into a generic standard variety.
- Do not insert regional slang, phonetic spellings, grammatical features, or code-switching that the user did not supply or request.
- Do not exaggerate a supported feature until it becomes a mannerism.
- Do not label a feature as incorrect merely because a style guide for another variety rejects it.
- Preserve an organisation's required house style when the current task explicitly requires it, and treat that as a task constraint rather than the user's permanent voice.

When evidence conflicts, prefer the current audience and purpose, keep the feature Tentative or Unknown, and stay closer to the user's current wording.

## Profile representation

Record only useful behavioural guidance. Examples:

- `Preferred: Use Australian spelling in professional writing.`
- `Observed in personal messages: uses a short tag question to soften a request.`
- `Tentative: keeps some Hindi terms untranslated when writing to family.`

Avoid identity claims such as `writes like an Indian person` or broad instructions such as `add Australian slang`. The portable profile describes writing behaviour, not demographic identity.

## Release check

Before returning personal prose, ask:

1. Did the rewrite erase an evidenced regional or community feature without a task reason?
2. Did it introduce a dialect marker absent from the instruction and eligible evidence?
3. Did it turn one feature into a repeated performance?
4. Did it mistake dictated transcription punctuation for a personal habit?
5. Does the result still fit the current audience, relationship, and medium?
