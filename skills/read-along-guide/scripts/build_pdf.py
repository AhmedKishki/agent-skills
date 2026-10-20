# Build the combined PDF: title page, clickable contents with page numbers, guide files, definitions last.
# Usage: python3 -I build_pdf.py config.json
# config: {"guide_dir": ".../guide", "work_dir": ".../pdfbuild", "out": ".../guide_raw.pdf",
#          "fonts_dir": ".../fonts", "files": ["01_front_matter", ..., "99_definitions"],
#          "definitions": "99_definitions", "pdf_title": "...", "lang": "en-GB", "page_size": "A4",
#          "title_html": "<div class='k'>A read-along guide</div><div class='t'>Author,<br><i>Book</i></div>
#                         <div class='rule'></div><div class='s'>Edition<br>Scope</div>"}
# Then: fix_outline.py <work_dir>/guide.html raw.pdf fixed.pdf && slim_pdf.py fixed.pdf final.pdf
import json, os, re, subprocess, sys
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

C = json.load(open(sys.argv[1], encoding='utf-8'))
GUIDE, WORK, OUT, FONTS, DEFS = C['guide_dir'], C['work_dir'], C['out'], C['fonts_dir'], C['definitions']
os.makedirs(WORK, exist_ok=True)

md = '\n\n'.join(open(os.path.join(GUIDE, f + '.md'), encoding='utf-8').read().strip() for f in C['files'])
md = md.replace(f'({DEFS}.md#', '(#')
body = subprocess.run(['pandoc', '-f', 'markdown-implicit_figures', '-t', 'html5', '--wrap=none'],
                      input=md, capture_output=True, text=True, check=True).stdout
soup = BeautifulSoup(body, 'html.parser')
for hr in soup.find_all('hr'):
    hr.decompose()

# image paragraph + following italic 'Figure ...' caption -> one unbreakable <figure>
for p in list(soup.find_all('p')):
    kids = [k for k in p.contents if not (isinstance(k, str) and not k.strip())]
    if len(kids) == 1 and getattr(kids[0], 'name', None) == 'img':
        fig = soup.new_tag('figure', attrs={'class': 'fig'})
        nxt = p.find_next_sibling()
        p.replace_with(fig); fig.append(kids[0])
        if nxt is not None and nxt.name == 'p' and nxt.get_text().strip().startswith(('Figure', 'Table')) and nxt.find('em'):
            cap = soup.new_tag('figcaption')
            for c in list(nxt.find('em').contents):
                cap.append(c)
            nxt.decompose(); fig.append(cap)

# inline SVGs so their text uses the embedded TrueType fonts; prefix ids so markers stay unique
for k, img in enumerate(soup.select('figure.fig img')):
    src = img.get('src', '')
    if src.endswith('.svg'):
        svg = re.sub(r'<\?xml[^>]*>', '', open(os.path.join(GUIDE, src), encoding='utf-8').read())
        svg = re.sub(r'id="([^"]+)"', lambda m: f'id="s{k}_{m.group(1)}"', svg)
        svg = re.sub(r'url\(#([^)]+)\)', lambda m: f'url(#s{k}_{m.group(1)})', svg)
        svg = re.sub(r'font-family="[^"]*"', 'font-family="GuideSans, DejaVu Sans, sans-serif"', svg)
        frag = BeautifulSoup(svg, 'html.parser').find('svg')
        frag['role'] = 'img'; frag['aria-label'] = img.get('alt', '')
        frag['style'] = 'width:100%; height:auto; display:block;'
        img.replace_with(frag)

for p in list(soup.find_all('p')):
    if p.find('em') and p.get_text().strip().startswith('Table') and len(p.contents) == 1:
        p['class'] = 'tablecap'

# page break before each part, kept outside the heading (a break on the h1 itself garbles bookmarks)
for h in soup.find_all('h1'):
    h.insert_before(soup.new_tag('div', attrs={'class': 'pb'}))

# wrap the definitions part so its letter headings get their own style and stay out of the contents
for h in soup.find_all('h1'):
    if h.get_text().strip() == 'Definitions':
        div = soup.new_tag('div', attrs={'class': 'defs'})
        node, nodes = h.next_sibling, []
        while node is not None and not (getattr(node, 'name', None) == 'div' and 'pb' in (node.get('class') or [])):
            nodes.append(node); node = node.next_sibling
        h.insert_after(div)
        for n in nodes:
            div.append(n.extract())

