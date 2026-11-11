"""Decode Xbox 360 tiled/DXT textures from user-supplied CAFF assets.
Output: PNGs and numbered material texture index. Not a game-file downloader.
Format reference: mscrnt/Sightline tools/texpack/xdecode.py.
Requires: pip install numpy pillow
Usage: python tools/decode_textures.py local-assets/files/new/background/facility/default.bin textures/facility
"""
from pathlib import Path
from PIL import Image
import numpy as np
import json,sys
from caff_min import parse

FORMATS={2:(1,1,1),6:(1,1,4),18:(4,4,8),19:(4,4,16),20:(4,4,16)}

def untile(raw,w,h,bpp,origin=(0,0)):
    x0,y0=origin
    aw=(w+31)//32*32;ah=(h+31)//32*32
    if x0+w>aw or y0+h>ah:raise ValueError("packed texture out of range")
    arr=np.frombuffer(raw[:aw*ah*bpp].ljust(aw*ah*bpp,b"\0"),dtype=np.uint8).reshape(-1,bpp)
    y,x=np.mgrid[y0:y0+h,x0:x0+w]
    log=(bpp>>2)+((bpp>>1)>>(bpp>>2))
    mac=((x>>5)+(y>>5)*(aw>>5))<<(log+7)
    mic=(((x&7)+((y&6)<<2))<<log)
    off=mac+((mic&~15)<<1)+(mic&15)+((y&8)<<(3+log))+((y&1)<<4)
    idx=(((off&~511)<<3)+((off&448)<<2)+(off&63)+((y&16)<<7)+(((((y&8)>>2)+(x>>3))&3)<<6))>>log
    return arr[np.clip(idx,0,len(arr)-1)]

def color(blocks,four_only=False):
    b=blocks.astype(np.uint32)
    a=(b[...,0]<<8)|b[...,1];c=(b[...,2]<<8)|b[...,3]
    bits=((b[...,4]<<8)|b[...,5])|(((b[...,6]<<8)|b[...,7])<<16)
    def c565(q):
        return np.stack((((q>>11)&31)*255//31,((q>>5)&63)*255//63,(q&31)*255//31),-1).astype(np.int32)
    p0,p1=c565(a),c565(c);four=(a>c)|four_only
    p2=np.where(four[...,None],(2*p0+p1)//3,(p0+p1)//2)
    p3=np.where(four[...,None],(p0+2*p1)//3,0)
    pal=np.stack([p0,p1,p2,p3],-2)
    al=np.stack([np.full_like(a,255)]*3+[np.where(four,255,0)],-1)
    h,w=blocks.shape[:2];out=np.zeros((h*4,w*4,4),np.uint8)
    for y in range(4):
        for x in range(4):
            i=((bits>>(2*(y*4+x)))&3).astype(np.int64)
            out[y::4,x::4,:3]=np.take_along_axis(pal,i[...,None,None].repeat(3,-1),-2)[...,0,:]
            out[y::4,x::4,3]=np.take_along_axis(al,i[...,None],-1)[...,0]
    return out

def decode(raw,t):
    fmt=t["fmt"];w,h=t["w"],t["h"];bw,bh,sz=FORMATS[fmt]
    if w<=0 or h<=0 or w>4096 or h>4096:raise ValueError("bad dimensions")
    x0=y0=0
    if t["mips"]>1 and min(w,h)<=16:
        if w>h:y0=16//bh
        else:x0=16//bw
    v=untile(raw,(w+bw-1)//bw,(h+bh-1)//bh,sz,(x0,y0))
    if fmt==6:return v[...,[1,2,3,0]]
    if fmt==2:
        out=np.empty((h,w,4),np.uint8);out[...,:3]=255;out[...,3]=v[...,0];return out
    if fmt==18:return color(v)[:h,:w]
    out=color(v[...,8:16],True)
    a=v[...,:8].astype(np.uint64)[...,[1,0,3,2,5,4,7,6]]
    bit=np.zeros(a.shape[:2],np.uint64)
    if fmt==19:
        for i in range(8):bit|=a[...,i]<<np.uint64(i*8)
        for y in range(4):
            for x in range(4):out[y::4,x::4,3]=(((bit>>np.uint64(4*(y*4+x)))&15)*17).astype(np.uint8)
    else:
        a0=a[...,0].astype(np.int32);a1=a[...,1].astype(np.int32)
        pal=np.zeros((*a.shape[:2],8),np.int32);pal[...,0]=a0;pal[...,1]=a1
        for i in range(2,8):
            p8=((8-i)*a0+(i-1)*a1)//7
            p6=((6-i)*a0+(i-1)*a1)//5 if i<6 else (0 if i==6 else 255)
            pal[...,i]=np.where(a0>a1,p8,p6)
        for i in range(6):bit|=a[...,i+2]<<np.uint64(i*8)
        for y in range(4):
            for x in range(4):
                ix=((bit>>np.uint64(3*(y*4+x)))&7).astype(np.int64)
                out[y::4,x::4,3]=np.take_along_axis(pal,ix[...,None],-1)[...,0]
    return out[:h,:w]

def export(path,dest):
    b=parse(path);dest=Path(dest);dest.mkdir(parents=True,exist_ok=True)
    texnames={t["name"] for t in b["texs"]}
    pool=next((e for e in reversed(b["ents"]) if e["sec"]==".gpu" and e["kind"]==12 and e["name"] not in texnames),None)
    report=[]
    for index,t in enumerate(b["texs"]):
        try:
            if t["fmt"] not in FORMATS:raise ValueError("unsupported format")
            if t["psz"]==0xffffffff:
                e=next(e for e in b["ents"] if e["sec"]==".gpu" and e["name"]==t["name"])
                start,length=e["off"],e["size"]
            else:
                if pool is None:raise ValueError("missing shared texture pool")
                start,length=pool["off"]+t["poff"],t["psz"]
            raw=b["data"][b["base"][".gpu"]+start:b["base"][".gpu"]+start+length]
            Image.fromarray(decode(raw,t)).save(dest/("%03d.png"%index))
            report.append(dict(index=index,status="ok",width=t["w"],height=t["h"],fmt=t["fmt"]))
        except Exception as exc:report.append(dict(index=index,status="error",reason=str(exc)))
    (dest/"textures.json").write_text(json.dumps(report,indent=2))
    print("Decoded",sum(x["status"]=="ok" for x in report),"of",len(report))
if __name__=="__main__":
    if len(sys.argv)!=3:sys.exit("Usage: python tools/decode_textures.py <CAFF .bin> <PNG output folder>")
    export(sys.argv[1],sys.argv[2])
