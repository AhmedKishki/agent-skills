# List candidate announcement sentences and counting lead-ins (to judge by hand against the say-it-directly rule).
# Usage: python3 -I detect_announce.py master/*.md
import re, sys, glob
NUM = r'(two|three|four|five|six|seven|several|a number of|various)'
NOUNS = r'(ways?|parts?|points?|kinds?|grounds?|issues?|things?|features?|reasons?|objections?|conclusions?|arguments?|claims?|options?|problems?|questions?|senses?|steps?|stages?|errors?|achievements?|strands?|charges?|comments?|answers?|replies|consequences?|conditions?|criteria|levels?|types?|theses|premises|models?|routes?|lines?|cases?|dimensions?|limits?|aims?|tasks?|respects?|contrasts?|distinctions?|changes?|effects?|functions?|roles?|sides?|camps?|traditions?|elements?|components?|moves?|phases?|principles?|corollaries|requirements?|implications?|lessons?|difficulties|tendencies|terms|categories|answers?|alternatives?|possibilities|mistakes?|confusions?|defects?|advantages?|virtues?|results?|outcomes?|fall-backs?|strategies|responses?|reactions?)'
META = r'\b(sums? up|summari[sz]es?|lists?|sets? out|spells? out|turns? to|takes? up|examines?|considers?|follows?|as follows|the following|below|outlines?)\b'
def sentences(text):
    return re.split(r'(?<=[.:!?])\s+(?=[A-Z‘(*\d])', text)
out = []
for f in sorted(sys.argv[1:]):
    for n, line in enumerate(open(f, encoding='utf-8'), 1):
        if line.startswith(('#', '!', '*Figure', '*Table', '|')) or not line.strip():
            continue
        body = re.sub(r'^\s*([-*]|\d+\.)\s+', '', line.strip())
        for s in sentences(body):
            s0 = re.sub(r'‘[^’]*’', 'Q', s)
            hit = None
            if re.search(r'\b' + NUM + r'\b(\s+\w+){0,3}\s+' + NOUNS + r'\b', s0, re.I) and (s.endswith(':') or len(s0.split()) <= 16):
                hit = 'count'
            elif s.endswith(':') and 'Q' not in s0 and len(s0.split()) <= 12:
                hit = 'colon-lead'
            elif re.search(META, s0, re.I) and len(s0.split()) <= 12:
                hit = 'meta'
            if hit:
                out.append(f'{f.split("/")[-1]}:{n} [{hit}] {s}')
print('\n'.join(out)); print(len(out), 'candidates', file=sys.stderr)
