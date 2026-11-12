"""Convert actual GoldenEye XBLA head source bundles into 3D GLBs.

No game assets are downloaded or distributed by this tool. Supply your own
locally extracted CAFF files: <head-root>/<head-name>/default.bin.

Usage:
  python tools/export_original_heads.py local-assets/files/new/head export/heads

Requirements: numpy, trimesh and this repository's convert_ge.py/caff_min.py.
35 of 37 head bundles in the supplied test package successfully converted;
the remaining two require improved CAFF/vertex-pool decoding. Texture UVs and
head-to-character attachments are NOT authored stage data.
"""
from pathlib import Path
import argparse, contextlib, io, json
import numpy as np
import trimesh
from convert_ge import convert

def export_one(path, output):
    with contextlib.redirect_stdout(io.StringIO()):
        draws, pools, stats = convert(path)
    if stats['triangles'] < 80:
        raise ValueError('source head geometry unsupported')
    vertices = np.asarray([v[0] for group in pools.values() for v in group if v], dtype=float)
    lo = np.percentile(vertices, 2, axis=0)
    hi = np.percentile(vertices, 98, axis=0)
    center = (lo+hi)*.5
    center[1] = lo[1]
    scale = .28 / max(hi[1]-lo[1], .00001)
    scene = trimesh.Scene()
    for i, (pool, indices) in enumerate(draws):
        vv = pools[pool]
        unique = sorted(set(indices))
        renumber = {old: new for new, old in enumerate(unique)}
        pos = (np.asarray([vv[j][0] for j in unique])-center)*scale
        if not np.isfinite(pos).all() or np.abs(pos).max()>20:
            continue
        rgb = np.asarray([vv[j][1] for j in unique])
        rgba = np.column_stack((np.uint8(np.clip(rgb*.66+.34,0,1)*255),
                                np.full(len(unique),255,np.uint8)))
        faces = np.asarray([renumber[j] for j in indices]).reshape(-1,3)
        keep = np.max(np.abs(pos[faces]),axis=(1,2))<.65
        faces = faces[keep]
        if not len(faces):continue
        mesh = trimesh.Trimesh(vertices=pos,faces=faces,process=False,vertex_colors=rgba)
        scene.add_geometry(mesh,geom_name=path.parent.name+'_'+str(i))
    blob = scene.export(file_type='glb')
    output.parent.mkdir(parents=True,exist_ok=True)
    output.write_bytes(blob)
    scene_check=trimesh.load(output,force='scene')
    faces=sum(len(m.faces) for m in scene_check.geometry.values())
    if faces<80:raise ValueError('head GLB has no usable original source triangles')
    return {'triangles':faces,'draw_batches':len(draws),'bytes':len(blob)}

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('source_head_root',type=Path)
    p.add_argument('output_dir',type=Path)
    a=p.parse_args()
    report={}
    for source in sorted(a.source_head_root.glob('*/default.bin')):
        try:
            report[source.parent.name]={'status':'converted',**export_one(source,a.output_dir/(source.parent.name+'.glb'))}
        except Exception as exc:
            report[source.parent.name]={'status':'unsupported','reason':str(exc)}
    a.output_dir.mkdir(parents=True,exist_ok=True)
    (a.output_dir/'head_conversion_report.json').write_text(json.dumps(report,indent=2))
    print('Converted',sum(r['status']=='converted' for r in report.values()),
          'of',len(report),'original head sources')

if __name__=='__main__':
    main()
