# White-box synthesis

Build one paragraph from supplied human wording. Return the paragraph and its construction record, or a precise gap.

## Inputs

- **Claim:** the single claim the paragraph must establish.
- **Sentences:** ordered sentence IDs and short propositions, including the intended relationships between them.
- **Fragments:** original codes (`user-n` or `src:A4`), exact human passages with their original span locations, relevant context, and permitted use: wording, evidence, user interpretation, or framework check.
- **Constraints:** the user's wording priorities, spelling convention, quotation requirements, and applicable conceptual limits.

The claim and sentence plan specify the target. Fragments supply the vocabulary and substantive basis. Original user wording supplies the paragraph's backbone; source passages supply the agreed additions.

## Algorithm

1. Match each planned sentence to the supplied fragments. Establish the basis for its proposition, qualifications, and relationship to adjacent sentences.
2. Build one sentence per ID, using the five operations below on meaningful contiguous spans. Keep every substantive word traceable to a supplied passage.
3. Assemble the sentences in the supplied order. Check the single claim, sentence relationships, and source qualifications against their original context.
4. Return **Paragraph**, **Used**, and **Construction** when all checks pass. Otherwise return **Gap**: the affected sentence ID, the missing wording or support, and one focused question requesting the required human contribution.

| Operation | Rule |
|---|---|
| COPY | Reproduce an exact contiguous original span with its necessary context. |
| INFLECT | Change only tense, number, grammatical case, article, or an unambiguous pronoun to a referent established in the same original passage. Preserve meaning, scope, modality, qualification, and emphasis. |
| NORMALISE | Correct unambiguous spelling or make meaning-neutral capitalization/punctuation changes under the supplied spelling convention. Preserve vocabulary and grammar. |
| ORDER | Arrange spans when original continuity or an explicit original user/source basis establishes their relationship. |
| DELETE | Remove equivalent repetition when subject, claim, scope, modality, and qualification match; retain the equivalent meaning. |

Apply INFLECT and NORMALISE to unquoted output. Keep direct quotations, saved originals, code, URLs, titles, and citation data exact. Preserve the spelling of proper names, trademarks, official names, and defined terms; adjust their capitalization only where unambiguous and meaning-neutral.

Every meaning-bearing join requires an explicit basis in the supplied human passages. Preserve a user's interpretation as their argument; treat source evidence as support only for what it establishes. Use framework-only inputs for fit checks. Return a gap when a required connection, unique deletion, substitution, or sentence-plan change exceeds the supplied basis and permitted operations.

## Output

```markdown
Paragraph: <complete paragraph>

Used:

- 1.1.1: user-21 (sentence 1); src:A4 — Service log.
- 1.1.2: user-21 (sentence 2).

Construction: <meaningful joins, transformations, evidence/framework use, and interpretive limits>
```

Give each output sentence one **Used** entry in the supplied order. Retain original fragment codes and name each source once. Mention paragraph-wide evidence or framework consultation in Construction, identifying any source used only there.

Identify spans only where needed: `full`, `sentence N`, `sentences N–M`, `paragraph N`, or `lines N–M`, counted from 1 within the original coded entry, excluding headings and metadata. Resolve ambiguous boundaries with short exact start/end quotations.

Keep **Construction** to the changes and limits needed to understand the result. For unchanged user prose, write `unchanged user wording`.
