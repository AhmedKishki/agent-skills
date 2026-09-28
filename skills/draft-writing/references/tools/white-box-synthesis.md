---
name: white-box-synthesis.md
description: Construct prose from exact eligible inputs and expose every sentence's lineage and operations.
---

# White-Box Synthesis

White-box is the basis for synthesis. Read the local arc, relevant material and shared source excerpts, then [decisions](../rules/decisions.md). Inputs are exact approved local Human or eligible Mixed wording and approved source-map excerpts. Local approved outputs require finite, recoverable lineage; reject circular or unavailable bases. Another section's user inputs, material and draft are not eligible inputs.

Source wording remains source-authored. Instructions and article-wide direction are not automatically article prose. Include author wording when it improves the passage; do not force it into every paragraph. Source-only synthesis is valid. Respect explicit exclusions.

Approval never converts Mixed into Human. An output using an eligible Mixed input remains Mixed. Explicitly AI-authored or `⟦AI-AUTHORED: ...⟧` spans are permanently ineligible for white-box, even when approved and stored in material. Exclude those spans and relations dependent on them, not all Mixed text. Verify and approve unverified inputs before use.

## Operations

- **COPY:** Copy a contiguous span.
- **DELETE:** Remove words without changing subject, scope, modality, qualification or relation.
- **ORDER:** Arrange spans only where an authorised input establishes their relation.
- **INFLECT:** Change tense, number, grammatical case, article or an unambiguous pronoun without changing meaning.
- **NORMALISE:** Make meaning-neutral spelling, capitalisation, typography or punctuation changes.

No operation may invent a connection, cause, comparison, interpretation, qualification or conclusion. Grammatical fluency does not prove a relation.

## Proposal

1. Identify the local passage, its purpose, exact eligible inputs, provenance and evidence limits.
2. Construct the passage and check every meaning-bearing word and relation against those inputs.
3. Show the complete output and a construction record for every sentence.
4. Obtain exact approval, then save to the specified owner. Material approval and draft insertion are separate decisions.

For each output sentence, show the exact output; every input label and file location; its author, source and locator; the exact copied span; and every operation. Spell out deleted words, inflections, normalisation and the basis for ordering. Codes, counts or summaries alone do not meet this requirement.

For example, from an approved excerpt by Lee, *Example Book*, p. 3, containing `As noted earlier, prices rose.`, a proposal for `Prices rose.` must show the excerpt's actual file and label, that full copied span, DELETE `As noted earlier, `, and NORMALISE `p` to `P`. This is a hypothetical demonstration, not a source to cite.

Keep construction records in the approval proposal. Saved material keeps exact local inputs, basis references, provenance and live constraints, not operation logs. Direct user edits remain intact; review affected lineage before reuse rather than assigning authorship by guesswork.

## Gaps

Identify the smallest missing wording, evidence, relation or authorisation and explain why these operations cannot supply it. Stop only the affected work. Ask for author wording, further evidence work or an explicitly requested [AI-authored proposal](ai-authored.md); do not volunteer invented prose.

When a complete passage also contains approved AI gap text, distinguish that direct insertion from white-box construction. Give the eligible sentences their full construction records and show each marked AI span separately with its authorship, destination and limits. Never use the span as an input or remove its label to make the passage appear wholly white-box.
