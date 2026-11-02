import sys,re; sys.path.insert(0,'/home/claude/work/lib')
from srcpage import page
from bs4 import BeautifulSoup, NavigableString, Tag
CATS=['Same','Similar','Different','Divergent','Disparate']
SKIP_CLASS=re.compile(r'(^|-)(diff-help|word-help|eyebrow|rowref|ref|reference|label|layout|badge|grid|reading|readings|subverse|word-menu|compare|kjv-text|wp-block-columns)$')
NONEN={'la','he','el','grc','hbo','arc','syc'}
_soup={}
def soup(path):
    if path not in _soup:
        if len(_soup)>6: _soup.clear()
        _soup[path]=BeautifulSoup(page(path),'lxml')
    return _soup[path]
def rel(href):
    if not href: return href
    return re.sub(r'^https?://staging-8e0d-waywardnightjars\.wpcomstaging\.com','',href)
def segs(p):
    """paragraph -> list of str | [text,href]"""
    out=[]
    def walk(n):
        for c in n.children:
            if isinstance(c,NavigableString):
                out.append(str(c))
            elif isinstance(c,Tag):
                if c.name in('input','label','script','style','details'): continue
                if c.name=='a' and c.get('href'):
                    out.append([c.get_text(),rel(c['href'])])
                elif c.name=='br': out.append(' ')
                else: walk(c)
    walk(p)
    # merge strings, normalise space
    res=[]
    for s in out:
        if isinstance(s,str):
            if res and isinstance(res[-1],str): res[-1]+=s
            else: res.append(s)
        else: res.append(s)
    res=[re.sub(r'\s+',' ',s) if isinstance(s,str) else [re.sub(r'\s+',' ',s[0]).strip(),s[1]] for s in res]
    if res and isinstance(res[0],str): res[0]=res[0].lstrip()
    if res and isinstance(res[-1],str): res[-1]=res[-1].rstrip()
    res=[s for s in res if s!='' and s!=['','']]
    if len(res)==1 and isinstance(res[0],str): return res[0]
    return res
def ptext(x): return x if isinstance(x,str) else ''.join(s if isinstance(s,str) else s[0] for s in x)
def skip(tag):
    if tag.get('data-reading') is not None: return True
    if (tag.get('lang') or '').split('-')[0] in NONEN and tag.name in('p','div','blockquote'): return True
    for c in tag.get('class') or []:
        if SKIP_CLASS.search(c): return True
    return False
HEAD={'h2','h3','h4','h5','h6'}
def flatten(node,ev):
    for c in node.children:
        if not isinstance(c,Tag):
            t=re.sub(r'\s+',' ',str(c)).strip()
            if len(t)>2 and not t.startswith('wp:') and not t.startswith('/wp:'): ev.append(('p',t))
            continue
        if c.name in('details','script','style','input','label','summary','header','mark','fieldset','button','svg','img','sup'): continue
        if skip(c): continue
        if c.find(class_=re.compile(r'(^|-)badge($|-)')) is not None and c.name in('p','div'): continue
        if c.name in HEAD:
            ev.append(('h',re.sub(r'\s+',' ',c.get_text(' ')).strip())); continue
        if c.name in('p','li','blockquote','dd','dt','figcaption'):
            s=segs(c)
            if ptext(s).strip(): ev.append(('q' if c.name=='blockquote' else 'p',s))
        elif c.name in('span','em','strong','i','b','a','small','cite','abbr','code'):
            s=segs(c)
            if ptext(s).strip(): ev.append(('p',s))
        else:
            flatten(c,ev)
    return ev
def group(ev):
    secs=[];cur={'title':'','text':[]}
    for k,v in ev:
        if k=='h':
            if cur['text'] or cur['title']: secs.append(cur)
            cur={'title':v,'text':[]}
        else:
            cur['text'].append(v if k=='p' else {'quote':v})
    if cur['text'] or cur['title']: secs.append(cur)
    return [s for s in secs if s['text']]
def rating_of(e):
    txt=' '.join(x.get_text(' ') for x in e.find_all(class_=re.compile(r'badge'))[:2])
    cat=e.get('data-category') or ''
    for c in (e.get('class') or []):
        m=re.search(r'-(same|similar|different|divergent|disparate)$',c)
        if m: cat=cat or m.group(1).capitalize()
    for k in CATS:
        if re.search(r'\b'+k+r'\b',txt) and not cat: cat=k
    if cat not in CATS: cat=''
    return cat, re.sub(r'\s+',' ',txt).strip()
def card(e):
    while e.name in('span','a','strong','h3','h4') and e.parent is not None: e=e.parent
    return e
def fixhref(x,path):
    if isinstance(x,str): return x
    if isinstance(x,dict): return {'quote':fixhref(x['quote'],path)}
    return [[s[0], path+s[1] if s[1].startswith('#') else s[1]] if isinstance(s,list) else s for s in x]
