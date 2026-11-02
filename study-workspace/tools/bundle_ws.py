"""Pack the Study Workspace chapter files into gzip bundles for the staging helper's wsdata job."""
import json,glob,os,gzip,hashlib,re,collections
import sys
SRC=sys.argv[1] if len(sys.argv)>1 else '/home/claude/work/ws/out'; DST=sys.argv[2] if len(sys.argv)>2 else '/home/claude/latin-translation/study-workspace/data'
os.makedirs(DST,exist_ok=True)
for f in glob.glob(DST+'/*.json.gz'): os.remove(f)
by=collections.OrderedDict()
def key(n):
    m=re.match(r'^(.*)-(\d+)(\.sources)?\.json$',n); return (m.group(1),int(m.group(2)),bool(m.group(3)))
for n in sorted(os.listdir(SRC),key=key):
    by.setdefault(key(n)[0],[]).append(n)
manifest={'bundles':[],'files':{}}
for book,names in by.items():
    parts=[];cur={};sz=0
    for n in names:
        c=open(f'{SRC}/{n}',encoding='utf-8').read()
        manifest['files'][n]=hashlib.md5(c.encode()).hexdigest()
        if sz+len(c.encode())>8_000_000 and cur: parts.append(cur);cur={};sz=0
        cur[n]=c; sz+=len(c.encode())
    parts.append(cur)
    for i,p in enumerate(parts,1):
        name=f'{book}.json.gz' if len(parts)==1 else f'{book}-part{i}.json.gz'
        raw=json.dumps({'files':p},ensure_ascii=False,separators=(',',':')).encode()
        gz=gzip.compress(raw,9,mtime=0)
        open(f'{DST}/{name}','wb').write(gz)
        manifest['bundles'].append({'name':name,'files':len(p),'raw':len(raw),'gz':len(gz),'sha256':hashlib.sha256(gz).hexdigest()})
json.dump(manifest,open(f'{DST}/manifest.json','w'),indent=1)
print(len(manifest['bundles']),'bundles',sum(b['gz'] for b in manifest['bundles']),'bytes gz',len(manifest['files']),'files')
