---
name: arguments.md
description: Defines argument formation and the record of current arguments and their bases.
---

# Arguments

## Accepts

Candidate claims, qualifications, counterarguments and connections inferred from source maps, user material, direct user requests, the thesis, existing arguments, the plan or problems exposed during drafting.

Inference identifies a candidate; it does not authorize the argument. Do not accept article order, synthesized passages, unsupported AI claims, broad source inventories or superseded arguments.

## Owns

`{project}-arguments.md` owns every current argument, its substantive relation to the thesis, its qualifications and dependencies, and the complete limited basis authorized for it.

## Standard structure

```markdown
---
name: "{project}-arguments.md"
description: Records current arguments, their thesis relations and their authorized bases.
---

# Arguments

## ARG-001 — <Current argument>

**Relation to thesis:** <The specific support, premise, development, qualification, complication or challenge.>

### Basis

- U-003 — <Contribution and limit when needed.>
- A4 — <Contribution and limit when needed.>
- ARG-002 — <Dependency and exact authorized use when needed.>

### Qualification

<Only when it limits the argument.>

### Contradiction

<Only while a real unresolved conflict blocks or qualifies use.>
```

Each argument has one monotonic `ARG-nnn` ID, one independently assessable claim, one real thesis relation, and a basis. Include only other sections that carry information. File order does not establish article order.

## Formation procedure

1. Examine current authorized inputs for a claim the article needs, including relations or gaps exposed by another argument, the plan or drafting.
2. Distinguish one independently assessable argument from its evidence, wording, qualifications and placement.
3. Reconstruct the candidate claim, thesis relation, qualifications and dependencies separately from authorised eligible inputs through white-box synthesis.
4. If any part cannot be reconstructed, identify its smallest exact gap, show why provenance-preserving operations cannot fill it and ask the user to supply or resolve it. Do not originate an AI-authored argument or volunteer AI wording; the user may explicitly request a separate AI suggestion.
5. Select a complete limited basis. Relevant user material is included when present; exclusion requires explicit user authorization.
6. State each input's contribution and limit when either is not evident from the argument.
7. Resolve contradictions among the candidate, thesis, user material, sources and existing arguments, or record the live blocker.
8. Present the candidate argument, thesis relation, complete basis and accurate Human or Mixed provenance together for explicit approval. Classify any output using a Mixed input as Mixed.
9. Save only the approved current argument. Update affected material, plan and draft uses when it changes.
10. Never reuse a removed or retired argument or contradiction ID; allocate the next historical value from progress.

## Prompt routing

Route each independent part of a user prompt once:

- a current aim, thesis, question, orientation or article-wide requirement goes to thesis;
- exact reusable user wording goes to user material;
- a claim, qualification, counterargument, connection or request to form an argument goes to arguments.

One prompt may supply independent parts to more than one owner. Preserve exact wording in user material and link it from the argument rather than duplicating it. A source quotation remains source-authored and goes to source mapping. Procedural requests are executed rather than stored as article material. If a unit could belong to incompatible owners, ask one focused question.

## Completion

The argument and complete limited basis are approved together, the thesis relation is substantive, provenance and limits are recoverable, and affected downstream work is current.