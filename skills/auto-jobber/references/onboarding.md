# Build the applicant's baseline together

## Gather and normalize

Accept an old CV, qualification lists or both, with extra information from the user. Use `extract` or existing PDF/document tools to obtain source text, then normalize it; extraction is not qualification verification. Ask about missing study, work, experience, certificates, expertise, languages, projects and online presence (including GitHub). Preserve unknowns; never guess language/proficiency levels. Collect interests and writing preferences without inferring personality.

Run `init` for a new private workspace; inspect rather than reset an existing one. Normalize confirmed source material using Profile formats. Keep original locators and distinguish facts still needing confirmation from verified evidence. Use `intake --data normalized.json` on the empty initialized workspace. It keeps `intake-source.json`, converts to `candidate-source.json`, stores all category entries and renders a baseline using the upstream-derived layout. Record metadata even where not every field is displayed in the CV.

Alternatively, use `bootstrap --data resume-data.json` for the user's existing awesome-cv-html data. It requires an untouched, unsealed initialized profile and does not fetch demo credentials. Both import paths start evidence unverified. Audit every entry, metadata field, contact detail and displayed claim against the source; import success is not truth verification. Set `verified: true` only for confirmed evidence. Fixed roles, institutions and dates need the same audit as editable text. Add missing retained categories manually after bootstrap.

## Review the base CV before sealing

Resolve Freshness, then run `preview` to generate only the base CV's standalone HTML, PDF and PNGs. Do not invent a companion letter at this stage. Present the CV to the user, invite corrections and iterate wording/layout until they approve. Inspect every CV preview page using Tailoring's visual checklist. Require verified support for editable blocks and source-audit all other claims. Set CSS `@page` to match policy `paper` (`A4` or `Letter`).

The user may revise qualifications, source HTML or CSS at any time. Review those changes together and regenerate the preview before sealing the approved baseline. `seal` hashes the profile, CV/CSS and imported source variants, retaining each revision under `baselines/<timestampUUID>/`. Languages defines variant selection and manifest registration for root or custom HTML sources. Previous baselines and application snapshots remain independent; do not rewrite them when the master profile changes. Keep external evidence locators available.

## Manual HTML setup or later corrections

For an existing HTML CV, copy it to workspace `cv.html` and styling to `cv.css`; fill the profile using Profile formats. Use one plain `<head>` and passive HTML. Replace scripts, images, remote fonts/icons and resource-loading CSS with text and system-font styling. Keep only the local `cv.css` stylesheet link. Register eligible marker regions using Profile formats; roles, titles, dates, nested HTML and whole sections are not editable regions. Follow the same source, freshness, preview and approval steps before sealing this alternative baseline.
