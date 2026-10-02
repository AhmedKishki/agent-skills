---
name: source-maps.md
description: Share approved exact source quotations with verified identity, locators and local excerpt IDs.
---

# Source Maps

Keep one source's identity and approved exact excerpts in `sources/source-maps/<author-title>.md`. Sections share this evidence, not each other's synthesis. Read article direction, research requirements and the active passage's evidence need before selecting excerpts.

## Mapping

1. For a new question, use the project's configured corpus discovery. For a mature question, start with existing maps and audit for omissions and counterevidence. Follow project settings, not a tool or search count built into this skill.
2. Report retrieval failures and their limits honestly. Never claim a failed search confirmed a passage. Ask about an alternative verification route when needed; do not ingest or change source inclusion without permission.
3. Verify source identity, wording and locators against the original. Search snippets and extracted text are provisional, not quote-safe or approved inputs. A quotation pasted by the user is still source-authored.
4. Select contiguous spans preserving subject, scope, modality and qualification. Disclose meaning-neutral transcription normalisation. Reopen the original if context is insufficient or the intended use changes.
5. Present the exact excerpt batch for approval, then save approved excerpts in source order. Mapping approval does not approve a material passage, synthesis or insertion.

## File Shape

```markdown
# <Author, Full Source Title>

**Original:** <Original file or stable URL.>
**Citation:** <Verified bibliographic details needed for citations.>
**Next excerpt:** EXCERPT-002

## EXCERPT-001
<Short topic.>

**Location:** Printed p. 12; PDF p. 15, <section title>.

> <Exact approved source wording.>
```

Use only actual bibliographic and locator data. EPUB or unpaginated sources need a stable chapter, section or equivalent locator, not an invented page. Omit absent fields; record a necessary missing detail as an active blocker in section progress. A map contains no article interpretation, section usage log or approval history.

## Identity And Corrections

Choose the stable author-title filename from verified identity. Distinguish a collision with a verified year or edition; ask if still ambiguous. No global source-code register is needed. Do not automatically rename an established map when correcting its title.

The full excerpt identity is map path plus ID, for example `sources/source-maps/author-title.md#excerpt-001`. Use ID-only headings, titles beneath them, and the map's own next-excerpt counter. Advance the counter on allocation, including rejected selections. Never reuse retired numbers; reread before allocation, check Git when uncertain and resolve concurrent collisions without overwriting.

A verified transcription or locator correction retains its ID; a different selection, split or merge receives a new ID. Propose the exact correction for approval. Then search for affected references and inspect only their uses; record unfinished reviews in each affected section's progress. Do not silently rewrite other sections or treat their material as reusable input. Finish by checking exact wording, locators, counter and links.
