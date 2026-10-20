---
name: read-along-guide
description: This skill should be used when the user asks to make, continue or finish a read-along guide, study guide or companion to a book, says "next" for the next chapter of such a guide, or asks for the guide's PDF. Covers intake, argument breakdown, verified quotes, prose rules, figures, linked definitions and a fast PDF.
---

# Read-along guide

A read-along guide is read unit by unit: the reader reads one guide unit, then the matching section of the book. The guide follows the book's argument in the book's order, breaks each argument into explicit steps, illustrates complicated arguments with diagrams, adds context only where the author skims, and defines every heavy term in a separate, hyperlinked definitions file. It is written in plain, direct, natural prose for a reader who is not an expert.

This file coordinates the work and holds the content rules. Each module in `references/` has one job. Read a module in full at the step that needs it:

| Module | Purpose | Read at |
|---|---|---|
| `references/prose.md` | house style, the deletion test, say-it-directly, style checks, the writing pass | before writing, and for the writing pass |
| `references/figures.md` | reconstructing the author's figures and adding new explanatory diagrams | step 4 |
| `references/definitions.md` | the definitions file and linking each term's first use to it | step 5 |
| `references/pdf.md` | combining the guide into one fast PDF with the definitions at the end | when the PDF is requested |

Everything here is the standing specification. Apply it without being reminded.

## 1. Intake (once, before any writing)

Read the source first (or at least its contents, front matter and one chapter), then ask with AskUserQuestion. Offer the defaults as the recommended options.

- **Edition and file**: which edition the guide follows (the uploaded file).
- **Scope**: which parts to cover (foreword, prefaces, chapters, appendices, postscript). Default: everything the author wrote; editors' introductions excluded unless asked.
- **Pace**: default one chapter per turn, delivered, then wait for the user's go-ahead ("next").
- **Units**: default one guide unit per book section. If a part has no section headings (e.g. a postscript), ask: one continuous unit with internal subheadings, or thematic units.
- **Figures**: default yes, both kinds: every diagram of the author's is reconstructed, and new diagrams are added wherever they make an argument easier to follow.
- **Endnotes**: default use them only where they clarify the argument.
- **Front matter**: default its own file, delivered with Chapter 1.
- **PDF**: asked when the PDF is requested (`references/pdf.md`).

If anything is ambiguous at any point, stop and ask. Never assume.

## 2. Files and layout

```
<work>/
  source/            unpacked EPUB (or PDF) of the book
  text/              <part>.txt reading text, <part>.canon.txt, book.canon.txt
  master/            unlinked masters: 01_front_matter.md, 02_chapter_1.md, ..., 99_definitions.md
  guide/             deliverables: linked copies of the masters, images/
  figures/           figure sources (SVG files, HTML bodies)
  scripts/           copied from this skill's scripts/ folder
  fonts/             static TrueType fonts for the PDF
```

Edit only the masters. The deliverables in `guide/` are always regenerated from them (`references/definitions.md` covers the linking).

### Setup

