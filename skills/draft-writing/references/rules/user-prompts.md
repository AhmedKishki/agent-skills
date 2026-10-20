---
name: user-prompts.md
description: Route each part of a prompt to its owner without turning instructions or source quotations into author prose.
---

# User Prompts

Read the current object before applying a prompt or direct edit. Apply [Binding ownership](../../SKILL.md#binding-ownership) to each information unit before writing; the owner module's Allowed list must admit it. A relevant unit is not automatically allowed. Separate independent parts by function, preserving exact reusable wording. A multi-part prompt can update several owners, but each unresolved substantive decision follows [decisions](decisions.md), one question at a time.

| Content | Owner |
|---|---|
| Motivation, theory, explanatory commitments, scope or main thesis | `organisation/thesis-and-vision.md` |
| Audience, tone, style, length, quotations, footnotes or a standing project requirement | `organisation/requirements.md` |
| Article section order, overall section purpose or drafting/review sequence | `organisation/plan.md` |
| A section's argument, passage order or necessary connection | `arc-section-n.md` |
| Exact reusable author wording with a clear local destination | Labelled local input beside that passage in `material-section-n.md` |
| A quotation from another author | [Source mapping](../supplement/source-maps.md); retain source authorship and verify identity and locator |
| Revision to prose | [Drafting](../section/draft.md) or [smoothing](../tools/smoothing.md); propose the exact amendment |
| Approval or rejection | The exact identified object's owner and its local handoff |
| Pause, next action, unresolved local question or unfinished verification | `progress-section-n.md` |
| One-off procedural command | Perform the authorised action; retain only unfinished resume state |

For example, route a new thesis to thesis-and-vision, a citation instruction to requirements, and an exact sentence for section 2 to that section's local material. Do not preserve the entire mixed prompt as article prose.

Preserve exact user spelling, punctuation and paragraph breaks. Instructions are not eligible prose or voice evidence. User-pasted quotations remain source-authored; approval does not make them the user's words. Routing an input does not approve a claim, synthesis, connection or insertion.

If placement or intent is unclear, ask one focused question before writing it into a content owner. A pause may retain only the unresolved placement question and exact input required for the next decision, under progress's bounded pending-object exception. Before any section exists, use `organisation/plan.md`'s bounded setup exception instead; remove it when resolved. Do not create an inbox or miscellaneous material file. Article-wide pending questions stay beside their target owner.

Do not copy a user input to several sections to bypass source-only sharing. Ask for the destination or an explicit change to that rule. Direct user edits remain intact; if an edit changes evidence, provenance, placement or apparent authorship, identify the affected span and ask about the unresolved part rather than silently undoing or reclassifying it.

After routing, verify each unit against its Allowed list, keep its qualifications in the same owner, and remove duplicate routing commentary rather than writing "recorded in" or "held elsewhere" summaries. Instructions must not become prose; author/source wording remains distinguishable. Do not retain a duplicate prompt transcript after routing its live parts.
