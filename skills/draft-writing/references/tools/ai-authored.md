---
name: ai-authored.md
description: Fill identified gaps with explicitly requested and approved AI wording without making it a white-box input.
---

# AI-Authored Gap Filling

This tool supplies bounded wording for a gap that [white-box synthesis](white-box-synthesis.md) cannot fill. It does not supply missing evidence or replace the author's thesis. Read the local purpose, inputs, constraints and [decision rules](../rules/decisions.md).

## Request And Approval

1. Identify the exact gap and explain why eligible inputs cannot fill it. Offer author wording, further evidence work or an explicitly requested AI proposal. Wait for the choice before generating AI text; do not require the same permission again if it was already explicit.
2. Propose only the gap text and its destination. Mark every exact AI-authored span as `⟦AI-AUTHORED: exact wording⟧`. Identify authorship, purpose and evidence limits, not a fictitious white-box construction record.
3. Distinguish an interpretive connection from source findings. Do not invent facts, quotations, locators or citations. A connector cannot establish a causal relation absent from the evidence.
4. Obtain approval of the exact text and placement. Save only what was approved. A request for smoother prose or approval of a neighbouring paragraph is insufficient.

For a gap in section 1, the proposal names the local material passage or draft location and displays the complete marked text. It does not offer an unmarked alternative or label approval as Human authorship.

## Storage And Insertion

Approved marked text may appear in `material-section-n.md` and `draft-section-n.md`. Keep exact markers through saves, verbatim insertion, moves, smoothing review and final assembly. Human plus AI is Mixed; wholly AI wording is AI. Supporting evidence in Basis is not a claim that the source wrote the AI words. Keep live limits and dependent relations in the passage's Constraint.

Direct insertion means placing the already approved marked span at its approved destination without using it to generate other wording. If a complete passage combines eligible prose with an AI gap, show the white-box construction for eligible sentences and identify the marked insert separately. Do not describe the entire passage as a white-box result.

## Permanent Exclusion

AI-authored spans and relations dependent on them are permanently ineligible for white-box synthesis. Approval, copying, storage in material or surrounding Human wording never removes that exclusion. Ordinary eligible Mixed inputs remain usable; the label is not grounds to reject all surrounding text or to accept every span.

A changed AI span needs a fresh exact gap-text proposal and approval. Smoothing may propose deleting or relocating an unchanged marked span for its approved purpose, but may not transform it through white-box operations or repurpose it as a new input. Another section cannot borrow it.

Before completing, check exact approval, destination, markers, provenance and limits, then update local progress. In existing projects, preserve any stricter project rule that bars AI material; installing this skill does not change that rule.
