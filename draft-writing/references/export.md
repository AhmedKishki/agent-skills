# Requested source export

Create `{project}-export-YYYY-MM-DD-HHMMSS.md` only on an explicit source/excerpt export request. For compatibility, bare **export** means source export; **user export** means [user-export.md](user-export.md). This Markdown snapshot is neither canonical nor a drafting dependency; source maps and index remain authoritative. With no active maps, report that and create nothing. Update a missing/stale index first. Reuse only when the tracker names exactly the same maps and index.

## Assembly

Use maps once in assigned code sequence (A–Z, then AA onward), preserving gaps and established legacy order; use items in map order. Include every resolved Human quotation with a complete blockquote boundary, source, and locator; roles do not affect eligibility. Include legacy exact quotations; exclude reformulations, reductions, and unresolved quotation records. Preserve active labels, including `-MT` and legacy forms.

Use this schema. Omit only an empty item **Qualification** line and an absent **Themes** section:

    # Source excerpt export

    ## A — Exact full human-readable source name from the map title

    ### Source qualifications
    Copied edition/access details, scope, limits, and cautions; or **No additional source qualifications recorded.**

    ### Main points — copied source argument-path wording, not quotations
    - Exact **Main source argument or move** cell, in recorded order.

    ### Excerpts
    #### A1 — Recorded main claim/topic
    > Exact stored quotation with editorial omissions preserved.

    **Location:** Exact copied locator
    **Qualification:** Exact copied item-specific qualification, limit, or counterclaim

For no eligible excerpts write **No verbatim excerpts recorded.** After the last source append:

    ## Index

    ### Themes
    | Theme | Keywords |
    |---|---|

    ### Keywords
    | Keyword | Items |
    |---|---|

Copy the active index's lookup cells exactly and in order; omit its header, provenance, and Human-basis columns. Omit **Themes** when absent.

Source fields must remain readable without codes. Ask about unclear identity, wording, quotation status/boundary, source, locator, or qualification; save the resolution canonically and restart. Never repair or infer inside the export.

Include only the schema's codes, source identity, qualifications, main points, quotations, topics, locators, item qualifications, and index lookup. Exclude provenance, percentages, workflow state, filenames, roles, relevance, placement, use, reformulations, reductions, and synthesis. Copy punctuation, quotation marks, omissions, locators, DOI/ISBN/URL, and source-authored identifiers exactly. Do not rescan, supplement, summarise, reformulate, synthesise, merge, or deduplicate during export.

## Output and checks

Use plain Markdown only—never PDF/DOCX—with no cover, contents page, images, or decoration. Save and track per [file-output-standard.md](file-output-standard.md).

Before delivery, confirm the maps/index are unchanged; every indexed item resolves to one exported excerpt; every excerpt has a keyword; every source appears once with code and full name; and every quotation, locator, qualification, main point, and index cell matches its canonical text except whitespace. On mismatch, update the map/index under its owner rules and ask if substantive or uncertain; never repair the export.
