# House-style scan of a guide file's own prose (quotes, links and images masked out).
# Usage: python3 -I check_style.py guide.md
# Prints one line per flag. Judge each: literal uses and the author's own terms may stay.
import re, sys
md = open(sys.argv[1], encoding='utf-8').read()
body = re.sub(r'!\[[^\]]*\]\([^)]*\)', '', md)
body = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', body)
prose = re.sub(r'‘(.+?)’(?=[\s.,;:!?)\]*_]|$)', '“Q”', body, flags=re.S)
prose = re.sub(r'^>.*$', '', prose, flags=re.M)       # block quotes are the author's
checks = {
 'semicolon': r';',
 'em/en dash': r'[—–]| - ',
 'not..but': r'\bnot\b[^.!?\n]{0,60}\bbut\b',
 'rather than': r'\brather than\b',
 'instead of': r'\binstead of\b',
 'banned word': r'\b(posit(s|ed|ing)?|proliferat\w*|foreground\w*|problematis\w*|register\w*|important\w*|importance|operat\w*|does work|move[sd]?|moving|foreclos\w*|run[s]?|running|frontier\w*|agent\w*|actor\w*|crucial\w*|key)\b',
 'US spelling': r'\b\w+(iz(e|es|ed|ing|ation|ations)|yz(e|ed|es|ing))\b|\b(behavior\w*|center\w*|color\w*|favor\w*|labor\b|defense)\b',
 'bare This/It opener': r'(^|[.!?]\s+)(This|It|These)\s+(is|was|means|shows|makes|leaves|gives|has|does|can|will|would|matters)\b',
 'pseudo-cleft': r'(^|[.!?]\s+)What\s+\w+(\s+\w+)?\s+(is|does|means|wants|needs|shows)\b',
 'signposting': r'\b(let us|let\'s|we will|we shall|in this section|this section|below we|as we will see|note that)\b',
 'question': r'\?\s*$',
}
allowed_ize = {'size', 'prize', 'seize', 'capsize', 'analyse'}
n = 0
for name, pat in checks.items():
    for i, l in enumerate(prose.split('\n'), 1):
        if name == 'question' and (l.startswith('|') or not l.strip()): continue
        flags = 0 if name in ('bare This/It opener', 'pseudo-cleft') else re.I
        for m in re.finditer(pat, l, flags=flags):
            if name == 'US spelling' and m.group(0).strip().lower() in allowed_ize: continue
            n += 1; print(f'[{name}] line {i}: ...{l[max(0, m.start() - 50):m.end() + 40]}...')
print(f'{n} style flags')
