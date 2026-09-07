# Predraft

Assemble approved raw material according to the article arc, one paragraph at a time. Save it in `{project}-predraft.md`.

## Paragraph loop

1. Read the target paragraph's accepted claim, supporting argument claims, governing section claim or question, and thesis requirements. Ask the user to resolve any open structural decision.
2. Propose relevant sources and exact user/source fragments for each argument. Resolve codes through their originals; supply context and the proposed use of each fragment.
3. Run [white-box synthesis](white-box-synthesis.md) with the paragraph Claim, its ordered Arguments, Fragments and Constraints. Synthesis develops each argument and assembles the paragraph.
4. For a Gap, show the precise question and wait. Route the user's answer to its owner, then retry.
5. For a result, show the complete paragraph, its Used list and Construction account. Ask: **“Do you approve this paragraph, or what should change?”** Wait for explicit approval or comments.
6. Incorporate the user's comments. When feedback or a gap calls for changing a claim, argument, order or paragraph boundary, present the proposed arc change and wait for explicit approval. Apply the accepted arc change and reconcile references through the shared editing rules, then repeat synthesis against the revised plan. Present revised prose for its own approval; save the exact selected paragraph and record.
7. Proceed to the next paragraph in the agreed arc order and repeat this loop.

Keep the current candidate in the response until selected. Record the pending paragraph and question in the tracker for resumption. Recover or re-present that exact candidate before acting on a later approval.

A batch request establishes the scope; each paragraph still receives its own synthesis presentation and explicit selection. A direct instruction to use an exact user-written paragraph supplies its selection, after showing the unchanged wording and verifying its bases.

## Output

Use exactly two H2 parts. Part 1 uses H3 section headings and H4 paragraph headings. Part 2 uses H3 paragraph records.

```markdown
# Predraft

## Part 1 — Selected prose

### 1 — Human work

#### 1.1 — Prose

Reviewers check flagged results every day. Daily review keeps the service running.

## Part 2 — Construction records

### 1.1 — Record

Arc: [1.1](demo-article-arc.md#11--human-review-sustains-the-service)

Used:

- 1.1.1: user-21; src:A1 — Service log.
- 1.1.2: user-22.

Construction: A1 supplies “every day”; argument 1.1.2 is the user's interpretation.

Selection: User approved this exact paragraph.
```

Use the actual synthesis result. Keep fields in the order **Arc, Used, Construction, Selection**. Used maps each section.paragraph.argument number to its realised prose and original `user-n` / `src:A1` fragments. Identify ambiguous spans with the synthesis module's locators. Construction records meaningful operations, actual evidence or framework use, and limits briefly. Selection records exact consent.

Keep one current selected paragraph per arc target. Preserve earlier originals needed by its record in their wording/source owners. Present requested alternatives in the conversation for the user's choice.

## Titles and headings

Use exact user wording, or an explicitly requested exact source heading. Present the wording and origin for selection. Allocate stable `H01` IDs from the predraft row's heading counter.

Put an article title at `### H01 — Prose` before Part 1's sections; put a section heading at `#### H02 — Prose` within its section. Use matching Part 2 records. Arc specifies `article title` or `section 1 heading`; Used has one entry under the heading ID. This record owns reader-facing placement.

## Check and save

Verify that every planned argument is realised in order and the complete prose is covered by Used. Check that the arguments establish the paragraph claim and the paragraphs establish their section's claim or answer its governing question. Check original wording, source scope, joins, links and exact approval. Save prose and record together, then update the tracker.

Preserve direct edits and ask about uncertain selection or changed meaning. Resolve missing human wording through user wording or source work before presenting a replacement.
