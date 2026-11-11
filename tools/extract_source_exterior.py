"""Export original-source terrain ground polygons from the user's converted Surface GLB.

The source geometry is kept unchanged except for y translation and excluding
faces that overlap Facility. This is reconstructed adjacency, not the
authentic GoldenEye Facility exterior. No new triangles or invented trees.

Usage:
 python tools/extract_source_exterior.py surface.glb surface_exterior.glb
Dependencies: numpy, trimesh
"""
import argparse
from pathlib import Path
import numpy as np
import trimesh

def export(source,target,exclude_x=115,exclude_z=95,shift_y=62):
    scene=trimesh.load(source,force='scene')
    vertices,faces,colors=[],[],[]
    offset=0
    for mesh in scene.geometry.values():
        if len(mesh.faces)==0:continue
        triangles=mesh.triangles.astype(np.float32)
        midpoint=triangles.mean(axis=1)
        keep=(np.abs(mesh.face_normals[:,1])>.65)
        keep&=(midpoint[:,1]>-98)&(midpoint[:,1]<-25)
        keep&=mesh.area_faces>.04
        keep&=((np.abs(triangles[:,:,0])>exclude_x).all(axis=1)|
               (np.abs(triangles[:,:,2])>exclude_z).all(axis=1))
        if not np.any(keep):continue
        triangles=triangles[keep]
        source_color=np.asarray(mesh.visual.vertex_colors)
        if len(source_color)==len(mesh.vertices):
            rgba=source_color[mesh.faces[keep]].reshape(-1,4)
        else:rgba=np.tile(np.array([160,166,164,255],np.uint8),(len(triangles)*3,1))
        coords=triangles.reshape(-1,3).copy()
        coords[:,1]+=shift_y
        faces.append(np.arange(len(coords)).reshape(-1,3)+offset)
        offset+=len(coords)
        vertices.append(coords);colors.append(rgba)
    if not vertices:raise ValueError('No usable source terrain found')
    ground=trimesh.Trimesh(vertices=np.concatenate(vertices),
                           faces=np.concatenate(faces),process=False)
    ground.visual.vertex_colors=np.concatenate(colors)
    Path(target).write_bytes(trimesh.Scene(ground).export(file_type='glb'))
    print(f'Exported {len(ground.faces)} original Surface triangles')

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('source_glb');p.add_argument('output_glb')
    a=p.parse_args();export(a.source_glb,a.output_glb)
