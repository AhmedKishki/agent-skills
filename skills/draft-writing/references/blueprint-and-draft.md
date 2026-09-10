# Blueprint and draft

## Purpose

Build a versioned blueprint through critical discussion, then produce a finalised uncited draft one section at a time. The agent analyses and asks; the user decides.

## Inputs

The current thesis-and-vision, user wording, approved article arc, complete approved predraft, required source maps, [authorial voice](authorial-voice.md) and tracker. Blueprinting requires no word-count target, limit, projection or section budget unless the user supplies one.

## Blueprinting

1. Verify the inputs and list the article-level, section-level and fragment-level decisions needed to draft without substantive guessing.
2. Ask one focused critical question at a time. Quote or link the exact material, explain why a decision is needed, and state the consequences of genuine alternatives. The user may reject every alternative.
3. Route every answer through [ownership and routing](ownership-and-routing.md). Record only reader-facing selection, placement, treatment, boundaries and connections in `{project}-working-blueprint.md`; link to other owners.
4. After each decision, update the working blueprint and tracker. Identify selected material by passage, argument or exact opening and closing words. An open question gives no drafting authority.
5. Continue until the blueprint settles the proposition, reader-facing structure, treatment and destination of every predraft passage, order, section functions, paragraph plan, required relations, protected wording and qualifications, and section drafting order.
6. Present the complete working revision and ask: **“Do you approve blueprint revision WB-rN for finalisation as blueprint vN, or what should change?”** After approval, copy it unchanged to `{project}-blueprint-vN.md` with `Status: Approved`, `Version: vN` and `Finalised from: WB-rN`.

Questions may ask whether a section is needed, which claim organises it, whether an example performs a distinct function, what enters or leaves the draft, where material belongs, what connects two parts, where a paragraph ends, or which wording must survive.

## Blueprint output

```markdown
# Working blueprint

Status: Working | Awaiting approval
Revision: WB-rN
Current approved version: None | blueprint-vN.md
Basis: <thesis-and-vision, user wording, arc and predraft links>

## Article proposition
<Decisions>

## Draft structure
### 1 — <working heading>
- **Function:** <one exact contribution>
- **Material:** <passages, arguments or bounded fragments>
- **Treatment:** <include, develop, condense, combine, relocate or omit, with exact scope>
- **Paragraph plan:** <material and function of each paragraph>
- **Opening and close:** <decided movement>
- **Connection:** <exact relation to the next section>
- **Protected:** <wording, force and qualifications>
- **Open:** <question or None>

## Predraft treatment
| Material | Destination | Treatment | Function or consequence | Status |
|---|---|---|---|---|

## Required relations
| From | To | Relation | Basis | Wording status |
|---|---|---|---|---|

## Open questions
<Questions or None>
```

Approved versions are immutable. Develop a later substantive change in the working blueprint, present the complete revision, save the approved next version, and invalidate only affected draft sections.

Working blueprint states are `Working`, `Awaiting approval` and `Blocked`. A version exists only after approval and has `Status: Approved`.

## Section drafting

1. Work in the approved blueprint's order, one complete section at a time.
2. Before prose, present the section's blueprint requirements, selected fragments, available user wording, required relations and unresolved needs. Ask one focused question at a time until no substantive guess remains.
3. Route and preserve each answer. Reopen the blueprint when an answer changes selection, structure, order, emphasis, treatment, boundaries or a relation.
4. Apply [authorial voice](authorial-voice.md). AI-authored article wording is prohibited unless the user approves the exact proposed span for the identified need.
5. Save the current candidate in `{project}-working-draft.md`. Present its complete prose, `S<section>-rN`, governing blueprint version, bases, realised requirements, approved AI wording and conformance result. Ask: **“Do you approve section candidate S<section>-rN, reject it, or what should change?”**
6. Save only exact approved prose. Do not draft the next section while the current section awaits a decision.
7. After all sections are approved, assemble them without adding or revising prose. Validate the article as a whole, present the complete working revision and ask for exact approval.
8. After approval, copy it unchanged to `{project}-draft-vN.md` with `Status: Finalised`, `Version: vN` and its governing blueprint version. This uncited file is the sole input to [article citation](article-citation.md).

Section states are `Unstarted`, `Questions open`, `Candidate awaiting decision`, `Revision requested`, `Rejected`, `Approved and saved` and `Invalidated`. Complete working-draft states are `Assembling`, `Awaiting approval` and `Blocked`. A changed candidate receives a new revision.

## Draft output

```markdown
# <Article title>

<Approved sections in blueprint order; current candidate only when clearly marked unapproved.>

---

# Process appendix — outside the article

Status: Working | Assembling | Awaiting approval | Blocked
Revision: WD-rN
Blueprint: blueprint-vN.md
Current section: <number | None>
Current candidate: S<section>-rN | None

| Draft section | Blueprint section | Predraft material | Approved AI wording |
|---|---|---|---|
```

For `{project}-draft-vN.md`, replace the process status with `Status: Finalised`, add `Version: vN`, and remove every unapproved candidate. Keep process metadata outside the article.

## Validation

Verify every predraft passage has one explicit treatment; every included fragment has an approved destination and function; every omission, condensation, boundary, order and relation is approved; every section matches the governing blueprint; every section candidate is approved; assembly added no prose; voice and qualifications remain; every AI-authored span has exact approval; and all mappings resolve.

## Blocking condition

A missing decision, relation, wording basis, approval or required file blocks affected work. An omission, ambiguity, house convention or preference for smoother prose never grants discretion.

## Completion condition

Blueprinting completes with an approved immutable blueprint version. Drafting completes when the user approves the exact assembled prose and it is saved as an immutable finalised draft version.