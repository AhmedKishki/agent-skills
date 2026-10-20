# Checklist

- Work the steps in order. Tick a step only when its checks hold.
- Keep this audit and its cut report out of the operational files being cleaned.

## Before editing

- [ ] Capture a baseline: the line count, the word count and the section list.
- [ ] Search the repository for citations of each filename before moving anything.
- [ ] Inventory each unit's owner, allowed category, protected wording, command, override, qualification, exception, path, and its scope and ordering words.

## Job and type

- [ ] Read each file's job from its meta-view row.
- [ ] Identify each file's type before proposing, and choose the remedy for that type.
- [ ] State the remedy's trade-off to the user.
- [ ] Read the project's ownership contracts and classify every affected unit before planning edits.

## Contradictions

- [ ] Find rules that conflict before restructuring.
- [ ] Re-read the surrounding sections before reporting. A conflict often resolves itself nearby.
- [ ] Report each conflict to the user as a question. Leave the choice to the user.

## Sufficiency

- [ ] Check that each file holds everything its job requires.
- [ ] Report each missing requirement to the user as a question.
- [ ] Mark every line that serves no part of the job for cutting.

## Structural pass

- [ ] Restructure each file's scaffolding: language, sentences, sections and bullets.
- [ ] Transfer every unique qualification to the receiving owner before removing the origin.

## Semantic pass

- [ ] Read each file against the others. A merge reveals duplication that a structural pass leaves in place.
- [ ] Move every unit to the owner whose contract admits it, and consolidate every rule that two files state.
- [ ] Cut or relocate every line of second-order documentation outside the meta view.

## Apply

- [ ] Report every cut to the user before making it, and delete only on approval. Never delete silently.
- [ ] Keep the file's voice and existing formatting conventions.
- [ ] Locate each edit by content. Assert the content exists before writing.

## Verification

- Always verify. A reader can check a structure by eye and still miss a lost rule.

- [ ] For each removal, identify the surviving owner and complete equivalent unit, or the approved obsolete content. Unmatched unique information fails verification.
- [ ] Compare before/after qualifications semantically, not just by phrase presence.
  - Check attribution, modality, conditions, scope, approval extent, exclusions and order.
  - Check scope and ordering words such as "only", "unless", "first" and "much, though not all".
  - Match protected wording and counters exactly unless their change was approved.
  - A surviving label, identifier or distinctive phrase is not proof that the qualification survived.
- [ ] Check each receiving owner's allowed content, and confirm the actual information and its qualifications are present there, not only a link or a sentence about a move. Reject a duplicate operational record or an implicit ownership exception.
- [ ] Audit changed scaffolding for second-order documentation, source inventories in handoffs, historical narration, boilerplate and unclear actors. Treat string matches as findings to review, not permission to rewrite quotations or records.
- [ ] Check every inbound link and anchor after a heading or file change, including links in unchanged files; then check outgoing links, citations and identifier references.
- [ ] Run the project's applicable checks. A preservation or routing failure blocks completion; repair it or ask the author, never hide it behind a word-count reduction.

## Report

- [ ] Report every consolidation with the files it touched.
- [ ] Report the line count, word count and percentage change.
  - Report a small reduction as the honest result when every remaining line carries weight. Do not describe a small reduction as a cleanup.
- [ ] Commit and push the submodule before the parent pointer.
