"""Build sources-only Study Workspace data for the Law, Salvation, Wisdom and Glory divisions."""
import sys,json,re,os,collections
sys.path.insert(0,'/home/claude/work/lib')
import srcpage
from srcpage import page, split_url
from extract import extract, tidy, ptext
from saintspage import saints_page
from studyed import study_edition, disparate, DIV
W='/home/claude/work/ws'
import os as _os
OUTDIR=_os.environ.get('WS_OUT',W+'/out')
GEN=json.load(open(f'{W}/gen-chapter-ids.json'))
for slug,pid in GEN.items(): srcpage.TOT[f'/bible/law/genesis/{slug}/']=pid
NAMES={'genesis':'Genesis','exodus':'Exodus','leviticus':'Leviticus','numbers':'Numbers','deuteronomy':'Deuteronomy','matthew':'Matthew','mark':'Mark','luke':'Luke','john':'John','psalms':'Psalms','proverbs':'Proverbs','ecclesiastes':'Ecclesiastes','song-of-songs':'Song of Songs','lamentations':'Lamentations','wisdom-of-solomon':'Wisdom of Solomon','sirach':'Sirach','revelation':'Revelation','joshua':'Joshua','judges':'Judges','ruth':'Ruth','1-samuel':'1 Samuel','2-samuel':'2 Samuel','1-kings':'1 Kings','2-kings':'2 Kings','1-chronicles':'1 Chronicles','2-chronicles':'2 Chronicles','1-maccabees':'1 Maccabees','2-maccabees':'2 Maccabees','ezra':'Ezra','nehemiah':'Nehemiah','esther':'Esther','job':'Job','isaiah':'Isaiah','jeremiah':'Jeremiah','ezekiel':'Ezekiel','daniel':'Daniel','hosea':'Hosea','joel':'Joel','amos':'Amos','obadiah':'Obadiah','jonah':'Jonah','micah':'Micah','nahum':'Nahum','habakkuk':'Habakkuk','zephaniah':'Zephaniah','haggai':'Haggai','zechariah':'Zechariah','malachi':'Malachi'}
RANK={'Same':0,'Similar':1,'Different':2,'Divergent':3,'Disparate':4}
LABEL={'hebrew':'Hebrew and Greek','latin':'Latin and Greek','kjv':'King James and Greek','saints':'Saints Translation notes','study':'Study Edition','disparate':'Disparate Study'}
TODAY='2026-11-02'
def vkey(ref): return ref.split(':',1)[1]
def readings(cols):
    out={}
    for col in ('saints','hebrew','latin','kjv'):
        an=cols.get(col) or {}
        out[col]=' '.join(x['text'].strip() for x in an.values() if x.get('text')).strip()
    return out
def words_for(notes, ref):
    v=(notes.get('v') or {}).get(ref) or {}
    out=[]; seen=set()
    for u in v.get('u') or []:
        if u.get('k')!='ws': continue
        w=(notes.get('ws') or {}).get(u.get('id'))
        if not w or u['id'] in seen: continue
        seen.add(u['id'])
        out.append({'word':w.get('w',''),'greek':w.get('o',''),'literal':w.get('l',''),'note':w.get('n',''),'see':w.get('a',''),'theme':w.get('t',''),'kind':w.get('k',''),'colour':w.get('c','')})
    return out
