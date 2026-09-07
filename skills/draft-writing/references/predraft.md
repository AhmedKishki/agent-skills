# Predraft

Assemble approved raw material according to the article arc, one paragraph at a time. Save it in `{project}-predraft.md`.

## Paragraph loop

1. Read the target paragraph's accepted claim, sentence plan, surrounding handoffs and thesis requirements. Ask the user to resolve any open structural decision.
2. Gather exact user wording and source excerpts for that paragraph. Resolve codes through their originals; supply context and the proposed use of each fragment.
3. Run [white-box synthesis](white-box-synthesis.md) with Claim, Sentences, Fragments and Constraints.
4. For a Gap, show the precise question and wait. Route the user's answer to its owner, then retry.
5. For a result, show the complete paragraph, its Used list and Construction account. Ask: **“Do you approve this paragraph, or what should change?”** Wait for explicit approval or comments.
6. Incorporate comments into a revised candidate and repeat the check. On approval, save the exact prose and record below.
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

Arc: [1.1](demo-article-arc.md#11--review-sustains-service)

Used:

- 1.1.1: user-21 (sentence 1); src:A1 — Service log.
- 1.1.2: user-21 (sentence 2).

Construction: A1 supplies “every day”; the second sentence is the user's interpretation.

Selection: User approved this exact paragraph.
```

Use the actual synthesis result. Keep fields in the order **Arc, Used, Construction, Selection**. Used maps every prose sentence to its original `user-n` / `src:A1` fragments under the matching section.paragraph.sentence number. Construction records meaningful operations, actual evidence or framework use, and limits briefly. Selection records exact consent.

Keep one current selected paragraph per arc target. Preserve earlier originals needed by its record in their wording/source owners. Present requested alternatives in the conversation for the user's choice.

## Titles and headings

Use exact user wording, or an explicitly requested exact source heading. Present the wording and origin for selection. Allocate stable `H01` IDs from the predraft row's heading counter.

Put an article title at `### H01 — Prose` before Part 1's sections; put a section heading at `#### H02 — Prose` within its section. Use matching Part 2 records. Arc specifies `article title` or `section 1 heading`; Used has one entry under the heading ID. This record owns reader-facing placement.

## Check and save

Verify one selected prose sentence per arc sentence and per Used entry, in order. Check original wording, source scope, joins, links and exact approval. Save prose and record together, then update the tracker.

Preserve direct edits and ask about uncertain selection or changed meaning. Reconcile an accepted structural change with the arc and all affected numbering. Resolve missing human wording through user wording or source work before presenting a replacement.
