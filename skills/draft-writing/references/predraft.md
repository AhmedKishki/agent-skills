# Predraft

Assemble approved raw material according to the article arc, one paragraph at a time. Save it in `{project}-predraft.md`.

## Paragraph loop

1. Read the accepted paragraph claim, supporting arguments, governing section claim or question, and thesis requirements.
2. Propose relevant sources and exact user/source fragments for each argument. Resolve their originals and context.
3. Run [white-box synthesis](white-box-synthesis.md) with Claim, Arguments, Fragments and Constraints.
4. For a Gap, ask its precise question and wait. Route the answer to its owner, then retry.
5. Present the complete paragraph, its provenance line and the full synthesis record: exact fragments, argument coverage, ordered operations, support and limits. Ask: **“Do you approve this paragraph, or what should change?”** Wait for explicit approval or comments.
6. Apply the user's comments. For a changed claim, argument, order or boundary, obtain explicit approval of the proposed arc change, update its references through the shared rules, then repeat synthesis. Present the revised prose and full record for approval.
7. Save the exact selected prose and compact provenance, then proceed to the next paragraph.

Keep the unselected candidate and full record in the conversation, with the pending decision in the tracker. Recover or re-present the exact candidate before acting on a later approval. A batch request still requires each paragraph's presentation and selection. A direct instruction to use exact user prose supplies consent for that unchanged passage.

## Saved output

Use two H2 parts. Part 1 has H3 sections and H4 selected paragraphs. Part 2 has one H3 provenance record per paragraph.

```markdown
# Predraft

## Part 1 — Selected prose

### 1 — Human work

#### 1.1 — Prose

Reviewers check flagged results every day. Daily review keeps the service running.

## Part 2 — Provenance

### 1.1 — Record

**Provenance:** Mixed · Human wording: 100% · Method: white-box synthesis · Basis: A1, user-21, user-22
```

Apply the [compact provenance rule](file-output-standard.md#compact-provenance). The paragraph number identifies its arc target. Part 1 contains only exact user-selected prose; its matching record keeps the source trail. Retain a short `Use:` note only when a material interpretation limit or scoped permission would otherwise be lost. The full construction record belongs to the approval presentation.

Keep one current selection per paragraph. Present alternatives in conversation. Preserve original passages needed to reconstruct selected prose in their source/user-wording owners.

## Titles and headings

Present exact user wording, or an explicitly requested exact source heading, for selection. Allocate stable `H01` IDs from the predraft row's heading counter.

Put an article title at `### H01 — Prose` before Part 1's sections, or a section heading at `#### H02 — Prose` before that section's paragraphs. This position owns its placement. Give it a matching Part 2 record containing the same compact provenance format.

## Check and save

Before selection, verify that the full synthesis record covers every argument and the complete prose. Check that arguments establish the paragraph claim and paragraphs establish their section claim or answer its question. Verify original wording, source scope, joins and explicit consent.

After saving, check that the listed bases resolve and can support a feasible reconstruction through permitted operations. Preserve direct edits; resolve uncertain origin or changed meaning with the user before further synthesis.
