---
name: plan.md
description: Own article-level section order, purposes, drafting sequence and the current-section link.
---

# Article Plan

Keep article section order, each section's brief contribution, the agreed drafting and review sequence, and one current-section link in `organisation/plan.md`. Read the thesis and requirements before proposing changes. Use [decisions](../rules/decisions.md); placement does not establish a claim or approve prose.

```markdown
# Plan

## Article Order
1. [Section 1](../sections/section-1/arc-section-1.md): <Brief article-level purpose.>
2. [Section 2](../sections/section-2/arc-section-2.md): <Brief article-level purpose.>

## Drafting Sequence
<Agreed sequence and any author-directed deferral of review.>

## Current Section
[Section 1](../sections/section-1/progress-section-1.md)
```

Link only to files that exist. Until an arc exists, use its planned path as inline code, not a broken link. Omit the current-section field until a section has been selected. Passage order belongs in the section arc; status, next actions and blockers belong in its progress file. Do not copy those records, material or per-section status tables here.

Plan only enough to give current work a destination. If the user requests section-level planning only, stop there; do not force passage planning. Section arcs can be developed later.

Section numbers are stable identities, not reading-order positions. Reordering sections changes this list, not directory names or IDs. Choose a never-used section number when creating a section; check current files and Git if necessary. Merges, splits and content transfers require an exact separate proposal, not automatic renumbering or cross-section reuse.

Before any section exists, a pending setup question may retain the unresolved placement question and only the exact text needed to settle it. Remove it on resolution. This bounded exception is not a material store or global handoff.

After an approved change, check links and affected section boundaries. Update the current-section link only when work focus changes; leave detailed handoffs local.