toc = []
for h in soup.find_all(['h1', 'h2']):
    if h.name == 'h2' and h.find_parent('div', class_='defs'):
        continue
    toc.append((h.name, h['id'], h.get_text()))

def toc_html(pages):
    return '<ol class="toc">' + ''.join(
        f'<li class="toc-{l}"><a href="#{i}"><span class="t">{t}</span><span class="dots"></span>'
        f'<span class="n">{n}</span></a></li>' for (l, i, t), n in zip(toc, pages)) + '</ol>'

faces = []
for fam, files in [('GuideSerif', [('Lora-Regular', 400, 'normal'), ('Lora-Italic', 400, 'italic'),
                                   ('Lora-Bold', 700, 'normal'), ('Lora-BoldItalic', 700, 'italic')]),
                   ('GuideSans', [('Inter-Regular', 400, 'normal'), ('Inter-Italic', 400, 'italic'),
                                  ('Inter-SemiBold', 600, 'normal'), ('Inter-SemiBoldItalic', 600, 'italic'),
                                  ('Inter-Bold', 700, 'normal'), ('Inter-BoldItalic', 700, 'italic')])]:
    for fn, w, st in files:
        faces.append(f"@font-face {{ font-family: '{fam}'; src: url('file://{os.path.abspath(FONTS)}/{fn}.ttf') "
                     f"format('truetype'); font-weight: {w}; font-style: {st}; }}")
SERIF = "'GuideSerif', 'Liberation Serif', 'DejaVu Serif', serif"
SANS = "'GuideSans', 'DejaVu Sans', sans-serif"
CSS = '\n'.join(faces) + f"""
@page {{ size: {C.get('page_size', 'A4')}; margin: 22mm 21mm 24mm 21mm;
  @bottom-center {{ content: counter(page); font-family: {SANS}; font-size: 8.5pt; color: #52606d; }} }}
@page :first {{ @bottom-center {{ content: none; }} }}
html {{ font-family: {SERIF}; font-size: 10.5pt; line-height: 1.5; color: #1f2933; }}
body {{ margin: 0; }}
h1, h2, h3, h4, .toc, figcaption, table, .tablecap, .title-page, .contents-h {{ font-family: {SANS}; }}
div.pb {{ break-before: page; height: 0; }}
h1 {{ font-size: 21pt; line-height: 1.2; font-weight: 700; margin: 1pt 0 14pt; padding-bottom: 8pt; border-bottom: 1.5pt solid #1f2933; }}
h2 {{ font-size: 13.5pt; font-weight: 700; margin: 20pt 0 6pt; break-after: avoid; }}
h3 {{ font-size: 11pt; font-weight: 600; margin: 14pt 0 4pt; break-after: avoid; }}
h4 {{ font-size: 10.5pt; font-weight: 600; margin: 10pt 0 3pt; break-after: avoid; }}
p {{ margin: 0 0 7pt; orphans: 3; widows: 3; }}
ul, ol {{ margin: 0 0 8pt; padding-left: 18pt; }}
li {{ margin: 0 0 3pt; }} li > p {{ margin: 0 0 3pt; }}
a {{ color: #1f4e79; text-decoration: none; }}
figure.fig {{ margin: 10pt 0 12pt; break-inside: avoid; text-align: center; }}
figure.fig img {{ width: 100%; height: auto; max-height: 150mm; object-fit: contain; }}
figcaption {{ font-size: 8.5pt; color: #52606d; text-align: left; margin-top: 4pt; line-height: 1.4; }}
table {{ border-collapse: collapse; width: 100%; font-size: 8.8pt; line-height: 1.35; margin: 4pt 0 10pt; break-inside: avoid; }}
th, td {{ border: 0.6pt solid #9aa5b1; padding: 3pt 5pt; vertical-align: top; text-align: left; font-family: {SANS}; }}
th {{ background: #eef2f6; font-weight: 600; }}
p.tablecap {{ font-size: 8.8pt; color: #52606d; margin: 8pt 0 2pt; break-after: avoid; font-family: {SANS}; }}
.defs h2 {{ font-size: 16pt; color: #52606d; border-bottom: 0.6pt solid #9aa5b1; padding-bottom: 2pt; }}
.defs h3 {{ font-size: 10.5pt; margin: 9pt 0 2pt; }}
.defs p {{ margin-bottom: 4pt; }}
.title-page {{ height: 240mm; display: flex; flex-direction: column; justify-content: center; }}
.title-page .k {{ font-size: 10pt; letter-spacing: .08em; text-transform: uppercase; color: #52606d; margin-bottom: 14pt; }}
.title-page .t {{ font-size: 28pt; font-weight: 700; line-height: 1.15; margin-bottom: 14pt; }}
.title-page .s {{ font-family: {SERIF}; font-size: 12.5pt; color: #3e4c59; line-height: 1.5; }}
.title-page .rule {{ width: 60mm; border-top: 1.5pt solid #1f2933; margin: 18pt 0; }}
.contents-h {{ break-before: page; font-size: 21pt; font-weight: 700; margin: 0 0 14pt; padding-bottom: 8pt; border-bottom: 1.5pt solid #1f2933; }}
ol.toc {{ list-style: none; padding: 0; margin: 0; font-size: 9.3pt; line-height: 1.42; }}
ol.toc li {{ margin: 0; }}
ol.toc a {{ display: flex; align-items: baseline; color: #1f2933; }}
ol.toc .dots {{ flex: 1; border-bottom: 0.6pt dotted #9aa5b1; margin: 0 4pt; transform: translateY(-2pt); }}
ol.toc .n {{ min-width: 18pt; text-align: right; }}
li.toc-h1 {{ font-weight: 700; font-size: 10pt; margin-top: 5.5pt !important; }}
li.toc-h2 {{ padding-left: 14pt; color: #3e4c59; }}
"""
MAIN = str(soup)

