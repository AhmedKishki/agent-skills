# Review

Every lesson, supplement and re-explanation is reviewed once by the lesson reviewer before the student sees it. A skill lesson is reviewed part by part: the part up to the student's build step, then each continuation before you deliver it. Answers to the student's questions and check items are not reviewed.

## Sending the draft

Write the draft to a file outside the subject folder, such as the session's scratch or temporary directory, so the course records hold only what the student sees. Then start a fresh subagent with this prompt, filled in:

```
Read <absolute path of prompts/lesson-reviewer.md in this skill> and act as it says.
Draft: <absolute path of the draft>
Course goal: <goal from progress.md>
Student level: <each strand and its level, the misconceptions, and the key ideas of the lessons done>
This lesson: <number, title, type and key ideas>
Sources: <each cited source with its path or URL>
```

Send only this brief. Your reasoning about the draft and the passages you doubt stay out of it, so that the reviewer reads the text as the student will.

If the host has no subagents, finish the draft first, then read [lesson-reviewer.md](../prompts/lesson-reviewer.md) and review the draft against it as a separate pass, writing out the findings in its format before you revise.

## Acting on the review

There is one round. For each finding, check its evidence: open the quoted passage, rerun the command or reread the lines it names.

- If the finding holds, fix it in the draft.
- If it doesn't hold, ignore it. A misread source, a step the student already holds from an earlier lesson or a sentence that does carry information are examples.

For each claim listed under Unchecked, find a source that confirms it or mark it `[unsourced]`, as [sources.md](sources.md) describes.

Don't send the revision for another review. Write the revised lesson to the lesson note as [records.md](records.md) describes and deliver it. The student sees only the lesson: don't mention or quote the review in the reply, and don't save it in the subject folder. Add one line to the progress log with the number of findings and how many you fixed.
