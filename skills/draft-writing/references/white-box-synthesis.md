# White-box synthesis

Develop supporting arguments from supplied human wording and assemble one paragraph. Return the paragraph, a compact provenance summary and a full construction record, or a precise gap.

## Inputs

- **Claim:** the single claim the paragraph must establish.
- **Arguments:** ordered argument IDs and claims that together establish the paragraph's claim.
- **Fragments:** original codes (`user-n` or `src:A4`), exact human passages with their original span locations, relevant context, and permitted use: wording, evidence, user interpretation, or framework check.
- **Constraints:** the user's wording priorities, spelling convention, quotation requirements, and applicable conceptual limits.

The claim and supporting arguments specify the target. Fragments supply the vocabulary and substantive basis. Original user wording supplies the paragraph's backbone; source passages supply the agreed additions.

## Algorithm

1. Match each argument to the supplied fragments. Establish its claim, qualifications and contribution to the paragraph's claim.
2. Develop each argument as prose, using the five operations below on meaningful contiguous spans. Keep every substantive word traceable to a supplied passage.
3. Assemble the argument passages in the supplied order. Check that they jointly establish the paragraph's claim; verify connections and source qualifications against their original context.
4. Return **Paragraph**, **Provenance**, and **Record** when all wording and support checks pass. Otherwise return **Gap**: the affected argument ID, the missing wording or support, and one focused question requesting the required human contribution.

| Operation | Rule |
|---|---|
| COPY | Reproduce an exact contiguous original span with its necessary context. |
| INFLECT | Change only tense, number, grammatical case, article, or an unambiguous pronoun to a referent established in the same original passage. Preserve meaning, scope, modality, qualification, and emphasis. |
| NORMALISE | Correct unambiguous spelling or make meaning-neutral capitalization/punctuation changes under the supplied spelling convention. Preserve vocabulary and grammar. |
| ORDER | Arrange spans when original continuity or an explicit original user/source basis establishes their relationship. |
| DELETE | Remove equivalent repetition when subject, claim, scope, modality, and qualification match; retain the equivalent meaning. |

Apply INFLECT and NORMALISE to unquoted output. Keep direct quotations, saved originals, code, URLs, titles, and citation data exact. Preserve the spelling of proper names, trademarks, official names, and defined terms; adjust their capitalization only where unambiguous and meaning-neutral.

Every meaning-bearing join requires an explicit basis in the supplied human passages. Preserve a user's interpretation as their argument; treat source evidence as support only for what it establishes. Use framework-only inputs for fit checks. Return a gap when a required connection, unique deletion, substitution, or argument-plan change exceeds the supplied basis and permitted operations.

## Output

```markdown
Paragraph: <complete paragraph>

**Provenance:** Mixed · Human wording: 100% · Method: white-box synthesis · Basis: A4, user-21, user-22

Record:

| Argument | Result span | Original fragments | Construction and support |
|---|---|---|---|
| 1.1.1 | <exact output passage> | <codes, locators and exact human spans> | <operations in order, source support and limits> |
| 1.1.2 | <exact output passage> | <codes, locators and exact human spans> | <operations in order, source support and limits> |
```

Give each argument one record row and cover the complete paragraph. Quote every exact fragment used, identify its original code and location, and name each source once. Show the order of operations and every join, cut or grammatical change needed to reconstruct the result. Explain what the evidence establishes and what remains the user's interpretation. Include the context needed to judge qualifications. State any paragraph-wide evidence or framework consultation after the table.

For unchanged wording, identify its exact original span and COPY. Locate fragments by `full`, `paragraph N`, `paragraphs N–M`, `line N` or `lines N–M`, counted within the coded entry, excluding headings and metadata. Count stored lines. Resolve ambiguous spans with short exact start/end quotations.

Derive the provenance from the verified inputs and operations: distinguish unchanged human wording from assistant composition, and list the actual basis codes once. A result built entirely from verified human originals through the permitted operations has `Human wording: 100%`; unresolved wording returns a Gap.
