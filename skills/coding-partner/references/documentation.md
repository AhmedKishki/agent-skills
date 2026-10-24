# Documentation

## File mental model

- Give every source file a brief description of its responsibility and how its main parts and data or control flow fit together. A simple file may need only one sentence.
- Explain the design decisions, constraints, and trade-offs needed to understand that arrangement, rather than catalogue its functions.

## Minimal explanation

- Write plain, direct documentation containing only what its job requires. Avoid repetition, boilerplate, and line-by-line code paraphrases.
- Leave self-documenting fragments intact. Explain only behaviour or reasons that are not already clear from the code and its verified contracts.
- Comments should explain intent or constraints, not compensate for obscure code.
- Keep each explanation in one authoritative place. Follow existing documentation conventions; if none exist, agree placement with the user. Do not automatically create a separate document for every file.

## Evidence and maintenance

- Describe verified operation and agreed design decisions. Do not invent the original author's intent. Label material inferred rationale as inference rather than fact.
- For source files created or changed by the agreed task, include any missing file overview and necessary documentation updates in the proposed change. Do not document unrelated files without an agreed task.
