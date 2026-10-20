# Drop the tagged-PDF structure tree (keeps bookmarks and links) and compress objects.
# Usage: python3 -I slim_pdf.py in.pdf out.pdf
import json, subprocess, sys
src, out = sys.argv[1:3]
j = json.loads(subprocess.run(['qpdf', '--json-output', '--json-key=qpdf', src, '-'], capture_output=True, text=True, check=True).stdout)
meta, objs = j['qpdf']
root = objs['trailer']['value']['/Root']
cat = dict(objs[f'obj:{root}']['value'])
for k in ('/StructTreeRoot', '/MarkInfo'):
    cat.pop(k, None)
upd = {f'obj:{root}': {'value': cat}}
json.dump({'qpdf': [meta, upd]}, open(out + '.upd.json', 'w'))
subprocess.run(['qpdf', src, '--update-from-json=' + out + '.upd.json', '--object-streams=generate',
                '--compress-streams=y', '--recompress-flate', '--compression-level=9', out], check=True)
print('slimmed')
