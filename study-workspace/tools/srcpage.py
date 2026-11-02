import json,glob,re
TOT={}
for f in glob.glob('/home/claude/work/ws/pg-*.json'):
    for u,v in json.load(open(f)).items(): TOT[u.split('.com',1)[1]]=v[0]
_cache={}
def page(path):
    """path like /bible/.../comparison-edition/6/ -> html of that page part (nextpage split)"""
    m=re.match(r'(.*/)(\d+)/$',path)
    part=1
    if m and m.group(1) in TOT and path not in TOT: path,part=m.group(1),int(m.group(2))
    pid=TOT[path]
    if pid not in _cache: _cache[pid]=open(f'/home/claude/work/pages/{pid}.html').read().split('<!--nextpage-->')
    parts=_cache[pid]
    return parts[part-1] if part<=len(parts) else ''
def split_url(url):
    p=url.split('.com',1)[1]; path,_,anchor=p.partition('#'); return path,anchor
