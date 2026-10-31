# Keep the applicant's personal wording

## Retain the wording

Maintain a `personality.json` in the applicant's profile for wording they have entered about themselves, such as an interest, an opinion, a feeling or a line they would like to close a letter with. Keep each entry exactly as they entered it, because its value in a letter is that it sounds like them.

```json
{"schema_version": 1, "entries": [
  {"text": "<the applicant's exact words>", "author": "applicant",
   "source": "<conversation or artifact locator>",
   "use": "warm closing", "relevant_to": ["<field or kind of role>"]}
]}
```

Give each entry the applicant's exact `text`, `author: "applicant"` and the `source` locator of the conversation or artifact where they entered it. Add `use` and `relevant_to` when the applicant says where the wording should go or what it suits.

Store only wording the applicant entered. An agent-written suggestion, a paraphrase or a trait inferred from the CV or from their writing is not an entry, and neither are career facts, comments on a particular factual entry or the motivation for one job. Change or remove an entry only when the applicant asks.

## Use it in a letter

Read the entries before drafting a letter. Use an entry where its subject relates to the opportunity or to the letter's argument, and leave the others out: an entry that relates to neither reads as decoration, and one entry is usually enough.

Use the entry in the applicant's wording. Correct only spelling, capitalisation and grammar slips, and show those corrections with the draft.
