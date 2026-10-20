# Replace PDF bookmark titles with the exact heading texts from the HTML (Chromium drops spaces at line wraps).
# Usage: python3 -I fix_outline.py guide.html in.pdf out.pdf
import json, subprocess, sys
from bs4 import BeautifulSoup
html, pdf_in, pdf_out = sys.argv[1:4]
soup = BeautifulSoup(open(html, encoding='utf-8').read(), 'html.parser')
heads = [' '.join(h.get_text().split()) for h in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])]
j = json.loads(subprocess.run(['qpdf', '--json-output', pdf_in, '-'], capture_output=True, text=True, check=True).stdout)
objs = j['qpdf'][1]
def val(ref): return objs[f'obj:{ref}']['value']
trailer = objs['trailer']['value']
cat = val(trailer['/Root'])
items = []
def walk(ref):
    while ref:
        items.append(ref)
        v = val(ref)
        if '/First' in v: walk(v['/First'])
        ref = v.get('/Next')
walk(val(cat['/Outlines'])['/First'])
print('outline items', len(items), 'headings', len(heads))
assert len(items) == len(heads)
upd = {}
changed = 0
for ref, title in zip(items, heads):
    v = dict(val(ref))
    if v.get('/Title') != 'u:' + title:
        changed += 1
    v['/Title'] = 'u:' + title
    upd[f'obj:{ref}'] = {'value': v}
meta = j['qpdf'][0]
json.dump({'qpdf': [meta, upd]}, open(pdf_out + '.upd.json', 'w'))
subprocess.run(['qpdf', pdf_in, '--update-from-json=' + pdf_out + '.upd.json', pdf_out], check=True)
print('titles changed', changed)
