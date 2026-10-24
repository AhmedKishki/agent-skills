# CLI walkthrough and artifacts

Set `SKILL` to the installed skill directory. Workspace defaults to `AUTO_JOBBER_HOME`, otherwise `~/.local/share/auto-jobber`; explicit `--workspace` overrides both and must precede the subcommand. Keep private records outside the skill and repositories. Commands return JSON; retain their returned paths/IDs.

## Onboard and review the CV

```bash
SKILL=/absolute/path/to/auto-jobber
WORKSPACE="$HOME/.local/share/auto-jobber"
python3 "$SKILL/scripts/auto_jobber.py" --workspace "$WORKSPACE" doctor
python3 "$SKILL/scripts/auto_jobber.py" --workspace "$WORKSPACE" init
python3 "$SKILL/scripts/auto_jobber.py" --workspace "$WORKSPACE" extract \
  --input /private/old.pdf --output /private/extracted.txt
# Source-audit and normalize the extracted text plus the user's additions.
python3 "$SKILL/scripts/auto_jobber.py" --workspace "$WORKSPACE" intake \
  --data /private/normalized.json
# Alternative import instead of intake: bootstrap --data /private/resume-data.json
python3 "$SKILL/scripts/auto_jobber.py" --workspace "$WORKSPACE" status
```

After the Freshness dialogue, if confirmation is needed:

```bash
python3 "$SKILL/scripts/auto_jobber.py" --workspace "$WORKSPACE" confirm-current \
  --note "$ACTUAL_USER_REPLY" --confirmed-by-user
python3 "$SKILL/scripts/auto_jobber.py" --workspace "$WORKSPACE" preview
# Iterate corrections and previews; seal only after actual baseline approval.
python3 "$SKILL/scripts/auto_jobber.py" --workspace "$WORKSPACE" seal
```

`ACTUAL_USER_REPLY` means the explicit reply just received, not example consent. Optional voice retention before review/sealing:

```bash
python3 "$SKILL/scripts/auto_jobber.py" --workspace "$WORKSPACE" remember-voice \
  --text-file /private/user-sample.txt --source 'actual conversation locator'
```

## Repeat for each job

Run `status` again and resolve Freshness before `new`. Follow Voice to obtain this job's words and save them in `/private/actual-user-words.txt` before `wording`.

```bash
python3 "$SKILL/scripts/auto_jobber.py" --workspace "$WORKSPACE" new \
  --language en --job /private/complete-posting.txt
# Alternative to --job: --url https://employer.example/careers/vacancy
APPLICATION=/absolute/path/returned/by/new
python3 "$SKILL/scripts/auto_jobber.py" --workspace "$WORKSPACE" wording \
  --application "$APPLICATION" --text-file /private/actual-user-words.txt \
  --source 'actual current-job user reply locator'
# Optional repeated wording flags: --must-include 'exact user-required phrase'
python3 "$SKILL/scripts/auto_jobber.py" --workspace "$WORKSPACE" source \
  --application "$APPLICATION" --url https://employer.example/project \
  --title 'Actual official source title' --kind primary
```

Example domains are syntax illustrations, not evidence. Repeat `source` for real research; `--kind` accepts primary/secondary. Optional `--text-file /private/saved.txt` captures faithful extracted page text; `--published-at YYYY-MM-DD` records a source-supported date. Network fetching expects public HTTPS URLs. After authoring `research.json`/`plan.json` and completing source/voice audits:

```bash
python3 "$SKILL/scripts/auto_jobber.py" --workspace "$WORKSPACE" check \
  --application "$APPLICATION"
python3 "$SKILL/scripts/auto_jobber.py" --workspace "$WORKSPACE" build \
  --application "$APPLICATION"
BUILD=/absolute/path/returned/by/build
python3 "$SKILL/scripts/auto_jobber.py" --workspace "$WORKSPACE" verify --build "$BUILD"
# After applicant approval and every-page visual review:
python3 "$SKILL/scripts/auto_jobber.py" --workspace "$WORKSPACE" archive --build "$BUILD"
```

`build --html-only` is an HTML draft fallback; later make a fresh full build. `doctor` reports but does not install Python/Chrome/Poppler. Use existing Chrome/Chromium (`CHROME_BIN` selects it), `pdfinfo`, `pdftotext`, `pdftoppm`. The preview tool is needed even if `ready_for_pdf` is true without it. Do not disable Chrome's sandbox or set up a local model/database/API account.

The workspace retains raw intake/source variants, profile, CV/CSS, baseline revisions and CV-only `previews/`. Applications retain posting, `input/` baseline, `sources/`, `wording/`, plan and research. Successful `builds/` revisions retain their input, evidence, user wording, HTML/CSS, `cv.patch`, report and manifest. Full builds add PDFs/text/PNGs; the render report gives exact paths. `verify` detects file-set/hash changes, not truth or consent. `archive` copies the verified revision into the application's local `archive/`; nothing is submitted.

`extract` works offline on PDF (Poppler), DOCX (stdlib), HTML or UTF-8 text, including `.md`. Input and DOCX document XML are limited to 10 MiB. It refuses existing output and fewer than 40 readable characters; no legacy DOC/image OCR. Languages owns variant preview/seal and approved wording-translation commands.