def extract(path,anchor):
    s=soup(path); e=s.find(id=anchor)
    if e is None: return None
    e=card(e)
    cat,badge=rating_of(e)
    if not cat:
        first=e.find('p')
        if first is not None:
            m=re.match(r'^\s*\d+:\d+[a-z]?\s+(Same|Similar|Different|Divergent|Disparate)\s*$',first.get_text(' '))
            if m: cat=badge=m.group(1); first.decompose()
    secs=group(flatten(e,[]))
    for sec in secs: sec['text']=[fixhref(t,path) for t in sec['text']]
    return {'rating':cat,'badge':badge,'sections':secs,'tag':e.name,'cls':' '.join(e.get('class') or [])}
def saints_notes(path,anchor):
    """Saints chapter page: footnotes linked from the verse paragraph"""
    s=soup(path); e=s.find(id=anchor)
    if e is None: return None
    out=[]
    for a in e.find_all('a',href=True):
        h=a['href']
        if h.startswith('#') and h[1:]!=anchor:
            n=s.find(id=h[1:])
            if n is None: continue
            title=n.find('summary'); title=re.sub(r'\s+',' ',title.get_text(' ')).strip() if title else ''
            ps=[]
            for p in n.find_all(['p','li','blockquote']):
                sg=segs(p)
                if isinstance(sg,list): sg=[x for x in sg if not (isinstance(x,list) and x[0].startswith('Return to'))]
                    
                t=ptext(sg).strip(' ·')
                if t: ps.append(fixhref(sg if not isinstance(sg,list) or len(sg)!=1 or not isinstance(sg[0],str) else sg[0],path))
            if ps: out.append({'title':title,'text':ps})
    return out

LAYER_RE=re.compile(r'^(\d)\.\s+([^.·]{3,90}?)\s*(?:\.|·)(?:\s+(.*)|)$',re.S)
KNOWN=['Wording and meaning','Rabbinic understanding','Text and reception together','Direct word comparison','Saints’ teaching and understanding','How and why the differences arose','Further study','Saints and Christian understanding','How and why the difference arose','Classification and synthesis','Rabbinic teaching and understanding','Meaning and context','Reception source','How the difference arose','KJV ↔ Greek-English','Apostolic comparison','Saints reception — thematic comparison','Saints reception — quotation','Saints reception']
KNOWN_RE=re.compile(r'^(?:(\d)\.\s+)?('+'|'.join(re.escape(k) for k in KNOWN)+r')\s*[.:]\s*(.*)$',re.S)
def split_known(secs):
    out=[]
    for s in secs:
        if s['title']!='' or not any(KNOWN_RE.match(ptext(t)) for t in s['text'] if not isinstance(t,dict)):
            out.append(s); continue
        cur={'title':'','text':[]}; out.append(cur)
        for t in s['text']:
            m=KNOWN_RE.match(t) if isinstance(t,str) else None
            if m is None and isinstance(t,list) and t and isinstance(t[0],str):
                m0=KNOWN_RE.match(t[0])
                if m0:
                    cur={'title':m0.group(2),'text':[[m0.group(3)]+t[1:]]}; out.append(cur); continue
            if m:
                cur={'title':m.group(2),'text':[m.group(3)] if m.group(3).strip() else []}; out.append(cur)
            else: cur['text'].append(t)
    return [s for s in out if s['text']]
def tidy(secs):
    secs=split_known(secs)
    """split untitled sections whose paragraphs begin '1. Title. text'; trim stray separators"""
    out=[]
    for s in secs:
        if s['title']=='' and any(isinstance(t,str) and LAYER_RE.match(t) for t in s['text']):
            cur=None
            for t in s['text']:
                m=LAYER_RE.match(t) if isinstance(t,str) else None
                if m is None and isinstance(t,list) and t and isinstance(t[0],str): 
                    m0=LAYER_RE.match(t[0])
                    if m0: m=m0; t=[m0.group(3)]+t[1:]; title=m0.group(1)+'. '+m0.group(2); cur={'title':title,'text':[t]}; out.append(cur); continue
                if m:
                    cur={'title':m.group(1)+'. '+m.group(2),'text':[m.group(3)] if (m.group(3) or '').strip() else []}; out.append(cur)
                elif cur is not None: cur['text'].append(t)
                else:
                    cur={'title':'','text':[t]}; out.append(cur)
        else: out.append(s)
    for s in out:
        new=[]
        for t in s['text']:
            if isinstance(t,list):
                while t and isinstance(t[-1],str) and t[-1].strip(' ·;,')=='' : t=t[:-1]
                if len(t)==1 and isinstance(t[0],str): t=t[0]
            if isinstance(t,list) and len(t)==1 and isinstance(t[0],list) and t[0][0].startswith('Read the passage research'): continue
            if ptext(t if not isinstance(t,dict) else t['quote']).strip(): new.append(t)
        s['text']=new
    return [s for s in out if s['text']]
