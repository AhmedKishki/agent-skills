---
name: scheduled-learning
description: Set up and run a multi-session, section-by-section learning plan for a book, paper, or other long source. Each run explains one part of the source faithfully (main argument, premises and conclusions, key concepts, short quotes, max 2000 words) and records progress in a markdown progress file so nothing is ever explained twice. Use this whenever the user wants to study, work through, or be taught a source gradually over several sessions or automated runs, mentions "scheduled learning", a learning plan, "one section per run/day/week", "next section", "next run", or "continue where we left off" on a source, or when an automated task points at a learning progress file. Use it even if the user doesn't say "skill" or "scheduled".
---

# Scheduled learning

This skill turns a source (a book, a paper, a set of texts) into a numbered series of runs. Each run explains one part of the source and records what was covered in a markdown progress file. The next run reads that file and continues exactly where the last one stopped, so nothing is explained twice and nothing is skipped.

A **track** is one plan with one progress file. A track can include several sources. The plan is counted in **runs**, not dates: it doesn't matter whether runs happen daily, weekly, or whenever the user says "next".

There are two modes: **setup** (once per track) and **run** (every time the next explanation is triggered, manually or by an automated task).

## Ask, don't assume

The user wants anything ambiguous resolved by asking, never by guessing. In setup and in manually triggered runs, ask when something is unclear. In an unattended run nobody can answer, so follow the rules under "Unattended runs" instead.

## Which mode?

- The user wants to learn a source and no progress file exists for it → **setup**.
- A progress file is named in the request (or is the only one in the named folder) and its `plan_status` is `approved` → **run**.
- The progress file's plan is still `draft`, or the user wants to change the plan → treat it as **setup** (revise and re-present the plan).
- Several progress files could apply and the request doesn't say which → ask which one.

## Setup (once per track)

### 1. Clarify before planning

Before drafting anything, ask the user, in one batched message, about whatever isn't already clear from their request:

- Which source files, which folder holds them, and where the progress file should be kept.
- How each source is divided into units (chapters, numbered sections, page ranges, something else). If the user gave a division, use it. If not, propose one from the source's own structure, and ask when more than one reasonable structure exists.
- With several sources: the order (one after another, interleaved, other).
- Anything to leave out or include (front matter, bibliography, index, appendices).
- The language for the explanations.
- Anything else in the request that could be read two ways.

Skip questions the user has already answered.

### 2. Read the source's structure

Open the actual file. Extract the table of contents or headings and estimate each unit's size. The explanations and quotes must come from the real text, never from memory of the work, because a quote reconstructed from memory can be subtly wrong and the whole point is fidelity to the author. If the file can't be opened, or text extraction is unusable (for example a scanned PDF with no text layer), tell the user and stop.

### 3. Draft a concrete plan

One row per run: run number, source, exactly what the run covers (section titles, plus page ranges where the source has them), and approximate size. By default one unit is one run. Flag units that look too long or dense for 2000 words, so the user isn't surprised when a run later splits them. Tell the user that the exact content of each run is settled at run time and that the plan can change.

### 4. Get approval

Present the plan and wait for explicit approval. If the user asks for changes, revise and present it again. Don't write an approved progress file before approval.

### 5. Create the progress file

After approval, write the progress file using the format in `references/progress-file.md`, named `progress-<track-slug>.md`, in the agreed location. Then tell the user:

- the file's path and the number of runs,
- the one line that triggers a run, for manual use or for an automated task: *"Use the scheduled-learning skill with the progress file at `<path>`."*

Setup ends here. Don't start run 1 unless the user asks for it.

## Run (every time the next explanation is triggered)

1. **Load the track.** Read the progress file. Check that `plan_status` is `approved` and the track isn't complete. The next run is the lowest-numbered run marked `pending`.
2. **Read the source text for that run**, from the file. Also read what the progress file records about earlier runs: where the previous run stopped (if this run continues a split unit) and which concepts have already been introduced.
3. **Decide the scope.** Read the whole unit first and list its moving parts: claims, premises, objections and replies, concepts, supporting examples. Estimate whether a faithful explanation of all of it fits in 2000 words.
   - If it fits, the run covers the whole unit.
   - If it doesn't, split. Cover a coherent first part that ends at a natural joint of the argument (never mid-step) and record the exact stopping point. The remainder becomes the next run, and later runs are renumbered. A unit can split into more than two runs.
   - Make this decision before writing. Never squeeze content to make it fit, because the user would rather have two good runs than one run with gaps.
