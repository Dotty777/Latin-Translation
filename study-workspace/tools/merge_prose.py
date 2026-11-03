"""Merge authored study prose into a compiled Study Workspace chapter record.

usage: merge_prose.py <prose.py> [DST=/home/claude/work/ws/outc]

The prose module defines CHAPTER = {
  'slug': 'genesis', 'chapter': 2,
  'chapterNote': '...prose...',
  'headings': [...] (optional, keeps the compiled ones if absent),
  'verses': { '2:1': { 'received': ..., 'explain': ..., 'shared': [...],
                       'instructions': [{'type','basis','text'}], 'entries': [...],
                       'lost': [{'dir': 'keeps'|'loses'|'between', 'text': ...}],
                       'flags': [...] (optional) }, ... } }
Lexicon entries are drawn from ws/lexicon-catalogue.json (built from the site's lexicon pages).
"""
import json, sys, re, os, importlib.util, datetime

OUTC = '/home/claude/work/ws/outc'
CAT = json.load(open('/home/claude/work/ws/lexicon-catalogue.json', encoding='utf-8'))
BOILER = [
    r"^This entry studies a name or designation (?:of God in the Father/Creator section|associated with the Holy Spirit|applied to Jesus Christ in its cited context)\.\s*",
    r"^(?:Shared titles are not restricted to the Father in every passage|its stated contextual and interpretive qualifications remain in force|Ordinary uses and other bearers of the same name are distinct)\.\s*",
    r"^(?:divine name or title|title or designation|English translation convention|historical rendering of YHWH|Creature in the temptation narrative|Divine|Heavenly beings and sanctuary represent\w*)\s+",
]
CUT = re.compile(r"\s*(?:Scope:|Overview sources and context:|Read in context:|Verse references:|Read the sources:|Related:|Back to the term index|Greek: \S+ · \S+ Original-language source|Biblical context:).*$")

def lexicon_text(lid):
    e = CAT[lid]; t = e['text']
    for b in BOILER:
        t = re.sub(b, '', t)
    # drop the quoted verse and its edition line: "... Genesis 2:7 · World English Bible Classic (WEB) "
    m = re.search(r"\b[1-3]?\s?[A-Z][a-z]+(?: of [A-Z][a-z]+)? \d+:\d+(?:[–-]\d+)? · ", t)
    if m:
        rest = t[m.end():]
        k = re.search(r"\((?:WEB|KJV|JPS|LGNT|NA28)[^)]*\)\s+", rest)
        if not (k and k.end() < 140): k = re.search(r"(?:Bible|Version)\s+(?=[A-Z])", rest)
        if k and k.end() < 140: t = rest[k.end():]
    t = re.sub(r"^Greek biblical textual tradition · LXX = seventy\s+", '', t)
    t = CUT.sub('', t).strip()
    # trim to whole sentences, about 420 characters
    if len(t) > 440 or not t.endswith(('.', '”', '.)')):
        cut = t[:440]; i = max(cut.rfind('. '), cut.rfind('.”'), cut.rfind('.) '))
        t = cut[:i+1] if i > 120 else cut.rstrip()
    return t

def main():
    src = sys.argv[1]; dst = sys.argv[2] if len(sys.argv) > 2 else OUTC
    spec = importlib.util.spec_from_file_location('prose', src); mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    P = mod.CHAPTER; key = f"{P['slug']}-{P['chapter']}"
    path = f"{dst}/{key}.json"; d = json.load(open(path, encoding='utf-8'))
    refs = {v['ref']: v for v in d['verses']}
    missing = [r for r in refs if r not in P['verses']]; extra = [r for r in P['verses'] if r not in refs]
    if missing or extra: print('WARNING missing prose for', missing, 'extra prose for', extra)
    used = []
    for ref, pv in P['verses'].items():
        if ref not in refs: continue
        v = refs[ref]
        for k in ('received', 'explain'):
            v[k] = pv[k].strip()
        v['shared'] = [s.strip() for s in pv['shared']]
        v['instructions'] = [{'type': i['type'], 'basis': i['basis'], 'text': i['text'].strip()} for i in pv['instructions']]
        v['entries'] = list(pv.get('entries', []))
        for e in v['entries']:
            assert e in CAT, f'unknown lexicon id {e} at {ref}'
            if e not in used: used.append(e)
        v['lost'] = [{'dir': l['dir'], 'text': l['text'].strip()} for l in pv['lost']]
        for l in v['lost']: assert l['dir'] in ('keeps', 'loses', 'between'), (ref, l)
        if 'flags' in pv: v['flags'] = list(pv['flags'])
        assert v['shared'] and v['received'] and v['explain'], ref
    d['lexicon'] = {e: {'name': CAT[e]['name'].lstrip('✦ ').strip(), 'group': CAT[e]['group'], 'text': lexicon_text(e), 'link': f"/study-guides/{CAT[e]['page']}/#{e}"} for e in used}
    d['chapterNote'] = {'lost': P['chapterNote'].strip()}
    if P.get('headings'): d['headings'] = P['headings']
    d['status'] = 'Draft for review'
    d['generated'] = datetime.date.today().isoformat()
    json.dump(d, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    n = sum(1 for v in d['verses'] if v['received'])
    print(key, 'verses with prose', n, 'of', len(d['verses']), 'lexicon', used, 'bytes', os.path.getsize(path))

if __name__ == '__main__':
    main()
