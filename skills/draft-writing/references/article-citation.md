# Article citation

## Purpose

Verify and cite claims in a finalised article without changing its argument or prose, using New Left Review footnote style.

## Inputs and precondition

Begin only from an immutable `{project}-draft-vN.md` with `Status: Finalised`, created after the user's approval of its exact complete prose. Never cite `{project}-blueprint-working.md`, `{project}-draft-working.md` or a section candidate. Load the finalised draft, approved blueprint, predraft provenance, source maps, accessible originals, publication requirements and tracker. Cite only works the author has read.

## Procedure

1. Identify each claim requiring support and its exact draft location. Distinguish source evidence from user interpretation.
2. Recover and check the original, locator, scope, date, modality and qualifications. The source must support the claim as written.
3. If support fails, report the exact defect and stop that item. Do not revise finalised prose. An approved correction returns to [blueprint and draft](blueprint-and-draft.md), creates a new finalised draft version, and restarts citation from that version.
4. In `{project}-citation-working.md`, present each exact footnote and marker location for explicit approval. Separate attribution from parenthetical or tangential content; identify every substantive note span.
5. Apply only approved markers and notes without changing the prose. Renumbering and approved house-style formatting are mechanical.
6. Validate every marker, note, source, locator and qualification. Present the complete cited article for approval, then save the exact approved version as `{project}-cited-draft-vN.md`, naming its source draft.

## New Left Review style

Use bottom-of-page footnotes to clarify sources or add useful parenthetical or tangential ideas, not unnecessary bibliography. Refrain from self-citation. Preserve these forms and punctuation:

- Susan Woodward, *Balkan Tragedy: Chaos and Dissolution after the Cold War*, Washington, DC 1995, pp. 28–9.
- Fredric Jameson, ‘Marx’s Purloined Letter’, in Michael Sprinker, ed., *Ghostly Demarcations*, London 1999, p. 51.
- Lorna Sage, ‘The First Bacchante’, *London Review of Books*, 29 April 1999.
- Brenner, ‘The Best of Times, The Worst of Times: US Feminism Today’, *NLR* I/200, July–August 1993, pp. 156–7.

Use en dashes in page ranges. Book reviews carry no footnotes; this exception applies only when the article is a book review.

## Working output

```markdown
# Citation working file

Status: Working | Awaiting approval
Source draft: draft-vN.md

| ID | Draft location | Claim | Source and locator | Support and limits | Proposed footnote | State |
|---|---|---|---|---|---|---|
```

Use `Unstarted`, `Blocked`, `Proposed`, `Approved`, `Applied` or `Invalidated`. Record approval of each exact note and marker; link to source maps instead of duplicating excerpts.

## Completion condition

Every claim requiring support has a verified approved note or an explicit user-approved reason for none; every note follows NLR style; cited prose exactly matches the source draft; and the user has approved the complete cited version.

## Blocking condition

A non-finalised draft, inaccessible required original, unread work, support defect, unapproved substantive note or source-draft mismatch blocks affected citation work.