4. **Write the explanation** following the standards below.
5. **Update the progress file** (see `references/progress-file.md`): mark the run done with the date, add its coverage entry, and log any plan change. Do this before replying so the record is saved even if the conversation ends abruptly. If the update fails, say so plainly in the reply and note that the same run would repeat next time.
6. **Reply** in the format at the end of this file.

When the last run is done, set the track's status to `complete` and tell the user the plan is finished.

## Explanation standards

The reader should come away understanding what the author argues, how the argument proceeds, and what the author's key terms mean. They should not need the source open beside them.

**Fidelity.** Explain what the author lays out and nothing else.
- Don't add your own reading, interpretation, evaluation, criticism, examples, analogies, or connections to other thinkers or works. If the author makes a connection, report it as the author's.
- Keep the author as the subject of the sentences ("Bhaskar argues...", "He claims...", "The premise is...").
- When the author reports someone else's view, make clear whose view it is and where the author's own begins.
- If the text is obscure or ambiguous at some point, say so ("The text does not say whether...") instead of resolving it yourself.
- Keep the author's technical terms. Substituting a synonym can quietly change the meaning. Explain each term using the author's own definition or usage.

**Completeness.** Cover everything the author does in the unit: every claim, premise, objection and reply, concept, and each example that supports a step (say briefly what the example is there to show). Equations, diagrams, and tables count as content: explain what they show. The test: could someone reconstruct the unit's argument and its parts from your explanation alone? If you can't do that within 2000 words, the unit should have been split.

**Structure.** Choose headings and numbering that make the logic visible. A reliable shape:
1. *Main argument*: what the unit as a whole argues, in a few sentences.
2. *Key concepts*: the terms the author introduces or relies on here, each as the author defines or uses it.
3. *The argument step by step*: the bulk of the explanation. Break it into steps, and for each step show the premises and the conclusion drawn, and how that conclusion feeds the next step. Number the steps when it helps. Label premises and conclusions explicitly where the logic is dense.
4. *Where it ends*: the conclusion the author reaches, and, if the author says so, what it sets up next.

Adapt this when the unit's shape calls for it (for example, a unit that is mainly a critique of another position needs that position laid out first).

**Quotes.** Use short verbatim quotes in the middle of the explanation, to anchor key claims and definitions. Each quote should be a phrase or a single sentence, no longer than about 25 words, never a full paragraph. Quote only wording you have read in the file during this run; if you can't find the exact wording, paraphrase instead. Where the source gives locations (page or section numbers), add a brief reference after the quote so the user can find it.

**Language.** Plain, concise, direct. Short sentences, no jargon beyond the author's own terms, defined where they enter the argument. No filler: no praise for the author, no "in this section we will...", no closing recap. Write in the language the user chose at setup; quotes stay in the source's language.

**Length.** At most 2000 words for the explanation body, including quotes and headings. Count mechanically if you have a way to; otherwise estimate conservatively.

**No repetition.** Don't re-explain anything an earlier run covered. When the unit uses a concept already introduced, use the term without redefining it and point to the run where it was explained ("see Run 2"). Re-explain only if the author changes or extends the concept's meaning here, and then explain only the change. When a run continues a split unit, open with at most two sentences saying where the argument stands, then carry on.

## Plan changes

The plan belongs to the user, but runs may revise it when the source calls for it. The usual change is a split (step 3 above). Other changes, such as correcting a section boundary that turned out to be wrong, are allowed too. Rules:
- Runs already marked `done` keep their numbers and are never rewritten.
- Renumber the pending runs after a change.
- Log every change in the progress file's plan-changes section with the run it happened in and why.
- Mention the change to the user in the reply (see below).

## Unattended runs

An automated task has nobody to answer questions, so it must not improvise. If anything needed is missing or doubtful, stop, say exactly what the problem is, and leave the progress file untouched. That covers:
- the progress file is missing, unreadable, or its plan isn't approved,
- the source file is missing or can't be read,
- several progress files could apply and the trigger doesn't say which,
- the next run can't be identified from the file.

An unattended run that proceeds normally follows the same steps as any other run.

## Reply format

```
**Run N of M — <what this run covers>**

<the explanation>

---
Progress: N of M runs done. Next: Run N+1 — <what it covers>.
<If this run changed the plan: one or two sentences saying what changed and why.>
```

M is the current total, and may differ from the original plan after splits. The 2000-word limit applies to the explanation; the header and footer stay to a line or two each.
