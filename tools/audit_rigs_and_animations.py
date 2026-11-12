#!/usr/bin/env python3
"""Audit skeleton, skin and authored animation relationships in GLB/glTF.

Usage:
  python tools/audit_rigs_and_animations.py boris.glb other.glb --out rig_report.json

This reads real glTF node/skin/animation structures only. It does NOT decode
Xbox/XBLA proprietary CAFF animation tracks or invent bone mappings.
No third-party dependencies. Reports unresolved references, parentage, joints,
inverse bind matrix accessor metadata, targets, and track sampler metadata.
"""
import argparse
import json
import struct
from pathlib import Path

COMPONENTS={5120:1,5121:1,5122:2,5123:2,5125:4,5126:4}
ELEMENTS={"SCALAR":1,"VEC2":2,"VEC3":3,"VEC4":4,"MAT2":4,"MAT3":9,"MAT4":16}

def read_gltf(path):
    raw=path.read_bytes()
    if path.suffix.lower()==".glb":
        if len(raw)<20 or raw[:4]!=b"glTF":
            raise ValueError("Invalid GLB header")
        magic,version,length=struct.unpack_from("<4sII",raw)
        if version!=2 or length!=len(raw):
            raise ValueError("Expected complete glTF 2.0 GLB")
        off=12;document=None;bin_chunks=[]
        while off+8<=len(raw):
            size,kind=struct.unpack_from("<I4s",raw,off);off+=8
            if off+size>len(raw):raise ValueError("Truncated GLB chunk")
            chunk=raw[off:off+size];off+=size
            if kind==b"JSON":document=json.loads(chunk.decode("utf-8").rstrip(" \0"))
            elif kind==b"BIN\0":bin_chunks.append(chunk)
        if off!=len(raw) or document is None:raise ValueError("Missing/invalid JSON chunk")
        return document,bin_chunks
    return json.loads(raw.decode("utf-8")),[]

def accessor_info(doc,index):
    accessors=doc.get("accessors",[])
    if not isinstance(index,int) or not 0<=index<len(accessors):
        return {"index":index,"error":"invalid accessor index"}
    a=accessors[index];comp=a.get("componentType");typ=a.get("type")
    return {"index":index,"count":a.get("count",0),"type":typ,
            "componentType":comp,"bytesPerElement":COMPONENTS.get(comp,0)*ELEMENTS.get(typ,0),
            "bufferView":a.get("bufferView"),"sparse":bool(a.get("sparse"))}

def audit(path):
    doc,chunks=read_gltf(path)
    nodes=doc.get("nodes",[]);skins=doc.get("skins",[]);animations=doc.get("animations",[])
    parents=[[] for _ in nodes];issues=[]
    for idx,node in enumerate(nodes):
        for child in node.get("children",[]):
            if not isinstance(child,int) or not 0<=child<len(nodes):
                issues.append(f"node {idx}: invalid child {child}");continue
            parents[child].append(idx)
    node_info=[{"index":i,"name":n.get("name",f"node_{i}"),
                "parents":parents[i],"children":n.get("children",[]),
                "mesh":n.get("mesh"),"skin":n.get("skin"),
                "hasMatrix":"matrix" in n,"hasTRS":any(k in n for k in ("translation","rotation","scale"))}
                for i,n in enumerate(nodes)]
    result_skins=[]
    for i,skin in enumerate(skins):
        joints=skin.get("joints",[])
        for joint in joints:
            if not isinstance(joint,int) or not 0<=joint<len(nodes):
                issues.append(f"skin {i}: invalid joint {joint}")
        ibm=skin.get("inverseBindMatrices")
        meta=accessor_info(doc,ibm) if ibm is not None else None
        if meta and (meta.get("count")!=len(joints) or meta.get("type")!="MAT4"):
            issues.append(f"skin {i}: inverse bind accessor inconsistent with {len(joints)} joints")
        result_skins.append({"index":i,"name":skin.get("name"),"skeletonRoot":skin.get("skeleton"),
                             "jointCount":len(joints),"joints":[{"index":j,"name":nodes[j].get("name",f"node_{j}"),"parents":parents[j]}
                                if isinstance(j,int) and 0<=j<len(nodes) else {"invalid":j} for j in joints],
                             "inverseBindMatrices":meta})
    clips=[]
    for ai,animation in enumerate(animations):
        samplers=animation.get("samplers",[]);tracks=[]
        for ci,ch in enumerate(animation.get("channels",[])):
            target=ch.get("target",{});node=target.get("node");sid=ch.get("sampler")
            if not isinstance(node,int) or not 0<=node<len(nodes):
                issues.append(f"animation {ai} channel {ci}: invalid target node {node}")
            if not isinstance(sid,int) or not 0<=sid<len(samplers):
                issues.append(f"animation {ai} channel {ci}: invalid sampler {sid}");continue
            sampler=samplers[sid]
            tracks.append({"targetNode":node,"targetName":nodes[node].get("name") if isinstance(node,int) and 0<=node<len(nodes) else None,
                           "path":target.get("path"),"interpolation":sampler.get("interpolation","LINEAR"),
                           "input":accessor_info(doc,sampler.get("input")),
                           "output":accessor_info(doc,sampler.get("output"))})
        clips.append({"index":ai,"name":animation.get("name",f"animation_{ai}"),"channels":len(tracks),"tracks":tracks})
    return {"file":str(path),"format":"glTF 2.0","glbBinaryChunks":len(chunks),
            "nodeCount":len(nodes),"meshCount":len(doc.get("meshes",[])),
            "skins":result_skins,"animations":clips,"nodes":node_info,
            "issues":issues,"authoredAnimationClipsFound":len(clips),
            "originalXboxCAFFDecoded":False}

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("files",nargs="+",type=Path)
    p.add_argument("--out",type=Path,default=Path("rig_report.json"))
    args=p.parse_args()
    reports=[]
    for path in args.files:
        try:reports.append(audit(path))
        except (ValueError,KeyError,UnicodeError,OSError,struct.error) as e:
            reports.append({"file":str(path),"error":str(e)})
    args.out.write_text(json.dumps(reports,indent=2),encoding="utf-8")
    for r in reports:
        print(f"{r['file']}: skins={len(r.get('skins',[]))} clips={len(r.get('animations',[]))} "
              f"issues={len(r.get('issues',[]))} {r.get('error','')}")
    print(f"Report: {args.out}")
if __name__=="__main__":
    main()
