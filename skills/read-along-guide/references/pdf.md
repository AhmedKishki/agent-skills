# Read-along PDF

The guide's markdown files are combined into one PDF: a title page, a contents page with clickable entries and page numbers, the guide in reading order, and the definitions **last**. Internal definition links, the contents entries and the bookmarks all work, and the file renders quickly on phones and in browsers.

## 1. Ask first

When the user asks for the PDF, confirm with AskUserQuestion, offering the defaults:
- **Front pages**: a title page and a clickable contents list (recommended), contents only, or neither.
- **Page size**: A4 (recommended) or US Letter.

## 2. Fonts (the speed fix)

`python3 -I scripts/make_fonts.py fonts/` writes static TrueType fonts: Lora for the text, Inter for headings, tables and captions.

**Never let Chromium embed CFF/OpenType or variable fonts.** Skia turns them into Type 3 fonts, and those render slowly in phone and browser viewers. Measured on this kind of guide, the switch to static TrueType cut PDFium render time by about 40% and the file size from 5.5 MB to 3 MB. If Lora or Inter are missing, convert any other font pair to static TrueType (glyf) and use those in the `@font-face` rules of `build_pdf.py`.

## 3. Build

1. Write `config.json`:
   ```json
   {"guide_dir": "<work>/guide", "work_dir": "<work>/pdfbuild", "out": "<work>/pdfbuild/raw.pdf",
    "fonts_dir": "<work>/fonts",
    "files": ["01_front_matter", "02_chapter_1", "...", "06_postscript", "99_definitions"],
    "definitions": "99_definitions", "pdf_title": "A Read-Along Guide to <Author>'s <Title>",
    "lang": "en-GB", "page_size": "A4",
    "title_html": "<div class='k'>A read-along guide</div><div class='t'>Author,<br><i>Title</i></div><div class='rule'></div><div class='s'>Edition (Publisher, Year)<br>Scope</div>"}
   ```
2. `python3 -I scripts/build_pdf.py config.json` (two passes: the second fills in the contents page numbers).
3. `python3 -I scripts/fix_outline.py <work>/pdfbuild/guide.html raw.pdf fixed.pdf` restores exact bookmark titles.
4. `python3 -I scripts/slim_pdf.py fixed.pdf final.pdf` removes the structure tree and compresses objects. The bookmarks and links stay.

What `build_pdf.py` does:
- converts with pandoc (implicit figures off, so captions are not duplicated);
- joins each image and its italic caption into one unbreakable figure;
- inlines SVG figures with prefixed ids and the embedded fonts;
- puts a page break before each part in a separate `div` (a break on the `h1` itself garbles the bookmarks);
- keeps the definitions' letter headings out of the contents;
- numbers the pages in a CSS margin box, with no number on the title page;
- produces a tagged PDF with an outline (Chromium only writes bookmarks for tagged PDFs).

## 4. Verify

- `pdffonts final.pdf` lists only TrueType or CID TrueType fonts, with no Type 3.
- Every internal link resolves to a named destination (check the annotations with pdfminer).
- The number of bookmarks equals the number of headings, and the top-level bookmarks are the parts in order, with Definitions last.
- The build reports that the contents page numbers are stable between passes.
- Render sample pages with `pdftoppm -r 60` and Read them: the title page, the contents, a figure page, a table page, a definitions page and the last page. Check spacing, captions kept with figures, headings not stranded at the foot of a page, and that a very short last page is acceptable.
- Optional speed check: `pip install pypdfium2` and time rendering all pages.

## 5. Deliver

Copy `final.pdf` to the outputs folder under a descriptive name (e.g. `<Author>_<Short_title>_read-along_guide.pdf`) and send it with SendUserFile (`display: attach`). Also send a zip of the markdown files and images.
