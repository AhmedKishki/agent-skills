# Strong plain-prompt baseline

Use this prompt in a fresh conversation with the same model and settings as the Write Like Me arm. Replace every bracketed field. For blind comparison, copy only the rewritten artifact into the study file.

```text
Rewrite the current draft so it sounds natural and recognisably like the author while keeping the author's actual point.

Current audience: [AUDIENCE]
Purpose: [PURPOSE]
Writing context and format: [CONTEXT AND FORMAT]

Non-negotiable meaning rules:
- Preserve the thesis, polarity, facts, names, numbers, dates, quotations, causal relationships, and level of uncertainty.
- Do not add an opinion, emotion, achievement, client, meeting, anecdote, or lived experience that is not supported by the current draft or an explicit instruction.
- Do not make a tentative claim sound proven or a personal judgement sound universal.

Author evidence rules:
- Use the samples or answers only to infer supported writing behaviour such as explanation order, directness, qualification, judgement, rhythm, and reader relationship.
- Do not transfer sample facts, stories, topic vocabulary, opinions, or distinctive phrases into the new draft.
- Treat dictated or prompt-container punctuation and paragraphing as unknown, not as the author's habit.
- When evidence is mixed or weak, prefer clear natural prose over exaggerated imitation.

Writing rules:
- Fit the stated audience, purpose, context, and requested format.
- Remove hollow scene-setting, generic engagement bait, inflated abstraction, repetitive summary, and unnecessary signposting.
- Do not make every paragraph a one-line hook.
- Do not use em dashes or en dashes unless preserving an exact quotation or a source number/date range.
- Keep useful specificity and ordinary human variation. Do not add deliberate errors or fake messiness.

Return only the revised draft. Do not explain the changes or mention these instructions.

CURRENT DRAFT
[PASTE THE UNSEEN CURRENT DRAFT]

AUTHOR EVIDENCE
[PASTE THE SAME GENUINE SAMPLES OR QUICK ANSWERS THAT WERE AVAILABLE WHEN THE WRITE LIKE ME FILE WAS BUILT. FOR A DRAFT-ONLY FIRST-CLEAN TRIAL, WRITE: No author evidence supplied.]
```

