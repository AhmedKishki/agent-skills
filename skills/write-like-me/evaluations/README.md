# End-to-end evaluations

`scenarios.json` defines realistic skill requests, critical deterministic checks, and plain-language criteria.

`activation-scenarios.json` separately records requests that should and should not
activate the skill. The package test suite checks that these cases remain balanced,
unique, and aligned with the skill description:

```bash
python3 scripts/run_tests.py
```

Activation behavior still needs a fresh-conversation smoke test on each target
platform because routing is controlled by the host, not by this repository.

Validate the scenario contract:

```bash
python3 scripts/evaluate_scenarios.py
```

For an OpenAI or Claude run, start a fresh conversation with the packaged skill enabled. Run every scenario and record a JSON response:

```json
{
  "responses": [
    {
      "scenario_id": "clean-draft-no-samples",
      "output": "The complete user-visible response",
      "primary_output": "The rewritten draft or primary artifact only",
      "criteria": {
        "return revised draft first": true,
        "preserve claims": true,
        "remove generic AI texture": true,
        "ask for samples before helping": false,
        "invent a personal story": false,
        "turn all paragraphs into one-line hooks": false
      }
    }
  ]
}
```

Then grade it:

```bash
python3 scripts/evaluate_scenarios.py \
  --responses evaluations/openai-responses.json \
  --result evaluations/openai-results.json
```

Repeat for Claude. The `criteria` values may be assigned by a blinded human reviewer or a model-assisted reviewer, but critical token, leakage, factual, and long-dash checks remain deterministic. Any critical failure blocks release rather than being averaged into a score.

Required and forbidden content tokens are checked against `primary_output` when it is supplied. The long-dash check covers the full user-visible `output`, including explanations and onboarding.

During incremental smoke testing, add `--allow-partial` to grade recorded scenarios and leave the rest explicitly pending. A release run must omit `--allow-partial` so every scenario is required.

## Ordinary-user blind baseline

The scenario suite checks contract compliance. It does not establish that the plugin creates value visible to an ordinary writer.

Use `evaluations/beta/README.md` for the 10 to 20 person private beta. It includes:

- a strong plain-prompt baseline using the same raw evidence;
- fresh-chat comparison against the portable Write Like Me file;
- randomized A/B preparation with a separate answer key;
- trial and participant CSV templates;
- critical-failure codes;
- a deterministic scorer and pre-registered directional decision gate.

Run the harness with:

```bash
python3 scripts/run_blind_beta.py --help
```

## Package boundary

The Claude and OpenAI production ZIPs contain only runtime instructions,
references, metadata where applicable, and the Starter-file builder. Tests,
evaluation fixtures, beta materials, and development scripts ship only in the
separate source/evaluation ZIP.
