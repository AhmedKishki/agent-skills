# Activity tracker

Maintain `{project}-activity-tracker.md` as the file inventory, allocation checkpoint and resumption point. Update it after a coherent save or a change in the pending question.

## Output

```markdown
# Activity tracker

- **Project:** Demo
- **Focus:** Predraft 1.1
- **Now:** The presented 1.1 candidate awaits the user's approval or comments.
- **Next:** Apply the user's response to 1.1, then propose 1.2.
- **Next source code:** B
- **Next user number:** 23

| Tracked filename | Role/state |
|---|---|
| demo-user-wording.md | Original user language |
| demo-article-arc.md | Accepted argument plan |
| demo-predraft.md | Selected paragraphs; next H03 |
| demo-source-map-a-service-log.md | Source A; pages 1–12 checked; next item A5 |
| original-file.pdf | Source original |
```

Keep all six header fields and the table in this order. Now states actual progress or the unanswered question; Next states the next action conditional on the required user decision.

List existing files needed to resume, using paths relative to the tracker. Include required originals, conversions and every retained wording basis named in saved provenance. The inventory consists of working inputs and outputs.

Each map row owns checked coverage, access limits and next excerpt ID. Record an unavailable original in that map row, and in Now/Next when it blocks current work.

Advance source codes, user numbers, excerpt IDs and heading IDs on allocation. Recover their highest allocated values from reliable history before replacing a missing counter; retired IDs remain retired. Arc numbers follow current positions.

On resumption, check inventory paths and pending work against actual files, then continue from the last user decision.
