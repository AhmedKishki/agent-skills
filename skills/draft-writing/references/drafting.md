# Drafting

## Purpose

Transform the approved raw predraft into a connected reader-facing article by collaboratively determining connectors, headings, final paragraph boundaries, citations and assembly.

## Inputs

The approved thesis and arc, a predraft containing every in-scope approved passage with inline provenance, user wording, required source maps and the tracker.

Drafting may begin only when every in-scope passage is approved and saved, none is invalidated, every provenance basis resolves and no blocking passage question remains.

## Procedure

1. **Load and verify.** Read every input, preserve direct user edits and verify the preconditions.
2. **Propose layout.** Present the title, reader-facing headings, passage order, proposed paragraph boundaries, passages combined in one paragraph, passages split across paragraphs, required inter-passage and inter-section connectors, and citation placement. Identify every passage by ID and obtain approval of the exact layout.
3. **Develop connectors.** For one required connector at a time, identify the passages or sections connected and the exact relation to express. Present proposed wording, provenance and construction; ask for approval or comments and wait. Assign approved connectors stable IDs `C01`, `C02` and onward.
4. **Assemble.** Preserve approved passage wording, insert only approved connectors, apply approved paragraph boundaries and headings, and add mechanical citation formatting.
5. **Validate.** Verify that every predraft passage appears completely, no passage meaning changed, every connector was approved, every basis resolves, paragraph boundaries preserve meaning, order is approved, citations remain in scope, and length and form meet the thesis specifications.
6. **Present.** Show the complete article and ask for final approval or comments.

Route a wording problem to predraft; a claim, order or boundary problem to the arc and then predraft; a missing human transition to user wording and then connector development; an evidence problem to source maps and then predraft; and a substantive cut or combination to the arc and predraft. Drafting must not silently solve these problems.

## Output

Save `{project}-draft.md` with reader-facing prose first. Append:

```markdown
---

# Process appendix — outside the article

Status: Working
Basis: [Direction](demo-thesis-and-vision.md); [Arc](demo-article-arc.md); [Predraft](demo-predraft.md)

| Draft location | Predraft passage or approved connector |
|---|---|
| Section 1, paragraph 1 | [Passages 1.1 and 1.2](demo-predraft.md#11--human-review-sustains-the-service) |
| Section 1, paragraph 2 | Passage 1.3, first part |
| Section 1, paragraph 3 | Passage 1.3, second part; connector C01 |
```

If one paragraph contains multiple passages, list each passage. If one passage spans multiple paragraphs, list it in every affected row and identify the part by exact opening and closing words. Record every connector ID, exact approved wording, compact provenance and construction after the mapping table. Keep process metadata outside the reader-facing article.

Mark the exact article `Approved` when the user accepts it and `Complete` only when the user declares it finished. Route later substantive comments to their owners and re-present every changed passage or connector before updating the article.

## Completion condition

The user has approved the complete connected article; every passage and connector maps to its approved basis; and final paragraph boundaries and citations pass validation.

## Blocking condition

An incomplete or invalidated predraft, unresolved basis, unapproved connector or unapproved layout blocks assembly or final approval.

## Next owner

The user for final approval, or the module that owns a requested correction.
