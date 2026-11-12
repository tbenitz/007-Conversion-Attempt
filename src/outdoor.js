// Reconstructed outdoor test environment. No original GoldenEye trees/outpost geometry is claimed.
import * as THREE from 'three';
export const OUTDOOR_Y = -9;
export function buildOutdoor(scene,{density=10,seed=7}={}){
  let state=seed>>>0;
  const rand=()=>{state=(1664525*state+1013904223)>>>0;return state/4294967296};
  const root=new THREE.Group();root.name='Reconstructed exterior — generated, not original';
  scene.add(root);
  const trunkMat=new THREE.MeshStandardMaterial({color:0x65503a,roughness:1});
  const leafMats=[0x36533d,0x465b39,0x3d5f4a].map(color=>new THREE.MeshStandardMaterial({color,roughness:1,flatShading:true}));
  const stone=new THREE.MeshStandardMaterial({color:0x737b7c,roughness:1});
  const wall=new THREE.MeshStandardMaterial({color:0x606d70,roughness:1});
  const ground=new THREE.Mesh(new THREE.PlaneGeometry(210,180),new THREE.MeshStandardMaterial({color:0x445347,roughness:1}));
  ground.rotation.x=-Math.PI/2;ground.position.y=OUTDOOR_Y-.055;ground.name='Generated exterior ground';root.add(ground);
  const obstacles=[];
  const boxes=[];
  function addBox(x,z,w,d,h,material=stone,solid=true){
    const mesh=new THREE.Mesh(new THREE.BoxGeometry(w,h,d),material);
    mesh.position.set(x,OUTDOOR_Y+h/2,z);mesh.castShadow=false;root.add(mesh);
    if(solid)obstacles.push({x,z,rx:w/2,rz:d/2});
    boxes.push(mesh);
  }
  // Four perimeter compounds. Each contains walls, shelters, corridors and cover.
  const sites=[[-76,-65],[76,-65],[-76,65],[76,65]];
  for(const [x,z] of sites){
    // Broken perimeter and door openings (no collision across the openings).
    for(const dx of [-12,12])for(const dz of [-8,0,8])addBox(x+dx,z+dz,1.5,7.7,3.3,wall);
    for(const dz of [-12,12])for(const dx of [-8,0,8])if(!(dz===-12&&dx===0))addBox(x+dx,z+dz,7.7,1.5,3.3,wall);
    for(const dx of [-6,6])for(const dz of [-4,4])addBox(x+dx,z+dz,3.1,3.1,1.35);
    addBox(x+2,z+6,5,3,2.7,wall);
  }
  // Density=10 makes about 10x the older 54 source-prop placements as generated scenery.
  // Fixed seed ensures repeatability; reject the central imported Facility footprint and paths.
  const requested=Math.max(0,Math.round(54*density));
  const count=Math.min(2000,requested);
  const trunkGeo=new THREE.CylinderGeometry(.17,.27,1,5), crownGeo=new THREE.ConeGeometry(1,1,6);
  const trunks=new THREE.InstancedMesh(trunkGeo,trunkMat,count);
  const crowns=leafMats.map(mat=>new THREE.InstancedMesh(crownGeo,mat,count));
  const dummy=new THREE.Object3D(),counts=[0,0,0];
  let trees=0,cover=0,attempts=0;
  const points=[];
  function spaced(x,z,minDist){
    for(const p of points)if((p.x-x)**2+(p.z-z)**2<minDist**2)return false;
    for(const p of sites)if(Math.abs(x-p[0])<15&&Math.abs(z-p[1])<15)return false;
    return true;
  }
  while(trees+cover<count&&attempts++<count*45){
    const x=-99+rand()*198,z=-84+rand()*168;
    if(Math.abs(x)<51&&Math.abs(z)<43)continue;
    if(!spaced(x,z,2.1))continue;
    if(Math.abs(x)>97||Math.abs(z)>82)continue;
    points.push({x,z});
    const tree=rand()<.43;
    if(tree){
      const height=3+rand()*5.5;
      dummy.position.set(x,OUTDOOR_Y+height*.24,z);
      dummy.scale.set(1,height*.48,1);dummy.rotation.set(0,rand()*6.28,0);dummy.updateMatrix();
      trunks.setMatrixAt(trees,dummy.matrix);
      const crownIndex=Math.floor(rand()*3),ci=counts[crownIndex]++;
      dummy.position.set(x,OUTDOOR_Y+height*.71,z);
      dummy.scale.set(1.35+rand()*.8,height*.65,1.35+rand()*.8);dummy.updateMatrix();
      crowns[crownIndex].setMatrixAt(ci,dummy.matrix);
      obstacles.push({x,z,rx:.27,rz:.27});
      trees++;
    }else{
      const w=.9+rand()*2.8,d=.9+rand()*2.8,h=.65+rand()*1.7;
      addBox(x,z,w,d,h,rand()<.5?stone:wall);
      cover++;
    }
  }
  trunks.count=trees;trunks.instanceMatrix.needsUpdate=true;root.add(trunks);
  crowns.forEach((mesh,i)=>{mesh.count=counts[i];mesh.instanceMatrix.needsUpdate=true;root.add(mesh)});
  const edgeMat=new THREE.MeshStandardMaterial({color:0x89918b});
  for(const z of [-89,89])addBox(0,z,210,1.8,3,edgeMat);
  for(const x of [-104,104])addBox(x,0,1.8,180,3,edgeMat);
  return {root,obstacles,counts:{trees,cover,compoundSites:sites.length,total:trees+cover},isOutside(x,z){
    return Math.abs(x)>=51||Math.abs(z)>=43;
  },blocks(x,z,r=.35){
    return obstacles.some(o=>Math.abs(x-o.x)<o.rx+r&&Math.abs(z-o.z)<o.rz+r);
  }};
}
