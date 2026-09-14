# Argument formation

## Purpose

Define the unordered claims the article may need to establish in the arguments file family.

## Argument contents

Each `ARG-nnn` contains only:

- one claim;
- essential qualifications;
- dependencies on other arguments;
- status.

Do not store source excerpts, user quotations, synthesized prose or article placement here. File order has no article meaning.

Use one short index at `{project}-arguments.md` and bounded range files under `arguments/`, such as `arguments/{project}-arguments-001-025.md`. Add a new range before an existing range becomes difficult to review. Do not copy a claim into both its heading and body: use a short heading and state the claim once.

Keep only claim-specific qualifications with an argument. Put article-wide writing rules in draft direction and structural or passage-level constraints in the article arc. Link to a shared governing rule instead of repeating it across arguments.

## Procedure

1. Form one claim from the approved thesis, user interpretation or a gap exposed by later work.
2. Separate claims that require different evidence or could be accepted independently.
3. Present the exact ID, claim, qualifications and dependencies.
4. Ask whether the user approves that argument or what should change.
5. Save only the approved definition in its range file and add its ID and short name to the index.
6. If a changed argument affects an argument draft or article-arc use, mark those dependants for review.

## Format

```markdown
# Arguments 001–025

> **Editing note:** You may edit this file directly. Arguments are unordered; moving them does not change article order.

## ARG-001

**Status:** Approved

### Claim

<One claim.>

**Qualifications:** <Essential claim-specific limit. Omit when none.>

**Depends on:** ARG-002 <Omit when none.>
```

## Completion

The claim, claim-specific qualifications and actual dependencies are explicit and approved. The index resolves the ID to one range file. Prose synthesis is a separate stage.