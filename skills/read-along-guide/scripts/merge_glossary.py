# Merge new '### Term' entries from a staging file into the definitions file, alphabetically under '## Letter' groups.
# Usage: python3 -I merge_glossary.py master/99_definitions.md staging.md   (the definitions file must already have '# Definitions' and '## A')
import re, sys
G, NEW = sys.argv[1], sys.argv[2]
s = open(G).read()
title, rest = s.split('\n## A\n', 1)
entries = {}
for block in re.split(r'\n(?=### )', '## A\n' + rest):
    block = block.strip()
    if not block.startswith('### '): continue
    head, body = block.split('\n', 1)
    entries[head[4:].strip()] = re.sub(r'\n## [A-Z]\s*$', '', body.strip()).strip()
for block in re.split(r'\n(?=### )', open(NEW).read().strip()):
    head, body = block.split('\n', 1)
    h = head[4:].strip(); assert h not in entries, h; entries[h] = body.strip()
groups = {}
for h, b in entries.items(): groups.setdefault(h[0].upper(), []).append((h, b))
out = [title.rstrip() + '\n']
for L in sorted(groups):
    out.append(f'## {L}\n\n' + '\n\n'.join(f'### {h}\n{b}' for h, b in sorted(groups[L], key=lambda x: x[0].lower())) + '\n')
open(G, 'w').write('\n'.join(out)); print(len(entries), 'entries')
