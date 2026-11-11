"""Recover geometrically unmatched original-generation Facility triangles.
This script does not ship copyrighted assets. Requires locally extracted
original + remastered game files and scipy, numpy, trimesh.

Usage:
  python tools/patch_missing_facility.py converted/facility_textured.glb \
    local-assets/files/original/background/facility/default.bin \
    converted/facility_textured_repaired.glb
"""
import json,sys
from pathlib import Path
import numpy as np
import trimesh
from scipy.spatial import cKDTree
from convert_ge import convert

def patch(remastered,original,out,threshold=.5):
    scene=trimesh.load(remastered,force='scene')
    reference=np.concatenate([mesh.triangles_center for mesh in scene.geometry.values() if len(mesh.faces)])
    meshes,pools,report=convert(original)
    triangles=[];colors=[]
    for key,ids in meshes:
        verts=pools[key]
        for j in range(0,len(ids),3):
            corners=[verts[z] for z in ids[j:j+3]]
            if not all(x is not None for x in corners):continue
            triangles.append([(np.asarray(v[0])-[8418.75,0,-2000])*.01 for v in corners])
            colors.append([v[1] for v in corners])
    source=np.asarray(triangles);colors=np.asarray(colors)
    distance,_=cKDTree(reference).query(source.mean(axis=1))
    keep=distance>threshold
    patches=source[keep]
    shades=colors[keep]
    if len(patches):
        rgba=np.column_stack((np.clip((shades.reshape(-1,3)*.7+.30)*255,0,255).astype(np.uint8),
                              np.full(len(shades)*3,255,dtype=np.uint8)))
        mesh=trimesh.Trimesh(vertices=patches.reshape(-1,3),
             faces=np.arange(len(patches)*3).reshape(-1,3),process=False)
        mesh.visual.vertex_colors=rgba
        scene.add_geometry(mesh,geom_name='original_generation_gap_repair')
    out=Path(out);out.parent.mkdir(parents=True,exist_ok=True)
    out.write_bytes(scene.export(file_type='glb'))
    summary=dict(original_triangles=len(source),remastered_triangles=len(reference),
                 original_only_added=int(keep.sum()),threshold_meters=threshold)
    print(json.dumps(summary,indent=2))
    return summary

if __name__=='__main__':
    if len(sys.argv)!=4:sys.exit('Usage: patch_missing_facility.py <remastered.glb> <original.bin> <output.glb>')
    patch(*sys.argv[1:])