def page_html(pages):
    return (f"<!doctype html><html lang='{C.get('lang', 'en-GB')}'><head><meta charset='utf-8'>"
            f"<base href='file://{os.path.abspath(GUIDE)}/'><title>{C['pdf_title']}</title><style>{CSS}</style></head>"
            f"<body><section class='title-page'>{C['title_html']}</section>"
            f"<div class='contents-h'>Contents</div>{toc_html(pages)}{MAIN}</body></html>")

def render(html, out):
    path = os.path.join(WORK, 'guide.html')
    open(path, 'w', encoding='utf-8').write(html)
    with sync_playwright() as p:
        br = p.chromium.launch(); pg = br.new_page()
        pg.goto('file://' + path, wait_until='load'); pg.wait_for_timeout(500)
        pg.pdf(path=out, prefer_css_page_size=True, print_background=True, outline=True, tagged=True)
        br.close()

def toc_targets(pdf):
    # page number of each contents link's destination, in reading order (contents sit on the first pages)
    from pdfminer.pdfparser import PDFParser
    from pdfminer.pdfdocument import PDFDocument
    from pdfminer.pdfpage import PDFPage
    from pdfminer.pdftypes import resolve1
    doc = PDFDocument(PDFParser(open(pdf, 'rb')))
    dests = resolve1(doc.catalog['Dests'])
    pages = list(PDFPage.create_pages(doc))
    pno = {pg.pageid: i + 1 for i, pg in enumerate(pages)}
    out = []
    for pg in pages[:8]:
        annots = [resolve1(a) for a in (resolve1(pg.annots) or [])]
        annots.sort(key=lambda a: (-round(resolve1(a['Rect'])[3]), resolve1(a['Rect'])[0]))
        for a in annots:
            d = resolve1(a.get('Dest'))
            if d is None: continue
            d = resolve1(dests.get(d.name)) if hasattr(d, 'name') else d
            if isinstance(d, dict): d = resolve1(d.get('D'))
            out.append(pno.get(d[0].objid))
    return out, len(pages)

tmp = os.path.join(WORK, 'pass1.pdf')
render(page_html(['000'] * len(toc)), tmp)
t1, n1 = toc_targets(tmp)
t1 = t1[:len(toc)]
assert len(t1) == len(toc) and all(t1), (len(t1), len(toc))
render(page_html([str(t) for t in t1]), OUT)
t2, n2 = toc_targets(OUT)
print(f'contents entries {len(toc)}, pages {n2}, page numbers stable: {t2[:len(toc)] == t1}')
