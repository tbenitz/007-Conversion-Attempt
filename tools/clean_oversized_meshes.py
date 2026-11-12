"""Audit or remove obvious oversized triangles from a user-supplied converted map GLB.

Example:
  python tools/clean_oversized_meshes.py bunker.glb bunker_review.glb --max-edge 38

IMPORTANT: Large triangles can be genuine landscape. This is an experimental
per-map visibility repair, not original game collision/geometry restoration.
Do not apply thresholds globally without visual review.
"""
from argparse import ArgumentParser
from pathlib import Path
import json
import numpy as np
import trimesh
from PIL import ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True

def clean(source, dest, max_edge):
    scene = trimesh.load(source, file_type="glb", force="scene", process=False)
    before = removed = 0
    for mesh in scene.geometry.values():
        if not len(mesh.faces):
            continue
        tri = np.asarray(mesh.triangles, dtype=np.float32)
        edges = np.linalg.norm(tri - np.roll(tri, 1, axis=1), axis=2).max(axis=1)
        keep = edges <= max_edge
        before += len(keep)
        removed += int((~keep).sum())
        if not keep.all():
            mesh.update_faces(keep)
            mesh.remove_unreferenced_vertices()
    data = scene.export(file_type="glb")
    Path(dest).write_bytes(data)
    check = trimesh.load(dest, file_type="glb", force="scene")
    after = sum(len(mesh.faces) for mesh in check.geometry.values())
    if after != before - removed:
        raise RuntimeError(f"Expected {before - removed} faces, got {after}")
    print(json.dumps({"source": str(source), "max_edge": max_edge,
                      "original": before, "removed": removed, "remaining": after}, indent=2))

if __name__ == "__main__":
    p = ArgumentParser(description=__doc__)
    p.add_argument("source")
    p.add_argument("output")
    p.add_argument("--max-edge", type=float, required=True)
    a = p.parse_args()
    clean(a.source, a.output, a.max_edge)
