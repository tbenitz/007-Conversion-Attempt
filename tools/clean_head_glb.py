#!/usr/bin/env python3
"""Select coherent original XBLA head geometry, removing disconnected
misdecoded draw fragments. No game assets, fake meshes, UVs or rigs included.
Usage: python tools/clean_head_glb.py input.glb output.glb
Requires numpy and trimesh; all source assets supplied locally by their owner.
"""
import sys, json
import numpy as np
import trimesh
from pathlib import Path

def repair(original, output):
    scene=trimesh.load(original,file_type='glb',force='scene',process=False)
    choices=[]
    for name,mesh in scene.geometry.items():
        if len(mesh.faces)<15:continue
        faces=mesh.faces.copy()
        vertices=mesh.vertices.copy()
        tri=vertices[faces]
        extent=np.ptp(tri.reshape(-1,3),axis=0)
        if extent[1]>.205 or extent[2]>.36:
            med=np.median(vertices,axis=0)
            keep=(np.abs(tri[:,:,2]-med[2])<.24).all(axis=1)
            if extent[1]>.205:
                keep&=(tri[:,:,1]>=float(np.percentile(vertices[:,1],98))-.12).all(axis=1)
            if keep.sum()>=25:
                faces=faces[keep]
                extent=np.ptp(vertices[faces].reshape(-1,3),axis=0)
        if min(extent)<.017 or extent[0]<.034 or extent[1]<.034:continue
        if extent[0]>.32 or extent[1]>.23 or extent[2]>.34:continue
        aspect=max(extent)/max(.001,min(extent))
        choices.append((len(faces)/max(1.,(aspect/4)**2),name,mesh,faces))
    if not choices:raise ValueError("Source head still unsupported")
    _,name,mesh,faces=max(choices,key=lambda x:x[0])
    result=trimesh.Trimesh(vertices=mesh.vertices.copy(),faces=faces,process=False)
    if len(mesh.visual.vertex_colors)==len(mesh.vertices):
        result.visual.vertex_colors=mesh.visual.vertex_colors.copy()
    result.remove_unreferenced_vertices()
    v=result.vertices
    lo,hi=v.min(axis=0),v.max(axis=0)
    scale=np.clip(np.array([.21,.245,.18])/np.maximum(hi-lo,.005),.45,7)
    v[:]=(v-(lo+hi)*.5)*scale
    v[:,1]-=v[:,1].min()
    dest=Path(output)
    dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_bytes(trimesh.Scene(result).export(file_type='glb'))
    print(json.dumps(dict(source_group=name,kept_original_faces=len(result.faces),
                          warning="Source-triangle subset, not authentic UVs/rig"),indent=2))

if __name__=='__main__':
    if len(sys.argv)!=3:sys.exit(__doc__)
    repair(sys.argv[1],sys.argv[2])
