"""Attach decoded CAFF texture images to extracted Facility/Boris geometry.
Requires numpy, pillow, trimesh.
Usage:
    python tools/export_textured_glbs.py local-assets textures converted
You must run decode_textures.py on both CAFF files first.
Game assets are not included in this repository.
"""
import sys,struct
from pathlib import Path
import numpy as np
from PIL import Image
import trimesh
from trimesh.visual.texture import TextureVisuals
from trimesh.visual.material import PBRMaterial
from convert_ge import convert,modelparts,records

def material_indices(stream):
    slots={};found=[]
    for at,op,a in records(stream):
        if op==45 and len(a)>=3:
            n=a[1]>>16
            i=2+(2 if a[1]&65535 else 0);slots={}
            for j in range(min(n,16)):
                if i+1<len(a):
                    slots[a[i+1]>>16]=a[i]
                    i+=2
        if op in (1,48) and len(a)>=3 and a[0] in (4,5,13) and a[1]>2:
            found.append(slots.get(0))
    return found

def export(name,source,texture_dir,dest):
    meshes,pools,report=convert(source)
    b,blob,graph,stream=modelparts(source)
    mats=material_indices(stream)
    if len(meshes)!=len(mats):
        raise ValueError("Incomplete geometry resolution; material alignment cannot be trusted")
    arr=np.asarray([v[0] for vv in pools.values() for v in vv if v is not None])
    if name=="facility":
        center=np.asarray([8418.75,0,-2000]);scale=.01
    else:
        lo=np.percentile(arr,2,axis=0);hi=np.percentile(arr,98,axis=0)
        center=(lo+hi)/2;center[1]=lo[1]
        scale=2/max(hi[1]-lo[1],1)
    scene=trimesh.Scene()
    for i,(key,indices) in enumerate(meshes):
        off,stride,n=key
        used=sorted(set(indices));remap={j:k for k,j in enumerate(used)}
        vertices=(np.asarray([pools[key][j][0] for j in used])-center)*scale
        faces=np.asarray([remap[j] for j in indices]).reshape(-1,3)
        uv=[]
        for j in used:
            if name=="facility" and stride in (24,32):
                u,v=struct.unpack_from(">hh",blob,off+j*stride+16)
                uv.append((u/256,1-v/256))
            elif name=="boris" and stride in (32,36):
                u,v=struct.unpack_from(">hh",blob,off+j*stride+(24 if stride==36 else 20))
                uv.append((u/16384,1-v/16384))
            else:
                xyz=pools[key][j][0];uv.append((xyz[0]/300,xyz[2]/300))
        mesh=trimesh.Trimesh(vertices=vertices,faces=faces,process=False)
        tex_id=mats[i]
        source_png=Path(texture_dir)/("%03d.png"%tex_id) if tex_id is not None else None
        if source_png is not None and source_png.is_file():
            material=PBRMaterial(baseColorTexture=Image.open(source_png).convert("RGBA"),
                                 metallicFactor=0,roughnessFactor=1,doubleSided=True)
            mesh.visual=TextureVisuals(uv=np.asarray(uv),material=material)
        scene.add_geometry(mesh,geom_name=f"{name}_{i:03d}")
    Path(dest).parent.mkdir(parents=True,exist_ok=True)
    Path(dest).write_bytes(scene.export(file_type="glb"))
    print(dest,report["triangles"],"triangles",len(meshes),"draw batches")

if __name__=="__main__":
    if len(sys.argv)!=4:sys.exit("Usage: python tools/export_textured_glbs.py <extracted-root> <textures-root> <output-root>")
    root,tx,out=map(Path,sys.argv[1:])
    for name,rel in (("facility","background/facility/default.bin"),("boris","char/boris/default.bin")):
        export(name,root/"files/new"/rel,tx/name,out/(name+"_textured.glb"))
