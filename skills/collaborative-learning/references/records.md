# Project and Session Records

## Establish the destination

- Use the user's learning project directory when specified.
- If the user has not proposed a project name, choose an appropriate descriptive
  name based on the learning subject. Use a filename-safe directory name.
- Resolve `<project>/` to that directory; do not write learning records inside the skill.
- Use `<project>/learning-plan.md` for the plan and `<project>/sessions/<title>-session-n.md` for topic n.
- Choose a descriptive title for each session; use its lowercase hyphenated form
  as `<title>`. Record its title and relative file path in the learning plan.
- Create each session file lazily, only when its session is activated. Do not
  create future session files at the beginning. Create `sessions/` when needed.
- Keep established project names, session titles and paths stable on resumption.
- Check existing files before creating records; do not overwrite another subject.
- Honour the host's persistence requirements and preserve existing file identities.
- If saving fails, say so and preserve the pending content for recovery.
- Claim that a record is saved only after verifying the write succeeded.

## Maintain the plan

Record in `<project>/learning-plan.md`:

- Subject and agreed scope.
- Total session count and confirmation status.
- Numbered topics, ordered subtopics, and source locations.
- User confirmation and agreed plan changes.
- Current session, covered subtopics, next subtopic, and pending questions.

Keep completed, current, and pending coverage distinguishable.
Update progress after saving the corresponding session content.

## Maintain each session

Use this structure, omitting optional sections until they are needed:

```markdown
# Session n: [Topic]

Status: [in progress / complete]

## Related subtopics
[Ordered arguments, ideas, or claims from the confirmed plan]

## Explanation
[Full explanations delivered during this topic, with references]

## Discussion
### Exchange 1
**User:**
[User's exact question or clarification]

**Agent:**
[Full response with references]

## Optional exercises
[Requested questions, user answers, and feedback]

## References
[Complete source details and passage locations for this session]
```

- Save the explanation when delivered, not only when the topic ends.
- Append further subtopic explanations to the same session file in teaching order.
- Record learning-related user interactions verbatim, preserving wording and meaning.
- Record each delivered response fully; do not replace it with a discussion summary.
- Include requests to continue or adapt the plan when they occur during a session.
- Preserve the chronological order of discussion exchanges.
- Keep references local to the session and meaningful outside the chat interface.
- Record corrections explicitly and retain the exchange that prompted them.
- Do not silently rewrite the user's contributions or erase earlier discussion.
- Reopen the saved file to verify the latest explanation and exchange are present.
- On resumption, reconstruct progress from the records; do not fabricate missing turns.
