# Check that every ‘…’ quote in a guide file appears verbatim in the book and does not cross a note marker.
# Usage: python3 -I check_quotes.py guide.md <text_dir containing book.canon.txt>
import os, re, sys
md = open(sys.argv[1], encoding='utf-8').read()
canon = open(os.path.join(sys.argv[2], 'book.canon.txt'), encoding='utf-8').read()
def norm(s): return re.sub(r'\s+', ' ', s).strip()
canon_n = norm(canon)
body = re.sub(r'!\[[^\]]*\]\([^)]*\)', '', md)          # drop image refs
body = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', body)    # unwrap links
quotes = re.findall(r'‘(.+?)’(?=[\s.,;:!?)\]*_]|$)', body, flags=re.S)
bad = 0
for q in quotes:
    qn = norm(q.replace('*', ''))
    if canon_n.count(qn) == 0:
        bad += 1; print('NOT FOUND:', qn[:110])
    elif '†' in qn:
        bad += 1; print('CROSSES NOTE MARKER:', qn[:110])
print(f'{len(quotes)} quotes checked, {bad} problems')
