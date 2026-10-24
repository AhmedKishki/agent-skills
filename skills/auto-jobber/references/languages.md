# English and German application documents

## Select the offer language

Determine whether the posting is English (`en`) or German (`de`). Ask the user when mixed or ambiguous; do not infer document language from nationality or name. Both CV and letter must use that language. Pass the required `new --language` option; it selects an approved snapshot through workspace `variants.json`. Preserve `plan.job.language`: validation requires it to match the selection. Writing German documents never establishes German proficiency. Keep actual language levels source-backed and unknown when absent.

## Approve a baseline in each needed language

If the selected variant is missing, pause per-job drafting and prepare it with the user. Translate source-backed prose faithfully and review fixed labels, titles, chronology and meaning before approval. This is a separate baseline review, not a wholesale per-job rewrite or a bypass of Tailoring's edit budgets. `intake` optional `document_language: "en"|"de"` localizes fixed labels only; the agent must translate prose for user review rather than assume it was translated.

Keep editable master sources wherever the user maintains them, for example root `cv.html` for English and workspace `cv.de.html` for German; no special variants directory exists. The profile in `qualifications.json` stays shared and unchanged between languages. Keep compatible editable marker IDs and evidence references in each HTML source. Never create different qualification histories by language.

`preview` and `seal` accept optional `--language en|de`, `--html` and `--css`. They otherwise use root `cv.html`/`cv.css`; `seal` detects `<html lang="en">` or `<html lang="de">` and rejects a conflicting requested language. For example, after preparing the German source:

```bash
python3 "$SKILL/scripts/auto_jobber.py" --workspace "$WORKSPACE" preview \
  --language de --html "$WORKSPACE/cv.de.html" --css "$WORKSPACE/cv.css"
# Obtain actual approval of this CV before sealing it.
python3 "$SKILL/scripts/auto_jobber.py" --workspace "$WORKSPACE" seal \
  --language de --html "$WORKSPACE/cv.de.html" --css "$WORKSPACE/cv.css"
```

Each seal copies the selected HTML/CSS and shared profile/source files into `baselines/<id>/` and registers that language in `variants.json`; root `baseline.json` is updated only when sealing root `cv.html`. Editable masters remain separate. Profile or imported-source changes, including monthly confirmation or remembered voice, invalidate the corresponding snapshot hashes. Review and reseal each needed language variant; retain prior revisions unchanged.

## Translate current-job user wording with approval

`wording --language en|de` declares the original input language; omitting it defaults to the offer language, so specify it when different. Keep the original hashed snapshot. Propose a faithful translation and obtain explicit user approval before capturing it separately:

```bash
python3 "$SKILL/scripts/auto_jobber.py" --workspace "$WORKSPACE" approve-translation \
  --application "$APPLICATION" --language de --text-file /private/approved.txt \
  --source 'actual user approval locator' --confirmed-by-user
```

The target must equal the offer language. The command adds a hashed translation record under `plan.user_input.translation` with `approval_source`, `approved_at` and `authorship: "user-approved-translation"`; it does not relabel AI translation as raw user voice. The approval flag cannot itself establish genuine consent. Voice's excerpt rules apply to the current-language original or this approved translation. `--must-include` phrases are exact final-language requirements; obtain user approval for any translated replacement before recording it. Translation never replaces the mandatory current-job applicant contribution.

Write letter sentence prose, greeting and closing in the selected language. The renderer localizes the subject and date: German `Bewerbung als …` with `DD.MM.YYYY`, English `Application for …` with ISO date. It does not translate prose or detect whether an `en`/`de` HTML declaration describes the actual text language.
