# Render explanatory figures (HTML box layouts) and previews of SVG figures to PNG with Playwright.
# Usage: python3 -I render_figure.py <out_dir> fig1.html [fig2.html ...]   -> <out_dir>/fig1.png (2x, 1000px layout width)
#        python3 -I render_figure.py --preview <out_dir> fig.svg [...]     -> <out_dir>/fig_preview.png (to Read and check)
# An input .html file holds only the figure body (no <html>/<style>); the shared stylesheet below is added.
import os, sys
from playwright.sync_api import sync_playwright
CSS = """
* { box-sizing: border-box; margin: 0; padding: 0; }
body { background: #ffffff; font-family: 'Inter', 'DejaVu Sans', sans-serif; color: #1f2933; }
#fig { width: 1000px; padding: 28px 30px 30px; background: #ffffff; }
.title { font-size: 21px; font-weight: 700; margin-bottom: 18px; }
.row { display: flex; gap: 22px; align-items: stretch; }
.col { display: flex; flex-direction: column; gap: 10px; }
.box { border: 2px solid #9fb3c8; background: #f0f4f8; border-radius: 10px; padding: 14px 16px; font-size: 16px; line-height: 1.38; }
.box h3 { font-size: 17px; font-weight: 700; margin-bottom: 6px; }
.label { font-size: 13px; font-weight: 600; letter-spacing: .04em; text-transform: uppercase; color: #52606d; margin-bottom: 4px; }
.small { font-size: 14px; color: #52606d; line-height: 1.35; }
.blue { border-color: #4a78b0; background: #e3edf8; }    /* knowledge, a position, the transitive side */
.amber { border-color: #b7832f; background: #f8eedd; }   /* a rival or contrasting position */
.green { border-color: #3f8f6b; background: #e1f2e9; }   /* real structures, mechanisms, the author's view */
.grey { border-color: #7b8794; background: #e9ecef; }    /* events, neutral or shared ground */
.arrow-down { text-align: center; font-size: 26px; color: #52606d; line-height: 1; margin: 6px 0; }
.arrow-right { display: flex; align-items: center; font-size: 28px; color: #52606d; }
.arr { display: flex; flex-direction: column; align-items: center; justify-content: center; color: #52606d; font-size: 28px; line-height: 1; }
.arr span { font-size: 12px; text-align: center; line-height: 1.2; margin-top: 4px; padding: 0 8px; }
"""
args = sys.argv[1:]
preview = args[0] == '--preview'
if preview: args = args[1:]
out_dir, files = args[0], args[1:]
os.makedirs(out_dir, exist_ok=True)
with sync_playwright() as p:
    br = p.chromium.launch()
    pg = br.new_page(device_scale_factor=2 if not preview else 1.5, viewport={'width': 1100, 'height': 1200})
    for f in files:
        src = open(f, encoding='utf-8').read()
        base = os.path.splitext(os.path.basename(f))[0]
        if preview:
            pg.set_content(f"<html><body style='margin:0;background:#fff'><div id='fig' style='display:inline-block'>{src}</div></body></html>")
            out = os.path.join(out_dir, base + '_preview.png')
        else:
            pg.set_content(f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body><div id='fig'>{src}</div></body></html>")
            out = os.path.join(out_dir, base + '.png')
        pg.wait_for_timeout(150)
        pg.locator('#fig').screenshot(path=out)
        print('wrote', out)
    br.close()
