"""Bulk PNG extraction from locally supplied XBLA CAFF assets.
Usage:
  pip install numpy pillow
  python tools/bulk_extract_and_decode.py game.live output/
Expects tools/caff_min.py and tools/decode_textures.py from this repo.
No copyrighted input files are included.
"""
import argparse,json,math,sys
from pathlib import Path
from collections import Counter
from decode_textures import export as decode

def offset(n):
    return 0xc000+(n+n//170+n//28900)*4096

def read_at(f,n):
    f.seek(offset(n))
    return f.read(4096)

def manifest(f):
    # The package file-table location is validated by the initial STFS
    # extraction workflow and is specific to the supplied retail build.
    entries=[]
    for block in range(57):
        b=read_at(f,block)
        for j in range(64):
            r=b[j*64:(j+1)*64]
            name=r[:40].split(b"\0")[0].decode("utf8","replace")
            if not name:continue
            entries.append(dict(id=block*64+j,name=name,
                start=int.from_bytes(r[47:50],"little"),
                size=int.from_bytes(r[52:56],"big"),
                parent=int.from_bytes(r[50:52],"big"),
                contiguous=bool(r[40]&64)))
    byid={e["id"]:e for e in entries}
    for e in entries:
        chain=[e["name"]];p=e["parent"];seen=set()
        while p in byid and p not in seen:
            seen.add(p);par=byid[p];chain.insert(0,par["name"]);p=par["parent"]
        e["path"]="/".join(chain)
    return entries

def extract(f,e,target):
    if not e["contiguous"]:raise ValueError("fragmented STFS file")
    offsets=[k for k in range(5) if read_at(f,e["start"]+k)[:4]==b"CAFF"]
    if not offsets:raise ValueError("CAFF header not found")
    shift=next(v for v in (2,1,0,3,4) if v in offsets)
    remain=e["size"];target.parent.mkdir(parents=True,exist_ok=True)
    with target.open("wb") as out:
        for i in range(math.ceil(remain/4096)):
            b=read_at(f,e["start"]+shift+i)[:remain]
            out.write(b);remain-=len(b)
    return shift

def main():
    p=argparse.ArgumentParser()
    p.add_argument("input",help="Unzipped user-provided Xbox LIVE/STFS package")
    p.add_argument("output",help="Conversion output directory")
    a=p.parse_args()
    root=Path(a.output);root.mkdir(parents=True,exist_ok=True)
    report=[];stats=Counter()
    with open(a.input,"rb") as f:
        entries=[e for e in manifest(f) if e["path"].startswith("files/new/")
                 and e["path"].endswith("/default.bin")
                 and e["path"].split("/")[2] in
                 ("background","skydome","char","head","gun","prop")]
        for j,e in enumerate(entries):
            _files,gen,kind,name,_default=e["path"].split("/")
            source=root/"source_caff"/kind/name/"default.bin"
            textures=root/"textures"/kind/name
            try:
                shift=extract(f,e,source)
                decode(source,textures)
                manifest_path=textures/"textures.json"
                image_report=json.loads(manifest_path.read_text())
                ok=sum(x["status"]=="ok" for x in image_report)
                failed=len(image_report)-ok
                stats["assets_ok"]+=1;stats["png"]+=ok;stats["textures_failed"]+=failed
                report.append(dict(path=e["path"],kind=kind,name=name,
                                   png=ok,failed=failed,shift=shift,status="ok"))
            except Exception as exc:
                report.append(dict(path=e["path"],kind=kind,name=name,
                                   status="error",reason=str(exc)))
                stats["assets_failed"]+=1
            if (j+1)%20==0:print(j+1,"/",len(entries),dict(stats),flush=True)
    (root/"conversion_report.json").write_text(json.dumps(
      dict(summary=dict(stats),assets=report),indent=2))
    print("FINISHED",dict(stats))

if __name__=="__main__":main()
