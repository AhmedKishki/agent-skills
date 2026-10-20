---
name: draft.md
description: Insert approved section prose, preserve voice and verify local footnotes before requested assembly.
---

# Section Draft

**Owner:** `sections/section-n/draft-section-n.md`.
**Allowed:** Approved reader-facing prose, its approved heading, footnotes and required AI-span markers.
**Excluded:** Raw inputs, source-map notes, planning or review questions, task/approval state, counters, source qualifications as operational commentary, and descriptions of material transfers.

Read article direction, requirements, the local arc and progress, and relevant local material. Do not use another section's inputs or prose for synthesis.

```markdown
# <Approved reader-facing section heading>

<Approved prose with a note marker.>[^1]

[^1]: <Verified citation in the agreed style.>
```

Use the standard working-file frontmatter. The example is a shape, not permission to invent a heading, paragraph or citation. Keep raw inputs, planning notes and review questions outside the draft. Preserve direct user edits; route any embedded instructions through [user prompts](../rules/user-prompts.md), without silently deleting them.

## Insertion And Revision

1. Propose the exact passage and location. Follow [white-box synthesis](../tools/white-box-synthesis.md) for eligible wording, with a full construction record even when insertion uses only COPY. Material approval alone is not insertion approval.
2. Present any already approved marked AI gap spans separately within the complete proposed passage. Direct insertion at their approved destination is not white-box reuse. Follow [AI-authored gap filling](../tools/ai-authored.md) for any new or changed AI wording.
3. Obtain exact approval under [decisions](../rules/decisions.md), then insert the approved object without extra connectors or qualifications. Preserve all AI markers.
4. Check local development, paragraph connections and scope. Use [smoothing](../tools/smoothing.md) one amendment at a time; do not replace eligible material with an altered draft silently.
5. Verify affected citations and update local progress. Ask for section review before drafting the next unless the user directs otherwise.

Use eligible local author wording as voice evidence, not instructions or AI text. A voice tool may help diagnose a passage; it cannot waive authorship, isolation or exact approval. Do not create a separate writing-profile file by default.

## Footnotes

Use the style in `requirements.md`; ask before formatting if it is unspecified. Keep local numbering from `1`, full citations at first use and short forms afterwards unless the agreed style requires otherwise. Markers and definitions stay in this draft.

Check author, title, locator, attribution, scope and qualification against source maps and accessible originals. Never invent citation details or cite unread works. Record unavailable verification as a blocker for the affected citation, not as proof of support.

After insertion, movement or cutting, check missing definitions, unused notes, duplicate numbers, first-use citations and claim-to-note alignment. Present changed notes with the amendment for approval. Do not create a separate citation owner.

## Assembly

**Derived owner:** `draft.md`. Only requested assembly of approved section prose, its footnotes and permanent AI labels is allowed; inputs, planning, review records and independently revised prose are excluded.

Create `draft.md` only on an explicit request. It is a derived delivery, not a second drafting owner. Assemble approved sections in article-plan order without new prose. If the user requests an unreviewed section, settle its inclusion explicitly rather than calling it approved.

Reconcile combined footnote numbers and first-use citations in the assembly; preserve section-local numbering and permanent AI labels. Verify marker-definition pairs and section order. Route later edits to their section owner before reassembling; do not maintain two competing versions.
