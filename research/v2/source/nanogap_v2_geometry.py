#!/usr/bin/env python3
"""AXEZENT NanoGap v2.0 research geometry: ray-phase-corrected gyroid.

Author: Shawn Calvin Snelling (AXEZENT).

Research-grade geometric prototype only. No finite element solver, material
characterization, impact testing or fatigue validation is implemented here.

v2 modifies ONLY the gyroid spatial phase from the original July 2026 v1.0
STL generator; otherwise carries over the mathematical geometric parameters,
tetrahedral support, and outer frame for a controlled geometric comparison.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable

import numpy as np
from scipy.integrate import cumulative_trapezoid
from skimage import measure
import trimesh

@dataclass(frozen=True)
class Parameters:
    author: str = "Shawn Calvin Snelling"
    architecture: str = "AXEZENT_NanoGap_Cube_v2_0_RayPhaseCorrected"
    side_mm: float = 63.5
    voxel_target_mm: float = 0.75
    frame_mm: float = 3.8
    pitch_core_mm: float = 14.0
    pitch_shell_mm: float = 8.0
    pitch_exponent: float = 1.35
    tau_core: float = 0.27
    tau_shell: float = 0.48
    thickness_exponent: float = 1.60
    triangle_vertex_fraction: float = 0.72
    triangle_strut_radius_mm: float = 1.65
    center_node_radius_mm: float = 3.5
    nano_alpha_per_mm: float = 0.22
    nano_tau_boost: float = 0.080
    padding_mm: float = 1.5


def pitch_of_r(r, p: Parameters):
    return p.pitch_core_mm - (p.pitch_core_mm - p.pitch_shell_mm) * np.asarray(r)**p.pitch_exponent


def tau_of_r(r, p: Parameters):
    return p.tau_core + (p.tau_shell-p.tau_core)*np.asarray(r)**p.thickness_exponent


def integrated_inverse_pitch(r, p: Parameters, resolution: int = 4097):
    """I(r)=int_0^r [1/P(s)]ds, evaluated on [0,1] with trapezoidal rule."""
    q=np.linspace(0.0,1.0,resolution, dtype=np.float64)
    A=cumulative_trapezoid(1.0/pitch_of_r(q,p),q,initial=0.0)
    return np.interp(np.asarray(r,dtype=np.float64),q,A)


def gyroid_phase_scale(r,p:Parameters):
    """Phase coefficient [rad/mm] satisfying dominant-face-ray target pitch."""
    r=np.asarray(r,dtype=np.float64)
    I=integrated_inverse_pitch(np.clip(r,0,1),p)
    return 2*math.pi*np.divide(I,r,out=np.full_like(r,1.0/p.pitch_core_mm),where=r>1e-12)


def segment_distance_sq(X,Y,Z,a:Iterable[float],b:Iterable[float]):
    a=np.asarray(tuple(a),np.float32)
    b=np.asarray(tuple(b),np.float32)
    v=b-a
    vv=float(v@v)
    t=np.clip(((X-a[0])*v[0]+(Y-a[1])*v[1]+(Z-a[2])*v[2])/vv,0.0,1.0)
    return (X-a[0]-t*v[0])**2+(Y-a[1]-t*v[1])**2+(Z-a[2]-t*v[2])**2


def box_sdf(X,Y,Z, center:tuple[float,float,float],half_size:tuple[float,float,float]):
    cx,cy,cz=center
    hx,hy,hz=half_size
    qx,qy,qz=np.abs(X-cx)-hx,np.abs(Y-cy)-hy,np.abs(Z-cz)-hz
    ox,oy,oz=np.maximum(qx,0),np.maximum(qy,0),np.maximum(qz,0)
    return np.sqrt(ox**2+oy**2+oz**2)+np.minimum(np.maximum(qx,np.maximum(qy,qz)),0)


def build_field(p: Parameters, method: str = "v2"):
    if method not in ("v1", "v2"):
        raise ValueError("method must be v1 or v2")
    H=p.side_mm/2
    n=int(np.ceil((p.side_mm+2*p.padding_mm)/p.voxel_target_mm))+1
    axis=np.linspace(-H-p.padding_mm,H+p.padding_mm,n,dtype=np.float32)
    ds=float(axis[1]-axis[0])
    X,Y,Z=np.meshgrid(axis,axis,axis,indexing="ij")
    r=np.maximum(np.maximum(np.abs(X),np.abs(Y)),np.abs(Z))/H
    rc=np.clip(r,0,1)
    P=pitch_of_r(rc,p)
    if method=="v1":
        phase_coeff=2*np.pi/P
    else:
        phase_coeff=gyroid_phase_scale(rc,p)
    gx,gy,gz=phase_coeff*X,phase_coeff*Y,phase_coeff*Z
    G=np.sin(gx)*np.cos(gy)+np.sin(gy)*np.cos(gz)+np.sin(gz)*np.cos(gx)

    h=p.triangle_vertex_fraction*H
    endpoints=((h,h,h),(h,-h,-h),(-h,h,-h),(-h,-h,h))
    d2=np.full(X.shape,np.inf,dtype=np.float32)
    for v in endpoints:
        np.minimum(d2,segment_distance_sq(X,Y,Z,(0,0,0),v),out=d2)
    distance=np.sqrt(d2)
    tau=tau_of_r(rc,p)+p.nano_tau_boost*np.exp(-p.nano_alpha_per_mm*distance)
    gyro=np.abs(G)-tau
    struts=distance-p.triangle_strut_radius_mm
    center=np.sqrt(X*X+Y*Y+Z*Z)-p.center_node_radius_mm

    ft=p.frame_mm
    c=H-ft/2
    frame=np.full(X.shape,np.inf,dtype=np.float32)
    for sy in (-1.,1.):
        for sz in (-1.,1.):
            np.minimum(frame,box_sdf(X,Y,Z,(0.,sy*c,sz*c),(H,ft/2,ft/2)),out=frame)
    for sx in (-1.,1.):
        for sz in (-1.,1.):
            np.minimum(frame,box_sdf(X,Y,Z,(sx*c,0.,sz*c),(ft/2,H,ft/2)),out=frame)
    for sx in (-1.,1.):
        for sy in (-1.,1.):
            np.minimum(frame,box_sdf(X,Y,Z,(sx*c,sy*c,0.),(ft/2,ft/2,H)),out=frame)
    union=np.minimum(np.minimum(np.minimum(gyro,struts),center),frame)
    clip=np.maximum(np.maximum(np.abs(X),np.abs(Y)),np.abs(Z))-H
    field=np.maximum(union,clip).astype(np.float32)
    return axis,ds,field


def build_mesh(p: Parameters,method:str):
    axis,ds,F=build_field(p,method)
    v,faces,_,_=measure.marching_cubes(F,level=0,spacing=(ds,ds,ds),allow_degenerate=False)
    v+=float(axis[0])
    m=trimesh.Trimesh(vertices=v,faces=faces,process=True)
    m.remove_unreferenced_vertices()
    m.process(validate=True)
    m.fix_normals()
    return m,ds


def receipt(p:Parameters,mesh:trimesh.Trimesh,ds:float,method:str,path:Path):
    return {
        'author':p.author,
        'method':method,
        'mesh_pitch_target_mm':p.voxel_target_mm,
        'actual_voxel_mm':ds,
        'file':path.name,
        'bytes':path.stat().st_size,
        'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
        'vertices':int(mesh.vertices.shape[0]),
        'facets':int(mesh.faces.shape[0]),
        'watertight':bool(mesh.is_watertight),
        'winding_consistent':bool(mesh.is_winding_consistent),
        'bounds_mm':mesh.bounds.tolist(),
        'volume_signed_mm3':float(mesh.volume),
        'volume_fraction_signed':float(mesh.volume)/p.side_mm**3,
        'surface_area_mm2':float(mesh.area),
        'volume_is_physical_only_if_watertight':True,
        'status':'GEOMETRIC_SIMULATION_ONLY_NOT_MECHANICAL_TEST',
    }


def main():
    a=argparse.ArgumentParser(description='AXEZENT NanoGap v2 reproducible geometric study')
    a.add_argument('--output',type=Path,default=Path('models'))
    a.add_argument('--voxel',type=float,default=.85)
    a.add_argument('--method',choices=['v1','v2'],default='v2')
    args=a.parse_args()
    p=Parameters(voxel_target_mm=args.voxel)
    args.output.mkdir(parents=True,exist_ok=True)
    mesh,ds=build_mesh(p,args.method)
    file=args.output/f'AXEZENT_NanoGap_{args.method.upper()}_63p5mm_voxel_{args.voxel:g}mm.stl'
    mesh.export(file)
    result=receipt(p,mesh,ds,args.method,file)
    (args.output/(file.stem+'.json')).write_text(json.dumps({'parameters':asdict(p),'result':result},indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':
    main()