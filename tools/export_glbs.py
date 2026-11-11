"""Convert extracted XBLA CAFF files into browser-friendly GLBs.
Usage:
  pip install numpy trimesh
  python tools/export_glbs.py local-assets converted
"""
import json,sys
from pathlib import Path
import numpy as np
import trimesh
from convert_ge import convert

def export(root,out):
    root,out=Path(root),Path(out)
    out.mkdir(parents=True,exist_ok=True)
    report={}
    entries=[
        ("facility","background/facility/default.bin"),
        ("boris","char/boris/default.bin"),
        ("oddjob","char/oddjob/default.bin"),
        ("trevelyan","char/trevelyan/default.bin"),
    ]
    for name,rel in entries:
        draws,pools,stats=convert(root/"files/new"/rel)
        all_vertices=np.asarray([v[0] for vv in pools.values()
                                 for v in vv if v is not None],dtype=np.float64)
        if name=="facility":
            center=np.array([8418.75,0,-2000])
            scale=.01
        else:
            lo=np.percentile(all_vertices,2,axis=0)
            hi=np.percentile(all_vertices,98,axis=0)
            center=(lo+hi)/2
            center[1]=lo[1]
            scale=2/max(hi[1]-lo[1],1)
        scene=trimesh.Scene()
        for i,(key,indices) in enumerate(draws):
            vs=pools[key]
            uniq=sorted(set(indices))
            remap={v:j for j,v in enumerate(uniq)}
            positions=(np.asarray([vs[j][0] for j in uniq])-center)*scale
            rgb=np.asarray([vs[j][1] for j in uniq])
            rgba=np.c_[((rgb*.67+.33)*255).astype("uint8"),
                       np.full(len(uniq),255,dtype="uint8")]
            faces=np.asarray([remap[j] for j in indices],dtype=np.int32).reshape(-1,3)
            mesh=trimesh.Trimesh(vertices=positions,faces=faces,
                                vertex_colors=rgba,process=False)
            scene.add_geometry(mesh,geom_name="%s_%03d"%(name,i))
        path=out/(name+".glb")
        path.write_bytes(scene.export(file_type="glb"))
        report[name]=dict(**stats,glb_bytes=path.stat().st_size)
        print(path,stats["triangles"],"triangles")
    (out/"CONVERSION_REPORT.json").write_text(json.dumps(report,indent=2))

if __name__=="__main__":
    if len(sys.argv)!=3:
        sys.exit("Usage: python tools/export_glbs.py <extracted-root> <converted-root>")
    export(sys.argv[1],sys.argv[2])
