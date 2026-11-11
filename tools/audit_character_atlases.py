"""Audit source-derived character atlas pairs in a user's own XBLA asset archive.
Works on the compact ZIP produced by this project's conversion workflow.
Requires pillow/numpy. Does not redistribute game assets.

Usage: python tools/audit_character_atlases.py GoldenEye_All_Assets_Compact_ONE_ZIP.zip report.json
"""
import io,json,sys,zipfile
from collections import defaultdict
from PIL import Image
import numpy as np

def score(data):
    a=np.asarray(Image.open(io.BytesIO(data)).convert("RGB"),dtype=np.float32)
    r,g,b=a[:,:,0],a[:,:,1],a[:,:,2]
    skin=np.mean((r>55)&(r>g*1.12)&(g>b*1.08)&(g>35)&(r<245))
    var=a.reshape(-1,3).std(axis=0).mean()
    return float(skin),float(var)

def audit(archive):
    groups=defaultdict(list)
    with zipfile.ZipFile(archive) as z:
        for path in z.namelist():
            parts=path.split("/")
            if len(parts)!=4 or parts[:2]!=["textures","char"] or not path.endswith(".webp"):
                continue
            try:
                skin,var=score(z.read(path))
                if var>11:groups[parts[2]].append((parts[3],skin))
            except (ValueError, OSError):continue
    report={}
    for character,entries in sorted(groups.items()):
        face=max(entries,key=lambda p:p[1])
        clothes=min([x for x in entries if x!=face] or [face],key=lambda p:p[1])
        report[character]={"face_sheet":face[0],"clothing_sheet":clothes[0],
                           "confidence":"unverified heuristic",
                           "original_uvs_reconstructed":False}
    return report

if __name__=="__main__":
    if len(sys.argv)!=3:sys.exit("Usage: audit_character_atlases.py <source zip> <report.json>")
    data=audit(sys.argv[1])
    with open(sys.argv[2],"w") as f:json.dump(data,f,indent=2)
    print(f"Audited {len(data)} character texture atlases; exact UVs still pending")
