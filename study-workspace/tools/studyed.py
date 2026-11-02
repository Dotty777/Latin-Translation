import sys,re; sys.path.insert(0,'/home/claude/work/lib')
from bs4 import BeautifulSoup, Tag
from extract import segs, ptext, rel
STUDY={'genesis':23385,'exodus':23433,'leviticus':23383,'numbers':23407,'deuteronomy':23431,'psalms':23852,'proverbs':23743,'ecclesiastes':23840,'song-of-songs':23874,'lamentations':23889,'wisdom-of-solomon':23904,'sirach':23917,'joshua':23738,'judges':23805,'ruth':23639,'1-samuel':23594,'2-samuel':23621,'1-kings':23521,'2-kings':23540,'1-chronicles':23553,'2-chronicles':23569,'1-maccabees':23580,'2-maccabees':23456,'ezra':23467,'nehemiah':23483,'esther':23631,'job':23501}
DISP={'genesis':18883,'exodus':18960,'leviticus':18961,'numbers':18962,'deuteronomy':18963,'song-of-songs':18635,'joshua':18878,'judges':18880,'ruth':18882,'1-samuel':18870,'2-samuel':18874,'1-kings':18868,'2-kings':18872,'1-chronicles':18867,'2-chronicles':18871,'1-maccabees':18869,'2-maccabees':18873,'ezra':18876,'nehemiah':18881,'esther':18875,'job':18877}
DIV={'genesis':'law','exodus':'law','leviticus':'law','numbers':'law','deuteronomy':'law','psalms':'wisdom','proverbs':'wisdom','ecclesiastes':'wisdom','song-of-songs':'wisdom','lamentations':'wisdom','wisdom-of-solomon':'wisdom','sirach':'wisdom','matthew':'salvation','mark':'salvation','luke':'salvation','john':'salvation','revelation':'glory','joshua':'judgement','judges':'judgement','ruth':'judgement','1-samuel':'judgement','2-samuel':'judgement','1-kings':'judgement','2-kings':'judgement','1-chronicles':'judgement','2-chronicles':'judgement','1-maccabees':'judgement','2-maccabees':'judgement','ezra':'judgement','nehemiah':'judgement','esther':'judgement','job':'judgement'}
def expand(text, ch_default):
    """'3:8–10' / '3:20, 3:24' / '8:4–5, 8:8' -> list of (ch,verse str)"""
    out=[]; ch=ch_default
    for part in re.split(r'[,;]\s*',text):
        part=part.strip().replace('—','–').replace('-','–')
        m=re.match(r'^(?:(\d+):)?(\d+)([a-z]?)(?:–(?:(\d+):)?(\d+)([a-z]?))?',part)
        if not m: continue
        if m.group(1): ch=int(m.group(1))
        v1=int(m.group(2)); 
        if m.group(5):
            ch2=int(m.group(4)) if m.group(4) else ch
            if ch2!=ch:
                out.append((ch,str(v1)+m.group(3))); out.append((ch2,m.group(5)+m.group(6))); ch=ch2; continue
            for v in range(v1,int(m.group(5))+1): out.append((ch,str(v)))
        else: out.append((ch,str(v1)+m.group(3)))
    return out
def study_edition(book):
    """-> {ch: {'verses':{v:[(title,text,href)]}, 'chapter':[{'title','text'}], 'summary':str}}"""
    pid=STUDY.get(book)
    if not pid: return {}
    s=BeautifulSoup(open(f'/home/claude/work/pages/{pid}.html').read(),'lxml')
    path=f'/bible/{DIV[book]}/{book}/study/'
    res={}
    for blk in s.find_all(class_='ss-study-anchor'):
        m=re.match(rf'^{re.escape(book)}-(\d+)$',blk.get('id') or '')
        if not m:
            m=re.match(r'^[a-z0-9-]*?-(\d+)$',blk.get('id') or '')
            if not m: continue
        ch=int(m.group(1)); d=res.setdefault(ch,{'verses':{},'chapter':[],'summary':'','anchor':blk.get('id')})
        det=blk.find('details') or blk
        summ=det.find('summary'); d['summary']=re.sub(r'\s+',' ',summ.get_text(' ')).strip() if summ else ''
        cur_title=''; chap=[]
        for c in det.children:
            if not isinstance(c,Tag) or c.name=='summary': continue
            if c.name in('ul','ol'):
                for li in c.find_all('li',recursive=False):
                    a=li.find('a',href=True); st=li.find('strong')
                    if a and st and a in st.descendants and re.search(r'#v\d+-\d+',a['href']):
                        refs=expand(a.get_text(),ch)
                        sg=segs(li)
                        # drop the leading ref link and dash
                        if isinstance(sg,list):
                            sg=sg[1:] if sg and isinstance(sg[0],list) else sg
                            if sg and isinstance(sg[0],str): sg[0]=re.sub(r'^\s*[—–-]\s*','',sg[0])
                            if len(sg)==1 and isinstance(sg[0],str): sg=sg[0]
                        label=a.get_text().strip()
                        for (cc,v) in refs:
                            res.setdefault(cc,{'verses':{},'chapter':[],'summary':'','anchor':blk.get('id')})['verses'].setdefault(v,[]).append({'ref':label,'text':sg})
                    else:
                        t=segs(li)
                        if ptext(t).strip(): chap.append((cur_title,t))
            elif c.name=='p':
                t=segs(c); tx=ptext(t).strip()
                if not tx or tx.startswith('Read ') and tx.endswith('→'): continue
                if c.find('strong') and len(c.get_text(strip=True))<60 and c.get_text(strip=True)==c.find('strong').get_text(strip=True):
                    cur_title=c.get_text(strip=True); continue
                chap.append((cur_title,t))
        # group chapter notes by title
        secs=[]
        for t,x in chap:
            if secs and secs[-1]['title']==t: secs[-1]['text'].append(x)
            else: secs.append({'title':t,'text':[x]})
        res[ch]['chapter']=secs
    return res, path
def disparate(book):
    pid=DISP.get(book)
    if not pid: return {},None
    from extract import group, flatten, tidy, rating_of, fixhref
    s=BeautifulSoup(open(f'/home/claude/work/pages/{pid}.html').read(),'lxml')
    path=f'/bible/{DIV[book]}/{book}/disparate-study/'
    res={}
    for art in s.find_all(id=re.compile(r'^study-\d+-\d+[a-z]?$')):
        m=re.match(r'^study-(\d+)-(\d+[a-z]?)$',art['id']); ch=int(m.group(1)); v=m.group(2)
        h=art.find(['h2','h3']); title=re.sub(r'\s+',' ',h.get_text(' ')).strip() if h else ''
        badge=art.find(class_='badge'); badge=re.sub(r'\s+',' ',badge.get_text(' ')).strip() if badge else ''
        secs=group(flatten(art,[]))
        secs=[x for x in secs if x['title']!=title]
        for sec in secs: sec['text']=[fixhref(t,path) for t in sec['text']]
        secs=tidy(secs)
        res.setdefault(ch,{})[v]={'title':title,'badge':badge,'sections':secs,'link':path+'#'+art['id']}
    return res,path
