import sys,re; sys.path.insert(0,'/home/claude/work/lib')
from bs4 import BeautifulSoup, Tag
from extract import segs, ptext, flatten, group, fixhref, tidy
REF=re.compile(r'^\s*(?:\d+\.\s*)?(?:(?:[1-3]\s)?[A-Z][A-Za-z]+(?:\s(?:of|Of)\s[A-Z][a-z]+)*\s+)?(\d+):(\d+)([a-z]?)(?:\s*[–-]\s*(?:(\d+):)?(\d+))?')
def refs_from(text, ch):
    m=REF.match(text)
    if not m or int(m.group(1))!=ch: return []
    v1=int(m.group(2)); suf=m.group(3)
    if m.group(5) and not m.group(4):
        return [str(v) for v in range(v1,int(m.group(5))+1)]
    return [str(v1)+suf, str(v1)] if suf else [str(v1)]
def clean_paras(node,path):
    out=[]
    for p in node.find_all(['p','li','blockquote']):
        if p.find_parent(['li','blockquote']) and p.name!='blockquote' and p.find_parent(['li','blockquote']) is not node: 
            if p.find_parent(['li','blockquote']) in node.find_all(['li','blockquote']): continue
        sg=segs(p)
        if isinstance(sg,list):
            sg=[x for x in sg if not (isinstance(x,list) and re.match(r'^(Return to|Back to)',x[0]))]
            while sg and isinstance(sg[-1],str) and sg[-1].strip(' ·;,')=='': sg=sg[:-1]
            if len(sg)==1 and isinstance(sg[0],str): sg=sg[0]
        if ptext(sg).strip(): out.append(fixhref(sg if p.name!='blockquote' else {'quote':sg},path))
    return out
def saints_page(path, html, ch, valid):
    s=BeautifulSoup(html,'lxml')
    vnotes={}; used=set()
    def add(vs,item):
        for v in vs:
            if v in valid: vnotes.setdefault(v,[]).append(item); return True
        return False
    # 1. details with a reference summary
    for d in s.find_all('details'):
        sm=d.find('summary')
        if not sm: continue
        t=re.sub(r'\s+',' ',sm.get_text(' ')).strip()
        vs=refs_from(t,ch)
        if not vs:
            m=re.match(r'^se-note-v(\d+)-(\d+[a-z]?)$',d.get('id') or '')
            if m and int(m.group(1))==ch: vs=[m.group(2)]
        if not vs: continue
        ps=clean_paras(d,path)
        if ps and add(vs,{'title':t,'text':ps}): used.add(id(d))
    # 2. numbered notes p[id*=note] "14. Genesis 3:1 Grammar. ..."
    for p in s.find_all('p',id=re.compile(r'note-\d+(-\d+[a-z]?)?$')):
        t=p.get_text(' ',strip=True)
        vs=refs_from(re.sub(r'^\d+\.\s*','',t),ch)
        if vs:
            sg=segs(p)
            if isinstance(sg,list):
                sg=[x for x in sg if not (isinstance(x,list) and re.match(r'^(Return to|Back to)',x[0]))]
                while sg and isinstance(sg[-1],str) and sg[-1].strip(' ·;,')=='': sg=sg[:-1]
            if add(vs,{'title':'','text':[fixhref(sg,path)]}): used.add(id(p))
    # headings + trailing chapter sections
    anchors=set(f'v{ch}-{v}' for v in valid)
    order=[]
    for el in s.find_all(True):
        if el.name=='h2' and not el.find_parent(['details','article']): order.append(('h',el))
        elif el.get('id') in anchors: order.append(('v',el))
    heads=[]; trailing=[]
    for i,(k,el) in enumerate(order):
        if k!='h': continue
        title=re.sub(r'\s+',' ',el.get_text(' ')).strip()
        nxt=None
        for k2,el2 in order[i+1:]:
            if k2=='h': break
            nxt=el2; break
        if nxt is not None:
            heads.append({'title':title,'ref':f"{ch}:{nxt['id'].split('-',1)[1]}"})
        elif not any(k2=='v' for k2,_ in order[i+1:]):
            trailing.append({'title':title,'node':el})
    chap=[]
    for t in trailing:
        el=t['node']; parent=el.parent
        # content: siblings after h2 until next h2
        ev=[]
        for sib in el.find_next_siblings():
            if sib.name=='h2': break
            if isinstance(sib,Tag):
                if sib.name=='details' or id(sib) in used: continue
                tmp=BeautifulSoup('<div></div>','lxml').div; 
                ev.extend(flatten_wrap(sib))
        secs=group([('h',t['title'])]+ev)
        for sec in secs:
            sec['text']=[fixhref(x,path) for x in sec['text'] if not (isinstance(x,str) and x.startswith('.') and '{' in x)]
        chap.extend([x for x in tidy(secs) if x['text']])
    return vnotes, heads, chap
def flatten_wrap(node):
    if node.name in('p','li','blockquote','ul','ol'):
        w=BeautifulSoup('<div></div>','lxml').div
        import copy; w.append(copy.copy(node)); return flatten(w,[])
    return flatten(node,[])
