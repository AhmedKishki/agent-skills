# Read-along definitions

Heavy terms are never defined at length inside the chapter files. They go into one alphabetical definitions file, `master/99_definitions.md`, and every guide file links the first use of each term in each `## ` section to its entry. In the PDF the definitions come at the end (`references/pdf.md`).

## 1. File format

```
# Definitions

## A

### A priori
Knowable independently of experience.

### Actualism
The doctrine that ... Bhaskar's description (Chapter 1, section 1.5): ‘...’.

## B
...
```

- Entries sit in alphabetical order under `## Letter` headings, one paragraph each, in the house style of `references/prose.md`.
- Link ids come from the `### ` headings: lowercase, punctuation removed, spaces to hyphens (`Fact/value dichotomy` → `factvalue-dichotomy`, `Ohm's law` → `ohms-law`). Pandoc and GitHub produce the same ids, so never rename a heading without relinking.

## 2. What goes in

- Every technical term, every coinage of the author's, foreign terms, and people, schools or works a beginner needs in order to follow the argument.
- Quote the author's own definition with its location when he gives one: "Bhaskar's definition (Chapter 2, section 2.2): ‘...’". Quotes are checked with `check_quotes.py`.
- Otherwise give a plain, accurate definition. Attribute borrowed terms correctly (who coined it, who made it central) and mark uncertainty.
- Use "See X" for cross-references between entries.
- When a later chapter extends a term, update the existing entry (add the new sense and its location). Do not create a duplicate.
- Glossary pointers to where a term is discussed are allowed in compact form ("examined in Chapter 1, section 1.3"). Everything else follows the say-it-directly rule.

## 3. Adding entries

1. Write the new entries to a staging file (`### Term` and one paragraph each).
2. `python3 -I scripts/merge_glossary.py master/99_definitions.md staging.md` merges them alphabetically. It stops on a duplicate heading. Edit existing entries directly.
3. Run `check_quotes.py` and `check_style.py` on the definitions file.

## 4. Linking

1. Copy the masters to `guide/` (the masters themselves are never linked).
2. For every guide file: `python3 -I scripts/link_terms.py guide/<file>.md guide/99_definitions.md [extra_patterns.json]`.
   - The script builds a pattern from each heading automatically: the phrase, an optional plural, case-insensitive unless the heading has capitals after its first letter. Longer headings are tried before shorter ones.
   - It links the first use of each term in each `## ` section. It looks in prose outside quotes first, then inside quotes, then in tables. It skips headings, image lines and caption lines.
3. `extra_patterns.json` maps a heading to extra regexes, which are tried first (variants, adjectives, italic forms such as `\*overt\*`). It can also map a heading to `null` to switch the automatic pattern off for over-general words ("Act", "Model", "Event"). Lookbehinds exclude false matches, such as book titles (*Scientific Realism and Human Emancipation*), names (Centre for Critical Realism) and ordinary uses of a word.
4. Review the new links in each file. List them with `grep -o '\[[^]]*\](99_definitions.md#[^)]*)'` and fix false matches through `extra_patterns.json`.

## 5. Link test

Concatenate all guide files, rewrite `(99_definitions.md#` to `(#`, convert with pandoc to HTML, and confirm that every `href="#x"` has a matching `id` and that every image file exists:

```bash
cat guide/0*.md guide/99_definitions.md | sed 's/(99_definitions\.md#/(#/g' | pandoc -f markdown -t html -o /tmp/combined.html
python3 -I - <<'PY'
import re, os, urllib.parse
h = open('/tmp/combined.html').read()
ids = set(re.findall(r'id="([^"]+)"', h)); hrefs = re.findall(r'href="#([^"]+)"', h)
bad = {x for x in hrefs if urllib.parse.unquote(x) not in ids and x not in ids}
print(len(hrefs), 'links,', len(bad), 'broken', sorted(bad)[:10])
print('missing images', [s for s in re.findall(r'src="([^"]+)"', h) if not os.path.exists(os.path.join('guide', s))])
PY
```
