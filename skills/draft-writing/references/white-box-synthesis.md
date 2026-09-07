# White-box synthesis

## Purpose

Transform one approved passage plan and one limited approved input set into one candidate passage with a complete construction record, or one typed gap.

## Inputs

- **Passage ID and claim:** the single claim the passage must establish.
- **Arguments:** ordered argument IDs and claims that together establish the passage claim.
- **Fragments:** only the limited input set explicitly approved in predraft: original codes (`user-n` or `src:A4`), exact human passages with their original span locations, context that identifies subject, scope, modality and qualification, and permitted use: wording, evidence, user interpretation, or framework check.
- **Constraints:** the user's wording priorities, spelling convention, quotation requirements, applicable conceptual limits and governing article-arc comments.

The approved claim and arguments fix the target. Approved fragments supply vocabulary and substantive bases. The article arc's broad inventories are not synthesis inputs and must never be passed to a run automatically. One run targets exactly one passage, which may contain zero, one or multiple paragraph breaks.

## Procedure

1. Match each argument to approved fragments. Identify its claim, qualifications and contribution to the passage claim.
2. Develop each argument as prose, using the five operations below on contiguous spans that contain a complete word, phrase or clause. Keep every meaning-bearing word traceable to an approved passage.
3. Assemble the argument spans in approved order. Check that they jointly establish the passage claim and that internal connections and qualifications follow from approved originals.
4. Return **Passage**, **Provenance**, and **Record** only when every argument and output span passes the checks below. Otherwise return one typed **Gap**.

| Operation | Rule |
|---|---|
| COPY | Reproduce an exact contiguous span. Valid: copy a complete clause. Invalid: insert an absent synonym. |
| INFLECT | Change only tense, number, grammatical case, article, or an unambiguous pronoun. Valid: `workers are` → `a worker is`. Invalid: `may` → `will`. |
| NORMALISE | Make meaning-neutral spelling, capitalization or punctuation changes. Valid: apply the approved spelling convention. Invalid: replace vocabulary. |
| ORDER | Arrange spans only when an approved original explicitly establishes their relation. Valid: reorder an enumerated list. Invalid: imply causation from co-occurrence. |
| DELETE | Remove repetition only when subject, claim, scope, modality and qualification are identical. Valid: delete a repeated identical clause. Invalid: delete a limiting qualification. |

Apply INFLECT and NORMALISE to unquoted output. Keep direct quotations, saved originals, code, URLs, titles, and citation data exact. Preserve the spelling of proper names, trademarks, official names, and defined terms; adjust their capitalization only where unambiguous and meaning-neutral.

Every word, including a function word inserted at a join, must occur in an approved fragment in the required sense and be recorded by an operation. Do not alter the passage plan. Preserve a user's interpretation as their argument; treat source evidence as support only for what it establishes; use framework-only inputs only for fit checks.

Use one gap type: `Missing user wording`, `Missing evidence`, `Unsupported connection`, `Source-context ambiguity`, `Arc inconsistency`, or `Constraint conflict`. State the passage ID, affected argument ID, missing requirement, authoritative owner, one focused question and allowed resolution paths.

## Output

```markdown
Passage: <complete candidate passage>

**Provenance:** Mixed · Human wording: 100% · Method: white-box synthesis · Basis: A4, user-21, user-22

Record:

| Argument | Result span | Original fragments | Construction and support |
|---|---|---|---|
| 1.1.1 | <exact output passage> | <codes, locators and exact human spans> | <operations in order, source support and limits> |
| 1.1.2 | <exact output passage> | <codes, locators and exact human spans> | <operations in order, source support and limits> |
```

Give each argument one record row and cover the complete passage. Quote every exact fragment used, identify its original code and location, and name each source once. Show every operation in execution order. Explain what evidence establishes and what remains the user's interpretation. State passage-wide evidence or framework consultation after the table.

For unchanged wording, identify its exact original span and COPY. Locate fragments by `full`, `paragraph N`, `paragraphs N–M`, `line N` or `lines N–M`, counted within the coded entry, excluding headings and metadata. Count stored lines. Resolve ambiguous spans with short exact start/end quotations.

Apply the [provenance contract](provenance.md). Internal connections among a passage's arguments belong to this synthesis; connectors between distinct passages or sections belong to drafting.

## Completion condition

Every argument has one record row, every output span is reconstructable, all sources retain their scope and qualifications, and the candidate establishes exactly the approved passage claim.

## Blocking condition

Return a typed gap instead of prose when any completion check fails.

## Next owner

Predraft presents the candidate and complete record to the user.
