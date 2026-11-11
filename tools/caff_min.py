"""Parse CAFF bundles from the user's locally extracted XBLA files.
Format documentation: mscrnt/Sightline tools/texpack/caff.py.
"""
import re, struct
from pathlib import Path

def parse(path):
    data=Path(path).read_bytes()
    offset=data.find(b"CAFF",0,16384)
    if offset<0: raise ValueError("CAFF header not found")
    d=data[offset:]
    secs=[]
    for n in (b".gpu",b".data",b".stream"):
        i=d.find(n+b"\0",0,0x400)
        if i>=0:secs.append((i,n.decode()))
    if not secs:raise ValueError("No sections")
    secs=[n for _,n in sorted(secs)]
    last=max(d.find(s.encode()+b"\0",0,0x400) for s in secs)
    last=d.find(b"\0",last)+1
    match=re.search(rb"[A-Za-z]:\\",d[last:last+0x400])
    if match is None:raise ValueError("No string table")
    start=match.start()+last
    n=(start-last-4)//4
    offsets=struct.unpack(">%dI"%n,d[last+4:last+4+n*4])
    names=[d[start+o:d.find(b"\0",start+o)].decode("latin1") for o in offsets]
    adb=d.find(b".adb\0")
    if adb>=0:p=adb+5
    else:
        m=re.search(rb"default\.rba\0",d)
        if m is None:raise ValueError("No resource table")
        p=m.end()
    while p<len(d) and d[p]==0:p+=1
    p-=3
    ents=[]
    while p+14<=len(d):
        nm,off,sz,sec,kind=struct.unpack_from(">IIIBB",d,p)
        if nm==0 or nm>4000 or sec==0 or sec>len(secs):break
        ents.append(dict(name=nm,off=off,size=sz,sec=secs[sec-1],kind=kind))
        p+=14
    ext={}
    for e in ents:ext[e["sec"]]=max(ext.get(e["sec"],0),e["off"]+e["size"])
    header=(len(d)-sum(ext.values()))&~3
    def bases(h):
        b={};off=h
        for s in secs:b[s]=off;off+=ext.get(s,0)
        return b
    base=bases(header)
    first=next((e for e in ents if e["sec"]==".data" and e["size"]==0x70),None)
    if first:
        for delta in (0,-4,4,-8,8,-12,12,-16,16):
            at=base[".data"]+first["off"]+delta
            if d[at:at+8]==b"texture\0":
                header+=delta;base=bases(header);break
        else:raise ValueError("Could not validate data section")
    texs=[]
    for e in ents:
        if e["sec"]!=".data" or e["size"]!=0x70:continue
        at=base[".data"]+e["off"];r=d[at:at+0x70]
        if r[:8]!=b"texture\0":continue
        flags,_,_,w,h,poff,psz,mips=struct.unpack(">IIIHHIIB",r[0x18:0x31])
        texs.append(dict(name=e["name"],fmt=flags&63,w=w,h=h,poff=poff,psz=psz,mips=mips))
    return dict(data=d,ents=ents,base=base,names=names,texs=texs,hdr=header,ext=ext)
