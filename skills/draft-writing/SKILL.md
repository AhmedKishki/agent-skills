---
name: draft-writing
description: Collaboratively plan and write an article under the user's explicit direction through source-grounded, passage-by-passage synthesis and approval.
---

# Draft writing

Empower the user to realise their thesis and vision while preserving human authorship and decision-making throughout the article.

## Governing collaboration

A **passage** is the article arc's single-claim compositional unit. It is developed and approved as one rhetorical unit independently of final paragraph boundaries. In the draft, one passage may form part of a paragraph, one paragraph, or multiple paragraphs.

The user decides the thesis, interpretation, source and fragment selection, structure, passage claims, supporting arguments, wording, final paragraph boundaries and final form. A substantive action changes meaning, interpretation, evidence selection, source use, a claim, an argument, order, a boundary, wording, qualification, structure or final layout. Present the exact proposed substantive action and wait for explicit user approval before adopting it.

Approval must refer unambiguously to the exact proposal or candidate presented. “Approve”, “approved”, “use this” or an equally explicit instruction tied to that object counts as approval. Silence, lack of objection and an ambiguous “continue” or “next” do not. Comments, questions and requested changes do not approve the object.

Mechanical actions are reading requested material, preserving supplied wording exactly, allocating IDs, applying an approved change exactly, formatting an approved object to a fixed schema, repairing references, and updating counters or tracker state. Perform them without a second approval unless intent, origin or correspondence is ambiguous.

Develop one passage at a time in arc order. Present every new or revised passage with its complete prose, compact provenance and full construction record. Wait for the user's decision before saving it as selected or developing the next passage. A gap blocks dependent work until its focused question is answered. A direct instruction to use exact prose approves only that exact prose; still present its construction record before saving it.

## Use

Read the [file standard](references/file-output-standard.md), [ownership rules](references/ownership-and-routing.md), [consent and state rules](references/consent-and-state.md), [provenance contract](references/provenance.md), [editing rules](references/editing-and-reference-integrity.md), and every task module affected by the request. On resumption, read the [tracker](references/activity-tracker.md), inspect its listed files and recover any pending candidate before acting on a later decision.

| Task | Required input | Module | Result |
|---|---|---|---|
| Establish direction | User commitments | [Thesis and vision](references/thesis-and-vision.md) | Approved governing direction |
| Preserve human language | User-authored article language | [User wording](references/user-wording.md) | Stable exact originals |
| Extract a source | Accessible source original and agreed scope | [Source maps](references/source-maps.md) | Approved coded excerpts |
| Design the argument | Approved direction | [Article arc](references/article-arc.md) | Approved sections, passages, arguments, comments and broad fragment inventories |
| Construct one candidate | Approved passage plan and limited approved input set | [White-box synthesis](references/white-box-synthesis.md) | Candidate with record, or typed gap |
| Develop raw material | Approved arc | [Predraft](references/predraft.md) | Approved raw passages with inline provenance |
| Create the article | Complete approved predraft | [Drafting](references/drafting.md) | Connected reader-facing draft |
| Check fidelity | Declared scope and available originals | [Fidelity audit](references/fidelity-audit.md) | Read-only findings |
| Record progress | Current workflow event | [Activity tracker](references/activity-tracker.md) | Exact resumption cursor |

Workflow: direction → user wording and source maps → article arc → passage-by-passage predrafting → connected draft → optional fidelity audit. Revisit an owner when the user requests a change or a gap requires one.