def build_book(book, stats):
    pd=json.load(open(f'{W}/pd-{book}.json'))
    se=study_edition(book); se,se_path=(se if se else ({},None))
    dsp,dsp_path=disparate(book)
    for ch_s in sorted(pd,key=int):
        ch=int(ch_s); rows=pd[ch_s]
        valid=set(vkey(r) for r in rows)
        notes=json.load(open(f'{W}/notes/{book}-{ch}.json')) if os.path.exists(f'{W}/notes/{book}-{ch}.json') else {}
        # saints page (chapter-N page; Genesis uses its own chapter pages)
        sp=f'/bible/law/genesis/chapter-{ch}/' if book=='genesis' else None
        if not sp:
            for r in rows.values():
                for x in (r.get('saints') or {}).values():
                    p,_=split_url(x['url'])
                    if 'compared' not in p: sp=p
                    break
                if sp: break
        vnotes,heads,chapsecs=({},[],[])
        if sp and sp in srcpage.TOT:
            vnotes,heads,chapsecs=saints_page(sp,page(sp),ch,valid)
        if not heads and book in('genesis',):
            pass
        verses=[]; sources={}
        for ref,cols in rows.items():
            v=vkey(ref); srcs=[]; ratings={}
            seen=set()
            for col in ('hebrew','latin','kjv'):
                for an in (cols.get(col) or {}).values():
                    path,anchor=split_url(an['url'])
                    if (path,anchor) in seen: continue
                    seen.add((path,anchor))
                    r=extract(path,anchor)
                    if r is None: stats['missing'][col]+=1; continue
                    secs=tidy(r['sections'])
                    if r['rating']: ratings[col]=max(ratings.get(col,''),r['rating'],key=lambda x:RANK.get(x,-1))
                    srcs.append({'kind':col,'label':LABEL[col],'rating':r['rating'] or '','badge':r['badge'],'link':path+'#'+anchor,'sections':secs})
                    stats['src'][col]+=1
            for n in vnotes.get(v,[]):
                srcs.append({'kind':'saints','label':LABEL['saints'],'rating':'','badge':'','link':sp+'#v%d-%s'%(ch,v),'sections':[n]}); stats['src']['saints']+=1
            for n in (se.get(ch,{}).get('verses',{}).get(v,[]) if se else []):
                srcs.append({'kind':'study','label':LABEL['study'],'rating':'','badge':'','link':se_path+'#'+se[ch]['anchor'],'sections':[{'title':n['ref'],'text':[n['text']]}]}); stats['src']['study']+=1
            d=(dsp.get(ch) or {}).get(v)
            if d:
                srcs.append({'kind':'disparate','label':LABEL['disparate'],'rating':'Disparate' if 'Disparate' in d['badge'] else '','badge':d['badge'],'link':d['link'],'title':d['title'],'sections':d['sections']}); stats['src']['disparate']+=1
            top=max(ratings.values(),key=lambda x:RANK[x]) if ratings else ''
            level='none' if not top else ('notable' if RANK[top]>=3 else ('minor' if RANK[top]>=1 else 'none'))
            first_link=srcs[0]['link'] if srcs else ''
            verses.append({'ref':ref,'readings':readings(cols),'badge':top,'level':level,'ratings':ratings,
                'received':'','explain':'','shared':[],'instructions':[],'entries':[],'lost':[],'flags':[],'siteNote':'','whyNote':'',
                'words':words_for(notes,ref),'link':first_link})
            sources[v]=srcs
            stats['verses']+=1
            if not ratings: stats['unrated']+=1
        chap=[]
        if chapsecs: chap.append({'label':'Saints Translation chapter notes','link':sp,'sections':chapsecs})
        if se and ch in se and (se[ch]['chapter'] or se[ch]['summary']):
            chap.append({'label':'Study Edition · '+(se[ch]['summary'] or f'{NAMES[book]} {ch}'),'link':se_path+'#'+se[ch]['anchor'],'sections':se[ch]['chapter']})
        data={'book':NAMES[book],'slug':book,'chapter':ch,'status':'Sources only · study notes not yet written','sourcesOnly':True,'generated':TODAY,
              'credit':'Source studies, word studies and cross-references are drawn from this site’s comparison pages, study editions and reference reviews. Open each source for its full text and citations.',
              'chapterNote':{'lost':''},'headings':heads,'lexicon':{},'verses':verses}
        json.dump(data,open(f'{OUTDIR}/{book}-{ch}.json','w'),ensure_ascii=False,separators=(',',':'))
        json.dump({'chapter':chap,'verses':sources},open(f'{OUTDIR}/{book}-{ch}.sources.json','w'),ensure_ascii=False,separators=(',',':'))
        stats['chapters']+=1
if __name__=='__main__':
    books=sys.argv[1:] or list(NAMES)
    stats={'chapters':0,'verses':0,'unrated':0,'src':collections.Counter(),'missing':collections.Counter()}
    for b in books:
        build_book(b,stats); print(b,'done',stats['chapters'],flush=True)
    stats['src']=dict(stats['src']); stats['missing']=dict(stats['missing'])
    print(json.dumps(stats))