1. Copy the `scripts/` folder from this skill's base directory (shown when the skill loads) to `<work>/scripts/`.
2. Install what is missing: `pip install --break-system-packages beautifulsoup4 lxml fonttools pdfminer.six playwright pillow`, plus `pandoc` and `qpdf`.
3. Unzip the EPUB into `source/`. Find the xhtml files in reading order (spine in `content.opf`).
4. `python3 -I scripts/extract_epub.py source/OEBPS text <part1> <part2> ...`. For a PDF source, use `pdftotext -layout` per chapter for reading, and build `book.canon.txt` from `pdftotext` (no layout) with line breaks collapsed. Replace note-marker digits by `†` where they can be detected.
5. List the author's figures (`grep -n '\[IMG' text/*.txt`) and convert the image files to PNG for viewing.
6. Note where each chapter's endnotes start in its `.txt` file (endnote N sits at a fixed line offset), so notes can be read quickly.

## 3. Structure of a chapter file

```
# Chapter N: <Title as in the book>

## What Chapters 1 to N-1 established
**Chapter 1.** <two or three sentences>
**Chapter 2.** ...
(one short paragraph per earlier chapter, so the file stands alone; Chapter 1 and the front matter recap nothing)

## The argument in brief
1. **<Short label> (N.1).** <the section's main claim and how it is reached, in one or two sentences>
2. ...

---

## N.1 <Section title exactly as in the book>
### <Subheading naming a step of the argument, stated as a claim or topic, never a question>
...
```

- One `## ` unit per book section, with the book's own section title, so the reader can find it. Subsections of the book get `### ` subheadings.
- Use the author's chapter and section numbers for cross-references ("Chapter 2, section 2.5"). Never page numbers. When the author cites his own pages, convert them to chapter and section.

## 4. Content rules

- **Follow the argument.** Each unit states what the author claims, the reasons he gives, the objections he answers and the conclusion he draws, in his order. Each subsection takes up a question the previous one raised.
- **Break arguments down.** Where the author argues, lay the argument out as numbered steps (premises, then conclusion). Make a premise explicit only when the author relies on it, and say that it is implicit. Use tables for comparisons between positions, and diagrams for arguments with direction, branching, levels or causation.
- **Context only where the author skims.** Explain names, schools, works and technical background a beginner needs, briefly and accurately. Mark it as context. Never present an inference of your own as the author's view, and never invent connections between ideas, people or texts.
- **Quotes.** Short verbatim quotes in curly single quotes ‘ ’, findable with Ctrl+F. Every quote must match the book exactly (case included) and must not cross a note marker. Terms are marked with italics or bold, never with quotation marks. Translations of foreign words also go in italics.
- **Endnotes** only where they clarify the argument ("A note adds that ...").
- **No extras**: no questions to the reader, no "check yourself", no summaries of your own beyond the argument in brief, no evaluation of the author unless asked, no fluff.
- **Definitions are never front-loaded** in the chapter. Heavy terms go to the definitions file (`references/definitions.md`).

## 5. Per-chapter workflow

1. **Read** the whole chapter and its notes before writing. View the author's figures. List the figures to reconstruct and the places where a new diagram would clarify the argument.
2. **Write** `master/NN_chapter_N.md` in the structure of section 3, following section 4 and `references/prose.md`. Build long files in several Write/Edit steps.
3. **Quotes**: `python3 -I scripts/check_quotes.py master/NN_chapter_N.md text` must report 0 problems. Shorten or correct any quote that is not found or that crosses a note marker.
4. **Figures**: follow `references/figures.md`.
5. **Definitions and links**: follow `references/definitions.md` (new entries, linking, the combined link test).
6. **Fidelity audit**: spawn a subagent with the master, the chapter's source text, the author's original figure images and the guide's figures. Ask for:
   - factual or interpretive errors and misattributions;
   - invented connections and inaccurate outside context;
   - missing or garbled argument steps;
   - table accuracy;
   - figure accuracy, comparing redrawn figures element by element with the originals and new figures with the text they illustrate;
   - glossary accuracy.
   Each finding cites the source line and proposes corrected wording. The report stays under 1,200 words, with no style comments. Verify each finding against the source yourself, then apply the fixes.
7. **Writing pass**: follow `references/prose.md` (deletion test, say-it-directly, style check). Then run the quote check again.
8. **Deliver**: regenerate `guide/`, copy the guide files and images to the outputs folder, zip them, and send with SendUserFile. Reply in a few sentences: what was covered, which figures were redrawn and which were added, notable fixes, and anything to check. Then wait for the go-ahead.

When all parts are done and the user asks for the PDF, follow `references/pdf.md`.

## 6. Scripts

All in this skill's `scripts/` folder. Run them from `<work>` with `python3 -I`.

| Script | Purpose | Used in |
|---|---|---|
| `extract_epub.py` | reading text and canonical text from the EPUB | setup |
| `check_quotes.py` | every quote verbatim in the book, none crossing a note marker | step 3 |
| `check_style.py` | house-style flags | `references/prose.md` |
| `detect_announce.py` | candidate announcement and counting sentences | `references/prose.md` |
| `render_figure.py` | HTML figures to PNG, SVG previews | `references/figures.md` |
| `merge_glossary.py` | merge new definitions alphabetically | `references/definitions.md` |
| `link_terms.py` | link the first use of each term per section | `references/definitions.md` |
| `make_fonts.py` | static TrueType fonts for a fast PDF | `references/pdf.md` |
| `build_pdf.py` | title page, contents, guide, definitions last | `references/pdf.md` |
| `fix_outline.py` | exact bookmark titles | `references/pdf.md` |
| `slim_pdf.py` | drop the structure tree and compress | `references/pdf.md` |
