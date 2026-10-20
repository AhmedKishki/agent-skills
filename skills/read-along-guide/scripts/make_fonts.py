# Make static TrueType (glyf) fonts so Chromium/Skia embeds real fonts, not slow Type 3 glyphs.
# Usage: python3 -I make_fonts.py <fonts_out_dir>   (needs Lora variable TTFs and Inter OTFs installed)
import sys, os
from fontTools.ttLib import TTFont, newTable
from fontTools.varLib import instancer
from fontTools.pens.cu2quPen import Cu2QuPen
from fontTools.pens.ttGlyphPen import TTGlyphPen
OUT = sys.argv[1]
G = '/usr/share/fonts/truetype/google-fonts/'
for src, wght, name in [('Lora-Variable.ttf', 400, 'Lora-Regular'), ('Lora-Variable.ttf', 700, 'Lora-Bold'),
                        ('Lora-Italic-Variable.ttf', 400, 'Lora-Italic'), ('Lora-Italic-Variable.ttf', 700, 'Lora-BoldItalic')]:
    f = TTFont(G + src)
    st = instancer.instantiateVariableFont(f, {'wght': wght}, updateFontNames=False)
    st.save(os.path.join(OUT, name + '.ttf'))

def otf_to_ttf(path, out):
    font = TTFont(path)
    glyphOrder = font.getGlyphOrder()
    gs = font.getGlyphSet()
    glyf = newTable('glyf'); glyf.glyphOrder = glyphOrder; glyf.glyphs = {}
    for gname in glyphOrder:
        pen = TTGlyphPen(gs)
        try:
            gs[gname].draw(Cu2QuPen(pen, 1.0, reverse_direction=True))
        except Exception:
            pass
        glyf[gname] = pen.glyph()
    font['loca'] = newTable('loca'); font['glyf'] = glyf
    font['maxp'] = newTable('maxp'); maxp = font['maxp']
    maxp.tableVersion = 0x00010000
    for a in ('maxZones','maxTwilightPoints','maxStorage','maxFunctionDefs','maxInstructionDefs','maxStackElements','maxSizeOfInstructions','maxComponentElements'):
        setattr(maxp, a, 0)
    maxp.maxZones = 1
    font['head'].glyphDataFormat = 0
    post = font['post']; post.formatType = 2.0; post.extraNames = []; post.mapping = {}; post.glyphOrder = glyphOrder
    del font['CFF ']
    if 'VORG' in font: del font['VORG']
    font.sfntVersion = '\x00\x01\x00\x00'
    font.save(out)

I = '/usr/share/fonts/opentype/inter/'
for n in ['Regular', 'Italic', 'SemiBold', 'SemiBoldItalic', 'Bold', 'BoldItalic']:
    otf_to_ttf(I + f'Inter-{n}.otf', os.path.join(OUT, f'Inter-{n}.ttf'))
print('ok')
