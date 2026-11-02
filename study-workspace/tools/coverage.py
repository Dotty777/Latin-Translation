"""Usage: coverage.py [OUT_DIR] [CSV] [book,book,...]. Count what each Study Workspace chapter holds; writes coverage.csv and prints book totals as JSON."""
import json,glob,collections,csv,re,sys
OUT=sys.argv[1] if len(sys.argv)>1 else '/home/claude/work/ws/out'
NAMES=sys.argv[3].split(',') if len(sys.argv)>3 else ['genesis','exodus','leviticus','numbers','deuteronomy','matthew','mark','luke','john','psalms','proverbs','ecclesiastes','song-of-songs','lamentations','wisdom-of-solomon','sirach','revelation']
cols=['chapter','verses','rated_hebrew','rated_latin','rated_kjv','unrated','src_hebrew','src_latin','src_kjv','src_saints','src_study','src_disparate','words','headings','chapter_notes','prose']
rows=[];books={}
for b in NAMES:
    bc=collections.Counter()
    chs=sorted(int(re.search(r'-(\d+)\.json$',f).group(1)) for f in glob.glob(f'{OUT}/{b}-*.json') if re.search(rf'/{b}-\d+\.json$',f))
    for ch in chs:
        d=json.load(open(f'{OUT}/{b}-{ch}.json')); s=json.load(open(f'{OUT}/{b}-{ch}.sources.json'))
        c=collections.Counter(chapters=1)
        for v in d['verses']:
            c['verses']+=1
            for col in ('hebrew','latin','kjv'):
                if (v.get('ratings') or {}).get(col): c['rated_'+col]+=1
            if not v.get('ratings'): c['unrated']+=1
            c['words']+=len(v['words']); c['prose']+=1 if v.get('received') else 0
        for srcs in s['verses'].values():
            for x in srcs: c['src_'+x['kind']]+=1
        c['headings']=len(d['headings']); c['chapter_notes']=len(s['chapter'])
        rows.append({'chapter':f'{b}-{ch}',**{k:c[k] for k in cols[1:]}})
        bc.update(c)
    books[b]=dict(bc)
w=csv.DictWriter(open(sys.argv[2] if len(sys.argv)>2 else '/home/claude/latin-translation/study-workspace/coverage.csv','w',newline=''),fieldnames=cols); w.writeheader(); w.writerows(rows)
print(json.dumps(books))
