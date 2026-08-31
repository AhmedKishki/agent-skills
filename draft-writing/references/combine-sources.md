# Requested combined sources

Create `{project}-combined-sources-YYYY-MM-DD-HHMMSS.md` only when the user explicitly requests **combine sources**. This request-only file is neither canonical nor a drafting, evidence, synthesis, or approval input.

Read the current [activity tracker](activity-tracker.md). Collect every active source map once in assigned source-code order, preserving gaps and established legacy order, followed by the active [index](index.md). With no active source maps, report that and create nothing. Refresh a missing or stale index under its owner rules before combining.

## Assembly

Begin with the fixed wrapper `# Combined sources` and `**Process prose: AI**. Then copy the complete text of each active source-map file and the complete index unchanged. Preserve every embedded header, status, coverage statement, path row, excerpt, role, qualification, locator, provenance field, code, and index basis. Do not filter, repair, rescan, supplement, summarise, reformulate, synthesise, merge, deduplicate, normalise headings, or omit fields.

Add only these fixed HTML boundary comments around each block, substituting its exact tracker path:

    <!-- BEGIN VERBATIM FILE: exact tracker path -->
    <!-- END VERBATIM FILE: exact tracker path -->

The wrapper and comments supply no source meaning. Do not add a cover, contents page, narrative introduction, or reformatted source key.

Save and track the result under [file-output-standard.md](file-output-standard.md). Its tracker row must name the exact active source maps and index as its reuse basis. Any basis change makes it stale; retire it with the required removal notice and regenerate only on a new request.

Before delivery, confirm the inputs stayed unchanged during assembly, every active map appears exactly once in assigned order, the complete index appears last, every embedded block is byte-for-byte identical to its input, and only the fixed wrapper and boundary comments were added. On mismatch, discard only the invalid new combination and report the discrepancy; never repair an input inside the combined file.
