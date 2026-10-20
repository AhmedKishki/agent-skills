# Explanations

Use the recorded level if present; otherwise ask the user to choose Beginner,
Standard, or Expert. Do not infer expertise. Keep that choice until the user
changes it. Explain each proposed patch before asking for approval. Do not print
all three levels unless the user asks for them.

Use the scope below for the explanation. The level does not change the approval
boundary, amount of code shown, or required check and risk disclosure. Keep that
proposal context separate from the explanation. Avoid unrelated tutorials and
repetition. Show each code block once; refer back to it instead of repeating it.

## Beginner — learner or student

Explain the algorithm in plain language, then the language primitives and
constructs used, then the code step by step in execution order. Define relevant
types, operators, variables, functions, and control flow without assuming prior
knowledge. Connect each step to the algorithm; use a small example when helpful.

## Standard — junior developer

Explain the algorithm, then summarize how the code implements it. Cover the main
functions and control or data flow concisely. Skip language-primitive definitions
and line-by-line walkthroughs.

## Expert — senior or academic

Explain the algorithm only: its method, why it works, and relevant assumptions,
invariants, or complexity. Omit code summaries, syntax lessons, and code
walkthroughs. Do not add jargon or claim properties the algorithm does not have.

## Same code, different explanations

For a proposed Python predicate:

```python
def valid_age(age: int) -> bool:
    return 0 <= age <= 130
```

- **Beginner:** The algorithm accepts an integer age only when it meets both
  limits, 0 and 130. `def` declares the function; `age` is its input parameter.
  `int` and `bool` are type hints for the input and result, not runtime checks.
  The `<=` operator means less than or equal to.
  First, `0 <= age` checks the lower limit. If it passes, `age <= 130` checks the
  upper limit. `return` sends back the resulting Boolean: `True` if both checks
  pass, otherwise `False`. For example, 18 passes both checks; 131 fails the second.
- **Standard:** Test both inclusive bounds on an already validated integer; accept
  only when both hold. The function returns the result of a chained comparison.
  Input-type validation remains the caller's responsibility.
- **Expert:** Inclusive interval membership with an integer-input precondition:
  accept exactly when both lower and upper bounds hold. No iteration is needed.
