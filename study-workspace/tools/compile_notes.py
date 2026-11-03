"""Compile the textual layer of each verse study from the site's own source studies.

Fills siteNote, whyNote, lost (direction list) and chapterNote.lost for every chapter record,
strictly from text already present in the chapter's sources record. Interpretive prose
(received, explain, shared, instructions) is left for authoring.

usage: compile_notes.py SRC_DIR DST_DIR [book ...]
"""
import sys, os, json, re, glob, collections
sys.path.insert(0, '/home/claude/work/lib')
from extract import ptext

SRC, DST = sys.argv[1], sys.argv[2]
ONLY = set(sys.argv[3:])
os.makedirs(DST, exist_ok=True)
TODAY = '2026-11-02'
RANK = {'Same': 0, 'Similar': 1, 'Different': 2, 'Divergent': 3, 'Disparate': 4}
LABEL = {'hebrew': 'Hebrew and Greek', 'latin': 'Latin and Greek', 'kjv': 'King James and Greek'}
L1 = re.compile(r'^(?:\d\.\s*)?(Direct word|Direct wording|Wording and meaning|English word comparison|Meaning and context|Alignment)', re.I)
L4 = re.compile(r'^(?:\d\.\s*)?(Combined classification|Classification and synthesis|Text and reception together)', re.I)
L5 = re.compile(r'^(?:\d\.\s*)?How (and why )?the differences? arose', re.I)
BOILER = re.compile(r'(The complete source readings appear above\.?|These observations can be read together[^.]*\.|Compare the named sources[^.]*\.|Interpretive additions stay outside[^.]*\.|Read the named [^.]*\.|Open the (full|complete) [^.]*\.|Assessment open\.?|Review pending\.?|The expanded menu preserves the full verse and all wording highlights\.|See layer \d\.?|Selected English contrasts:|(?:(?:BHS|Rahlfs[–-]Hanhart|NA28|Clementine|Textus Receptus|LXX|MT)\s+[\d:a-z–-]+\s*·?\s*)+\.?)', re.I)
REFONLY = re.compile(r'^\s*((BHS|Rahlfs|NA28|Clementine|KJV|Masoretic|Septuagint|Vulgate|Textus)[^.]{0,80}\.?\s*)+$')

def para_text(t):
    if isinstance(t, dict): t = t['quote']
    return re.sub(r'\s+', ' ', ptext(t)).strip()

def layer(card, rx):
    out = []
    for sec in card['sections']:
        if rx.match(sec['title'] or ''):
            for t in sec['text']:
                s = para_text(t)
                if s and not REFONLY.match(s): out.append(s)
    return ' '.join(out)

def first_layer(card):
    txt = layer(card, L1)
    if not txt and card['sections'] and not card['sections'][0]['title']:
        txt = ' '.join(para_text(t) for t in card['sections'][0]['text'])
    return clean(txt)

def clean(s):
    s = BOILER.sub('', s or '')
    s = re.sub(r'\bText:\s*', '', s)
    s = re.sub(r'^\s*(?:(?:Same|Similar|Different|Divergent|Disparate)\s*(?:·\s*\w+)?\.\s*)+', '', s)
    s = re.sub(r'\s+', ' ', s).strip(' ·;,-—')
    return s

def trim(s, n=420):
    if len(s) <= n: return s
    cut = s[:n]
    m = re.search(r'^(.*?[.!?])(?=\s)', cut[::-1])
    return (cut[:len(cut) - m.start()] if m else cut).strip() + ('' if cut.endswith('.') else '…')

def compile_chapter(book, ch):
    d = json.load(open(f'{SRC}/{book}-{ch}.json'))
    s = json.load(open(f'{SRC}/{book}-{ch}.sources.json'))
    tally = {k: collections.Counter() for k in LABEL}
    notable = []
    for v in d['verses']:
        if v.get('received'):  # authored prose is kept untouched
            continue
        vs = v['ref'].split(':', 1)[1]
        cards = [x for x in s['verses'].get(vs, []) if x['kind'] in LABEL]
        primary = next((c for k in ('hebrew', 'latin', 'kjv') for c in cards if c['kind'] == k and c['rating']), None) \
            or next((c for k in ('hebrew', 'latin', 'kjv') for c in cards if c['kind'] == k), None)
        lost = []
        for c in cards:
            if not c['rating']: continue
            tally[c['kind']][c['rating']] += 1
            text = first_layer(c) or clean(layer(c, L4))
            if not text: continue
            if c['kind'] == 'hebrew': dir_ = 'keeps' if c['rating'] == 'Same' else 'differs'
            else: dir_ = 'between'
            lost.append({'dir': dir_, 'text': LABEL[c['kind']] + ' · ' + c['rating'] + ': ' + trim(text)})
        v['lost'] = lost
        if primary:
            v['siteNote'] = trim(first_layer(primary), 900)
            v['whyNote'] = trim(clean(layer(primary, L5)), 900)
            v['siteNoteLabel'] = LABEL[primary['kind']] + ' · ' + (primary['rating'] or primary['badge'] or 'assessment open')
        if v.get('badge') in ('Divergent', 'Disparate'): notable.append(vs)
    parts = []
    for k in ('hebrew', 'latin', 'kjv'):
        t = tally[k]
        if not t: continue
        n = sum(t.values())
        parts.append(f"{LABEL[k]}: {n} rated verse{'s' if n != 1 else ''} (" + ', '.join(f'{t[r]} {r}' for r in RANK if t[r]) + ')')
    if parts and not d['chapterNote'].get('lost'):
        note = f"Compiled from the site's source studies for {d['book']} {ch}. " + '; '.join(parts) + '.'
        if notable: note += ' Verses rated Divergent or Disparate: ' + ', '.join(notable) + '.'
        note += ' The written summary of what changes across this chapter has not been written yet.'
        d['chapterNote']['lost'] = note
    if not any(v.get('received') for v in d['verses']):
        d['status'] = 'Textual notes compiled from the site’s studies · study prose not yet written'
        d['generated'] = TODAY
        d['credit'] = 'Textual notes, source studies, word studies and cross-references are drawn from this site’s comparison pages, study editions and reference reviews. Open each source for its full text and citations.'
    json.dump(d, open(f'{DST}/{book}-{ch}.json', 'w'), ensure_ascii=False, separators=(',', ':'))
    if os.path.abspath(SRC) != os.path.abspath(DST):
        open(f'{DST}/{book}-{ch}.sources.json', 'w').write(open(f'{SRC}/{book}-{ch}.sources.json').read())
    return len(d['verses']), sum(1 for v in d['verses'] if v['siteNote']), sum(1 for v in d['verses'] if v['lost'])

stats = collections.Counter()
for f in sorted(glob.glob(f'{SRC}/*.json')):
    m = re.match(r'^(.*)-(\d+)\.json$', os.path.basename(f))
    if not m: continue
    book, ch = m.group(1), int(m.group(2))
    if ONLY and book not in ONLY: continue
    n, sn, lo = compile_chapter(book, ch)
    stats['chapters'] += 1; stats['verses'] += n; stats['siteNote'] += sn; stats['lost'] += lo
print(json.dumps(stats))
