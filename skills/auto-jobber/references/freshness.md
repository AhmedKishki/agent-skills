# Calendar-month qualification review

Run `status` against the actual retained profile before onboarding approval,
profile updates or a repeated application. Display its aware local
`current_datetime`, `current_month`, `latest_entry_month`, `last_reviewed_at` and
`needs_confirmation`; never substitute a hardcoded date or an assumed timezone.

The script finds the latest nonfuture qualification `updated_at`, `date`, `end`
or `start`. It compares the year/month of `last_reviewed_at`, otherwise that latest
entry, to the current year/month. This is not a rolling 30-day interval.
September 30 to October 1 and December to January each cross a review boundary.
With no known entry date or review, ask whether the profile is current.
When the review is already in the current month, do not ask again solely because
employment or another qualification is old. Still accept volunteered changes.

If confirmation is needed, ask what has changed in qualifications, projects,
certificates, language information or public work since the last review. Show
the relevant retained facts so the user can correct them or explicitly say
nothing changed. Update affected records and source-audit them before proceeding.

Only after an explicit user reply, run `confirm-current --note 'actual user reply'
--confirmed-by-user`. Record the real reply, including a genuine no-change reply;
never invent consent or run the flag as an agent impersonating the applicant.
The command writes `last_reviewed_at` and `current_confirmation` using actual time.
Its flag records the caller's assertion, not independent proof of user consent.

Confirmation changes the profile and invalidates the existing seal. Review the
current baseline with the user as needed, then reseal under Onboarding before
`new`. Voice retention and other profile edits likewise require review/resealing.

`seal`, `new`, `check` and `build` enforce freshness. The latter two currently use
the application's captured profile: when its month becomes stale, leave that
snapshot intact and create a new application from the refreshed approved baseline.
Do not silently patch an old snapshot to make its date gate pass.
