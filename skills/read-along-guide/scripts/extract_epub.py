# Usage: python3 -I extract_epub.py <epub_dir_with_xhtml> <out_dir> part1 part2 ...   (parts = xhtml basenames in reading order)
# Writes <part>.txt (reading text, one block per line, headings as ##, images as [IMG ...])
# and <part>.canon.txt plus book.canon.txt (inline text, note markers replaced by the sentinel †) for quote checks.
import os, re, sys
from bs4 import BeautifulSoup
src, out, parts = sys.argv[1], sys.argv[2], sys.argv[3:]
os.makedirs(out, exist_ok=True)
canon_all = []
for name in parts:
    html = open(os.path.join(src, name + '.xhtml'), encoding='utf-8').read()
    soup = BeautifulSoup(html, 'lxml')
    lines = []
    for el in soup.body.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'p', 'li', 'blockquote', 'td', 'img']):
        if el.name == 'img':
            lines.append('[IMG ' + el.get('src', '') + ']'); continue
        if el.name in ('li', 'td', 'blockquote') and el.find('p'): continue
        t = re.sub(r'\s+', ' ', el.get_text(' ')).strip()
        if t: lines.append(('#' * int(el.name[1]) + ' ' + t) if el.name.startswith('h') else t)
    open(os.path.join(out, name + '.txt'), 'w', encoding='utf-8').write('\n'.join(lines))
    soup = BeautifulSoup(html, 'lxml')
    for a in soup.find_all('a', attrs={'epub:type': 'noteref'}):
        a.replace_with('†')
    blocks = []
    for el in soup.body.find_all(['h1', 'h2', 'h3', 'h4', 'p', 'li', 'td']):
        if el.find(['p', 'li']): continue
        t = re.sub(r'\s+', ' ', el.get_text('')).strip()
        if t: blocks.append(t)
    open(os.path.join(out, name + '.canon.txt'), 'w', encoding='utf-8').write('\n'.join(blocks))
    canon_all.append('\n'.join(blocks))
    print(name, len(' '.join(lines).split()), 'words')
open(os.path.join(out, 'book.canon.txt'), 'w', encoding='utf-8').write('\n'.join(canon_all))
