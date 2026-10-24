# Auto-jobber

A reusable, author-led skill for retaining qualifications, reviewing a base CV, researching an employer and shaping each letter from the applicant's own words. The output is matching HTML/CSS plus reviewable PDFs, not an automatic submission. Both documents follow the offer's English or German language, using separately reviewed CV baselines and user-approved translations of personal wording where needed.

Start with an old CV or lists of study, work, projects and other qualifications, plus anything missing from them. Review the generated CV together before approval; no cover letter is generated during onboarding. The profile can be revised later.

For each vacancy, supply the posting and your motivation, examples and desired tone. The agent preserves your wording instead of inventing a generic letter. Later sessions check whether the qualifications need a calendar-month update.

The CV layout uses a centered header and red accents. The companion letter uses the same styling. Remote fonts/icons and the old Gulp toolchain are not required. Credits and license: [THIRD_PARTY_LICENSE](THIRD_PARTY_LICENSE).

Read [SKILL.md](SKILL.md) for the workflow and reference routing. The command walkthrough covers normalized `intake`, the alternative upstream `bootstrap` import, profile confirmation, CV previews and repeated applications.

Runtime requirements are Python 3, an existing Chrome/Chromium installation and Poppler tools. Agent web access supplies research; the scripts do not generate it. Private qualifications, source material and raw voice samples stay in `~/.local/share/auto-jobber` by default, outside the installed skill.
