# Read-along figures

Diagrams are a main tool for explaining complicated arguments. Every chapter of a read-along guide gets two kinds: reconstructions of the author's own figures, and new figures wherever a picture makes the argument easier to follow. Figure sources live in `figures/`, rendered or copied files in `guide/images/`.

## 1. Reconstructing the author's figures

- **Find them all.** Every `[IMG ...]` marker in `text/<part>.txt` points to an image in the EPUB. Convert each image to PNG (PIL) and Read it before writing the unit it belongs to.
- **Redraw as hand-written SVG** (`figures/figN_M_<name>.svg`, copied to `guide/images/`). Reproduce the author's content exactly:
  - every label and symbol (subscripts with `<tspan baseline-shift="sub">`);
  - every arrow, with its direction and style (solid, dashed, single or double head);
  - every line;
  - the relative layout. Do not add, drop, merge or reinterpret anything inside the drawing.
- **Helpful additions**, such as a key explaining the symbols or the names the author gives to each model's error, are allowed only when the author's own text supplies them. Set them visibly apart, in a separate key block or in smaller muted text. The caption says what was added: "redrawn from Bhaskar's diagram; the key is added from his text".
- **Placement**: at the point in the unit where the author's argument uses the figure.
- **Caption**: `*Figure N.M. <what the figure shows>, redrawn from <Author>'s diagram.*`
- **Check**: render a preview (`render_figure.py --preview`), Read the original and the redrawing, and compare them element by element (labels, symbols, arrow directions, dashes, positions). Fix any difference.
- **The author's tables** become markdown tables with verbatim cell contents (✓, ✗). Blank cells become "n/a" with a note, and the caption line goes above the table (`*Table N.M. ...*`).

## 2. Adding new figures

Add a figure wherever a picture would make an argument easier to follow than prose alone. Typical cases:

- an argument with a chain of steps or with branches (a model of explanation as a decision tree);
- levels, domains or strata and what belongs to each (the real, the actual and the empirical);
- positions and what they share or dispute (two traditions resting on one picture of science);
- a process or cycle (the transformational model of social activity; the cycle of scientific discovery);
- a causal analysis with several causes or co-causes (who causes what in an experiment; two causal series that cross);
- the form of an argument (the shape of a transcendental argument).

Rules:

- A new figure illustrates what the text beside it says. Everything in it is stated in the guide's text or in the book, and it adds no claim of its own.
- Use a table for a grid of comparisons. Use a figure when the content has direction, sequence, nesting, branching or causation.
- One idea per figure. Place it directly after the paragraph or numbered steps it illustrates.
- Labels are short and follow the house style (`references/prose.md`): British English, no semicolons or dashes. Any quote inside a figure is verbatim and is checked like other quotes.
- Caption: `*Figure N.M. <the point the figure makes, in one or two sentences>.*`
- Expect about one new figure for every two or three sections that contain a structured argument. Never add a decorative figure.

## 3. Technique

- **Box layouts** (boxes, flows, trees, comparisons): write the figure body as HTML in `figures/figN_M_<name>.html` and render it with `python3 -I scripts/render_figure.py guide/images figures/figN_M_<name>.html`. The script supplies the shared stylesheet, a 1000px layout width and a 2x PNG. Useful classes: `.title`, `.row`, `.col`, `.box` with a colour class, `.label`, `.small`, `.arrow-down`, `.arrow-right`, `.arr` with a `<span>` arrow label.
- **Geometry** (lines between symbols, nested strata, crossing series): hand-written SVG with `viewBox`, white background, font-family `Inter, 'DejaVu Sans', sans-serif`, and `<marker>` arrowheads. The PDF builder inlines SVGs and switches them to the embedded fonts.
- **Colours** keep one meaning across the whole guide:
  - blue: knowledge, or the position under discussion;
  - amber: a rival or contrasting position;
  - green: real structures and mechanisms, or the author's own view;
  - grey: events, or shared ground.
- **Legibility**: text at least 13px at the 1000px layout width, so it stays readable at A4 text width.
- **Numbering**: Figure N.M in order of appearance within chapter N, with the author's and the guide's figures counted together. Use P.1, P.2 for a postscript and F.1 for the front matter. File names: `figN_M_<short_name>.png|svg`. The image alt text repeats the caption.
- **Markdown**: the image line, then the italic caption line directly below it:
  ```
  ![Figure 2.1. ...](images/fig2_1_models.svg)

  *Figure 2.1. ...*
  ```

## 4. Checks

- Read every rendered PNG and every SVG preview. Fix overflowing or overlapping labels, labels wrapped in narrow columns, arrows that point to the wrong box or sit between the wrong elements, and arrowheads doubled or missing. Re-render after each fix.
- Run the quote check on any figure that contains quotes (put the quote in the caption or the text as well, or check it by hand against `book.canon.txt`).
- The fidelity audit (SKILL.md, step 6) compares redrawn figures with the originals and new figures with the text they illustrate.
