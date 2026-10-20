# Link the first use of each glossary term in each '## ' section of a guide file.
# Usage: python3 -I link_terms.py guide.md glossary.md [extra_patterns.json]
# Patterns come from the glossary headings automatically (phrase, optional plural, case-insensitive
# unless the heading has capitals after its first letter). extra_patterns.json maps a heading to a list
# of extra regexes (tried first), or to null to switch the automatic pattern off (for over-general words).
import json, re, sys
GUIDE, GLOSS = sys.argv[1], sys.argv[2]
EXTRA = json.load(open(sys.argv[3], encoding='utf-8')) if len(sys.argv) > 3 else {}
LINK_FILE = GLOSS.split('/')[-1]

def gid(h):
    h = re.sub(r'[*_`]', '', h).strip().lower()
    h = re.sub(r'[^\w\s-]', '', h, flags=re.U)
    return re.sub(r'\s+', '-', h)

heads = [l[4:].strip() for l in open(GLOSS, encoding='utf-8') if l.startswith('### ')]
W, E = r'(?<![\w-])', r'(?!\w)'
pats = []
for h in heads:
    for rx in EXTRA.get(h) or []:
        pats.append((len(h) + 1000, gid(h), re.compile(W + '(?:' + rx + ')' + E, re.I)))
for h in heads:
    if h in EXTRA and EXTRA[h] is None:
        continue
    words = [re.escape(w) for w in re.sub(r'[*_`]', '', h).split()]
    rx = r'[\s-]+'.join(words) + r'(?:s|es)?'
    flags = 0 if re.search(r'[A-Z]', h[1:]) else re.I
    pats.append((len(h), gid(h), re.compile(W + '(?:' + rx + ')' + E, flags)))
pats.sort(key=lambda x: -x[0])   # specific (long) before generic (short)

QUOTE = re.compile(r'‘.+?’(?=[\s.,;:!?)\]*_]|$)')
LINK = re.compile(r'\[[^\]]*\]\([^)]*\)')
def masked(line, mask_quotes):
    m = list(line)
    spans = [x.span() for x in LINK.finditer(line)] + ([x.span() for x in QUOTE.finditer(line)] if mask_quotes else [])
    for a, b in spans:
        for i in range(a, b): m[i] = '\x00'
    return ''.join(m)
def eligible(line, kind):
    if not line.strip() or line.startswith(('#', '![', '*Figure', '*Table')): return False
    is_table = line.lstrip().startswith('|')
    return is_table if kind == 'table' else not is_table

out = []
for sec in re.split(r'(?m)^(?=## )', open(GUIDE, encoding='utf-8').read()):
    lines, done = sec.split('\n'), set()
    for _, tid, rx in pats:
        if tid in done: continue
        placed = False
        for kind, mq in (('prose', True), ('prose', False), ('table', True), ('table', False)):
            for i, line in enumerate(lines):
                if not eligible(line, kind): continue
                mm = masked(line, mq)
                for m in rx.finditer(mm):
                    a, b = m.span()
                    if '\x00' in mm[a:b]: continue
                    lines[i] = line[:a] + f'[{line[a:b]}]({LINK_FILE}#{tid})' + line[b:]
                    placed = True; break
                if placed: break
            if placed: break
        if placed: done.add(tid)
    out.append('\n'.join(lines))
open(GUIDE, 'w', encoding='utf-8').write(''.join(out))
print('linked', GUIDE)
