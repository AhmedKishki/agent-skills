---
name: coding-partner
description: >-
  Explain existing code chunk by chunk, document necessary design decisions, and
  collaboratively engineer minimal sufficient, human-readable code under
  user-defined architecture, design, and style constraints. Use when the user
  requests a coding partner, white-box
  programming, a chunk-based code walkthrough, or collaborative coding focused
  on readability, explainability, and avoiding unnecessary complexity.
---

# Coding Partner

- Keep the code a white box: the user can understand its mechanisms, assumptions, and structure.

## Code model

- A chunk is coherent behaviour explainable using a small, explicit contract for its dependencies. Identify its inputs, outputs, relevant side effects, and failure behaviour.
- A segment combines chunks and references into a larger operation.
- A fragment is a reference to behaviour implemented elsewhere, such as a function call. Explain its contract; expand its implementation when that mechanism is necessary to understand the current chunk.
- These are explanatory roles, not fixed language constructs. A function can be a chunk in one explanation and a segment in another.
- Choose boundaries by meaningful behaviour, not line counts. Do not refactor existing code merely to make it fit this model.

## Entry point and functions

| Module | Function | Read |
|---|---|---|
| [Collaboration](references/collaboration.md) | Establish the goal, constraints, and working agreement. | First, when starting or resuming work. |
| [Code quality](references/code-quality.md) | Assess readability, necessary complexity, and sufficiency. | Before assessing existing design or proposing code. |
| [Reverse-engineering](references/reverse-engineering.md) | Explain existing code one chunk at a time. | When explaining existing code. |
| [Documentation](references/documentation.md) | Document file operation and necessary design decisions. | Before writing or assessing code documentation, or proposing source changes. |
| [Engineering](references/engineering.md) | Propose, approve, apply, and verify changes. | Before proposing or applying code or documentation changes. |

- Load only the modules needed for the current request, following the reading conditions above.
