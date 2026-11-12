"""Inspect the original Xbox GoldenEye CAFF 'hits' resource header.

This does not claim to parse authored physics surfaces or animations.
Supply a locally extracted source *_hits/default.mb.hit.bin file.
Usage: python tools/inspect_hit_caff.py my_facility_hits.bin
Requires repository caff_min.py.
"""
import sys, json, struct
from pathlib import Path
from caff_min import parse

def inspect(path):
    parsed=parse(path)
    data=parsed["data"]
    out={"input":str(path),"source_kind":"Xbox GoldenEye hit/collision resource",
         "sections":list(parsed["base"]),"caff_entries":len(parsed["ents"]),
         "has_authored_collision_decoder":False,"has_animation_decoder":False}
    entries=[]
    for entry in parsed["ents"]:
        sec=entry["sec"]
        pos=parsed["base"][sec]+entry["off"]
        piece=data[pos:pos+min(entry["size"],64)]
        marker=piece[:4].decode("ascii","replace")
        entries.append({"section":sec,"kind":entry["kind"],"size":entry["size"],
                        "first_four_bytes":marker,
                        "version_ascii":piece[5:17].decode("ascii","replace") if marker=="hits" else None})
    out["entries"]=entries
    print(json.dumps(out,indent=2))
    return out

if __name__=="__main__":
    if len(sys.argv)<2:sys.exit(__doc__)
    for f in sys.argv[1:]:inspect(Path(f))
