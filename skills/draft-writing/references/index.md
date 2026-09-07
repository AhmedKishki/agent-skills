# Source index

Maintain retrieval labels in `{project}-source-index.md`, derived from current source maps.

1. Ask the user for retrieval priorities when unspecified.
2. Propose a small set of keywords and excerpt assignments; obtain approval before adopting new labels or interpretive groupings.
3. Save accepted labels. After map changes, repair references and present any newly needed assignments.
4. Verify every active excerpt is reachable and every code resolves.

## Output

```markdown
# Source index

| Keyword | Excerpts |
|---|---|
| Human review | src:A1 |
```

When requested or accepted, append `## Themes` with a `Theme | Keywords` table.

Keep excerpt text in maps. Use `src:A1` references; retrieve their exact text and context from the map before proposing an article use. Preserve user-edited labels and organisation.
