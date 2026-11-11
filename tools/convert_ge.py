"""Experimental indexed-mesh conversion of locally extracted GoldenEye XBLA CAFF.
Based on structural analysis documented by mscrnt/Sightline xblaworld.py.
No texture decoding; unsupported faces are discarded.
"""
import math, struct
from caff_min import parse
STRIDES=(12,16,20,24,28,32,36,40,44,48,52,56,64)

def modelparts(path):
    b=parse(path);texnames={t["name"] for t in b["texs"]}
    models=[e for e in b["ents"] if e["sec"]==".gpu" and e["kind"]==5 and e["name"] not in texnames]
    streamed={e["name"] for e in b["ents"] if e["sec"]==".stream" and e["size"]>0}
    model=max(models,key=lambda e:(e["name"] in streamed,e["size"]))
    def part(sec):
        entries=[e for e in b["ents"] if e["sec"]==sec and e["name"]==model["name"]]
        if not entries:return b""
        e=max(entries,key=lambda e:e["size"])
        return b["data"][b["base"][sec]+e["off"]:][:e["size"]]
    blob=b["data"][b["base"][".gpu"]+model["off"]:][:model["size"]]
    return b,blob,part(".data"),part(".stream")

def records(stream):
    if len(stream)<4:return []
    start=struct.unpack_from(">I",stream)[0]
    if start<4 or start>len(stream) or start%4:return []
    header=struct.unpack_from(">%dI"%(start//4),stream)
    end=min([w for w in header if start<w<=len(stream)]+[len(stream)])
    recs=[];at=start
    while at+4<=end:
        word=struct.unpack_from(">I",stream,at)[0]
        size=word>>16;op=(word>>8)&255
        if size<4 or size%4 or at+size>end:break
        args=struct.unpack_from(">%dI"%(size//4-1),stream,at+4) if size>4 else ()
        recs.append((at,op,args));at+=size
    return recs

def expand(prim,ids):
    out=[]
    if prim==4:
        for i in range(0,len(ids)-2,3):out.extend(ids[i:i+3])
    elif prim==5:
        for i in range(1,len(ids)-1):out.extend((ids[0],ids[i],ids[i+1]))
    elif prim==13:
        for i in range(0,len(ids)-3,4):
            out.extend((ids[i],ids[i+1],ids[i+2],ids[i],ids[i+2],ids[i+3]))
    return out

def vertex(blob,offset,stride):
    if offset+stride>len(blob):return None
    position=struct.unpack_from(">fff",blob,offset+(4 if stride==36 else 0))
    if any(not math.isfinite(x) or abs(x)>1e6 for x in position):return None
    c=blob[offset+stride-4:offset+stride]
    return position,[c[3]/255,c[2]/255,c[1]/255]

def convert(path):
    _,blob,graph,stream=modelparts(path)
    recs=records(stream)
    draws=[(at,a[0],a[1],a[2]) for at,op,a in recs
           if op in (1,0x30) and len(a)>=3 and a[0] in (4,5,13) and a[1]>2]
    words=struct.unpack(">%dI"%(len(graph)//4),graph[:len(graph)//4*4])
    wanted={}
    for at,prim,count,handle in draws:
        wanted.setdefault(handle,set()).update(((count*2,1),(count*4,6)))
    index_records={}
    for i in range(len(words)-3):
        handle=words[i]
        if handle not in wanted:continue
        off,ln,kind=words[i+1:i+4]
        if (ln,kind) in wanted[handle] and off+ln<=len(blob):
            index_records.setdefault(handle,set()).add((off,ln,kind))
    runs=[]
    for off,ln,kind in sorted({x for arr in index_records.values() for x in arr}):
        if runs and off<=runs[-1][1]+4:
            runs[-1][1]=max(runs[-1][1],off+ln)
        else:runs.append([off,off+ln])
    pool_for_run={}
    for ri,(start,end) in enumerate(runs):
        matches=[]
        for i in range(len(words)-3):
            stride,off,ln=words[i],words[i+2],words[i+3]
            if stride in STRIDES and ln and ln%stride==0 and off+ln==start and off+ln<=len(blob):
                matches.append((off,stride,ln//stride))
        if matches:pool_for_run[ri]=max(matches,key=lambda x:x[2])
    poolmap={};meshes=[];skipped={}
    is_level="/background/" in str(path).replace("\\","/")
    bounds=struct.unpack_from(">7f",graph,0x34) if is_level else None
    for at,prim,count,handle in draws:
        candidates=[x for x in index_records.get(handle,[]) if x[1] in (count*2,count*4)]
        if len(candidates)!=1:
            skipped["index"]=skipped.get("index",0)+1;continue
        off,ln,kind=candidates[0]
        ri=next((i for i,(a,b) in enumerate(runs) if a<=off and off+ln<=b),None)
        if ri is None or ri not in pool_for_run:
            skipped["pool"]=skipped.get("pool",0)+1;continue
        vo,st,nv=pool_for_run[ri]
        fmt=">%d%s"%(count,"H" if kind==1 else "I")
        ids=list(struct.unpack_from(fmt,blob,off))
        if max(ids)>=nv:
            skipped["range"]=skipped.get("range",0)+1;continue
        key=(vo,st,nv)
        if key not in poolmap:
            poolmap[key]=[vertex(blob,vo+j*st,st) for j in range(nv)]
        vertices=poolmap[key];valid=vertices
        if is_level:
            centre,extent=bounds[1:4],bounds[4:7]
            valid=[v if v is not None and all(
                abs(v[0][axis]-centre[axis])<=abs(extent[axis])*1.15+2 for axis in range(3)
            ) else None for v in vertices]
        triangle_ids=expand(prim,ids)
        good=[x for j in range(0,len(triangle_ids),3)
              if all(valid[z] is not None for z in triangle_ids[j:j+3])
              for x in triangle_ids[j:j+3]]
        if good:meshes.append((key,good))
    return meshes,poolmap,dict(draws=len(draws),meshes=len(meshes),
                              triangles=sum(len(ids)//3 for _,ids in meshes),skipped=skipped)
