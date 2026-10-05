# Meta rules

## Information about information

- Information about information is second-order documentation: what a file records, holds, contains or has received, and where a rule or record lives.
- Second-order documentation lives in one standalone meta view and nowhere else.
- Every other file states first-order information only.
  - A file states its own content. It does not describe what another file holds, and it does not replace its content with a link to it.
  - Reject sentences saying another file records, holds, contains or has received information. State the information directly in its owner, or cut a redundant report.
  - Do not add a sentence announcing where a removed copy went. Do not create a transfer diary or breadcrumb paragraph.

## The meta view

- The meta view names each file, what it records and when to read it.
- The meta view states each file's purpose once, in one sentence.
- The meta view holds no first-order rules or content.
- If a file has no row, or its purpose is unclear or wrong, ask the user. Do not invent a purpose.

## Self-description

- A file carries no description of itself, in its frontmatter or its body.
- Exception: frontmatter its host requires, such as a skill entry point's `name` and `description`.
- A project or skill rule that requires self-description conflicts with this rule. Report the conflict to the user as a question; do not strip the description unasked.

## Links between files

- A file links another file only when the reader must open it to do this file's job: an input such as a source map, or the meta view's routing.
- A link saying where a rule or record lives is second-order documentation. The meta view owns it.
- When a duplicate is removed, cut it. Do not leave a link in its place.
- Do not replace the owner's information or qualifications with a pointer.

## Anti-patterns

| Avoid | Instead |
|---|---|
| "The file records…" or "This was added…" | State the information in its owner |
| Replacing required information with a link | Keep the information and its qualifications at the expected point |
| A link left where a duplicate was removed | Cut the copy; the meta view locates the owner |
| A file describing its own purpose | State the purpose in the meta view |
