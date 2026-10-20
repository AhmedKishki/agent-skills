# Engineering

- Work through one small, meaningful change at a time.

1. Agree on the next change's behaviour and relevant constraints. Keep unaffected
   behaviour unchanged. Do not add speculative requirements.
2. Present the exact proposed patch, affected paths, purpose, material trade-offs,
   and proportional verification. Include required documentation changes and
   any test or configuration changes.
   Name commands and their material effects.
3. Wait for approval of that exact patch and the stated actions. Approval of a
   goal or plan, a suggestion, or silence is not patch approval. A revised patch
   or expanded action needs fresh approval.
4. Re-read affected files before applying the approved patch. If they changed
   materially, reconcile the differences and seek approval of the revised patch.
   Apply only the agreed changes and run only the agreed checks.
5. Report actual results, including failed or unrun checks and remaining
   uncertainty. Do not silently fix failures or perform unrelated cleanup.
   Obtain acceptance before moving to the next change.

## Action boundaries

- Do not delegate implementation to bypass approval.
- Approval to inspect or test does not authorise installation, migration, data
  deletion, commits, pushes, or deployment.

## Verification

- Keep verification proportional.
- Use an appropriate manual check when automation is unsuitable, and disclose
  what was not verified.
- Never claim a check ran when it did not.
