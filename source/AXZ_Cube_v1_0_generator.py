#!/usr/bin/env python3
"""
AXZ / Dr. Shawn Quantum Cube v1.0 — canonical reproducible STL generator

Geometry:
  - graded gyroid sheet lattice
  - Chebyshev (cube-shell) radial grading
  - Triangle-Axe tetrahedral radial spine
  - exponential nano-gap reinforcement law
  - 12-edge structural frame

This is the first fully specified CAD implementation of the earlier conceptual
AXZ cube poster. It is a prototype geometry, not a certified structural part.
"""
from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable

import numpy as np
from skimage import measure
import trimesh


@dataclass(frozen=True)
class CubeParameters:
    name: str = "AXZ_Dr_Shawn_Quantum_Cube_v1_0"
    side_mm: float = 63.5
    voxel_mm: float = 0.95
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
    component_min_area_mm2: float = 20.0
    padding_mm: float = 1.5


def segment_distance_sq(
    X: np.ndarray,
    Y: np.ndarray,
    Z: np.ndarray,
    a: Iterable[float],
    b: Iterable[float],
) -> np.ndarray:
    a = np.asarray(tuple(a), dtype=np.float32)
    b = np.asarray(tuple(b), dtype=np.float32)
    vx, vy, vz = (b - a).astype(np.float32)
    wx, wy, wz = X - a[0], Y - a[1], Z - a[2]
    vv = float(vx * vx + vy * vy + vz * vz)
    t = np.clip((wx * vx + wy * vy + wz * vz) / vv, 0.0, 1.0)
    dx, dy, dz = wx - t * vx, wy - t * vy, wz - t * vz
    return dx * dx + dy * dy + dz * dz


def box_sdf(
    X: np.ndarray,
    Y: np.ndarray,
    Z: np.ndarray,
    center: tuple[float, float, float],
    half_size: tuple[float, float, float],
) -> np.ndarray:
    cx, cy, cz = center
    hx, hy, hz = half_size
    qx, qy, qz = np.abs(X - cx) - hx, np.abs(Y - cy) - hy, np.abs(Z - cz) - hz
    ox, oy, oz = np.maximum(qx, 0), np.maximum(qy, 0), np.maximum(qz, 0)
    outside = np.sqrt(ox * ox + oy * oy + oz * oz)
    inside = np.minimum(np.maximum(qx, np.maximum(qy, qz)), 0)
    return outside + inside


def clean_mesh(mesh: trimesh.Trimesh, minimum_area: float) -> trimesh.Trimesh:
    mesh.remove_unreferenced_vertices()
    mesh.process(validate=True)
    components = mesh.split(only_watertight=False)
    if len(components) > 1:
        kept = [part for part in components if part.area >= minimum_area]
        if not kept:
            kept = [max(components, key=lambda part: part.area)]
        mesh = trimesh.util.concatenate(kept)
        mesh.process(validate=True)
    mesh.fix_normals()
    return mesh


def mesh_from_field(
    field: np.ndarray,
    axis_start: float,
    spacing: float,
    minimum_area: float,
) -> trimesh.Trimesh:
    vertices, faces, _, _ = measure.marching_cubes(
        field,
        level=0.0,
        spacing=(spacing, spacing, spacing),
        allow_degenerate=False,
    )
    vertices += axis_start
    return clean_mesh(
        trimesh.Trimesh(vertices=vertices, faces=faces, process=True),
        minimum_area,
    )


def build_fields(p: CubeParameters):
    L = p.side_mm
    half = L / 2.0
    n = int(np.ceil((L + 2 * p.padding_mm) / p.voxel_mm)) + 1
    axis = np.linspace(
        -half - p.padding_mm,
        half + p.padding_mm,
        n,
        dtype=np.float32,
    )
    spacing = float(axis[1] - axis[0])
    X, Y, Z = np.meshgrid(axis, axis, axis, indexing="ij", sparse=False)

    # Cube-shell radius: r=0 at center, r=1 on the nearest cube face.
    r = np.maximum.reduce((np.abs(X), np.abs(Y), np.abs(Z))) / half
    rc = np.clip(r, 0.0, 1.0)

    # Canonical variable-gap law.  Larger pitch at the core, smaller pitch
    # toward the shell.  This implements the poster's 1.00 -> 0.25 gap trend
    # as a smooth, printable physical pitch field.
    pitch = p.pitch_shell_mm + (
        p.pitch_core_mm - p.pitch_shell_mm
    ) * (1.0 - rc ** p.pitch_exponent)

    # Canonical printable thickness law: thin core, reinforced shell.
    tau = p.tau_core + (p.tau_shell - p.tau_core) * (
        rc ** p.thickness_exponent
    )

    k = (2.0 * np.pi) / pitch
    gx, gy, gz = k * X, k * Y, k * Z
    G = (
        np.sin(gx) * np.cos(gy)
        + np.sin(gy) * np.cos(gz)
        + np.sin(gz) * np.cos(gx)
    )

    # Triangle-Axe geometry: four radial struts to alternating cube corners.
    h = p.triangle_vertex_fraction * half
    tetra_vertices = (
        (h, h, h),
        (h, -h, -h),
        (-h, h, -h),
        (-h, -h, h),
    )
    d2_min = np.full(X.shape, np.inf, dtype=np.float32)
    for vertex in tetra_vertices:
        d2 = segment_distance_sq(X, Y, Z, (0.0, 0.0, 0.0), vertex)
        np.minimum(d2_min, d2, out=d2_min)
    d_triangle = np.sqrt(d2_min)

    # Nano-gap coupling law K(d)=exp(-alpha*d), used as a local gyroid
    # reinforcement field around the Triangle-Axe spine.
    tau_effective = tau + p.nano_tau_boost * np.exp(
        -p.nano_alpha_per_mm * d_triangle
    )
    gyroid_field = np.abs(G) - tau_effective

    # Twelve structural edge rails.
    frame_field = np.full(X.shape, np.inf, dtype=np.float32)
    ft = p.frame_mm
    c = half - ft / 2.0
    for sy in (-1.0, 1.0):
        for sz in (-1.0, 1.0):
            d = box_sdf(X, Y, Z, (0.0, sy * c, sz * c), (half, ft / 2, ft / 2))
            np.minimum(frame_field, d, out=frame_field)
    for sx in (-1.0, 1.0):
        for sz in (-1.0, 1.0):
            d = box_sdf(X, Y, Z, (sx * c, 0.0, sz * c), (ft / 2, half, ft / 2))
            np.minimum(frame_field, d, out=frame_field)
    for sx in (-1.0, 1.0):
        for sy in (-1.0, 1.0):
            d = box_sdf(X, Y, Z, (sx * c, sy * c, 0.0), (ft / 2, ft / 2, half))
            np.minimum(frame_field, d, out=frame_field)

    triangle_strut_field = d_triangle - p.triangle_strut_radius_mm
    center_node_field = np.sqrt(X * X + Y * Y + Z * Z) - p.center_node_radius_mm
    core_union = np.minimum.reduce(
        (gyroid_field, triangle_strut_field, center_node_field)
    )
    full_union = np.minimum(core_union, frame_field)

    cube_clip = np.maximum.reduce((np.abs(X), np.abs(Y), np.abs(Z))) - half
    full_field = np.maximum(full_union, cube_clip)
    core_field = np.maximum(core_union, cube_clip)
    frame_only_field = np.maximum(frame_field, cube_clip)

    return axis, spacing, full_field, core_field, frame_only_field


def export_cube(p: CubeParameters, output_dir: Path) -> dict:
    output_dir.mkdir(parents=True, exist_ok=True)
    axis, spacing, full_field, core_field, frame_field = build_fields(p)

    outputs = {}
    for label, field in (
        ("FULL_ONE_PIECE", full_field),
        ("LATTICE_CORE", core_field),
        ("OUTER_FRAME", frame_field),
    ):
        mesh = mesh_from_field(
            field,
            float(axis[0]),
            spacing,
            p.component_min_area_mm2,
        )
        filename = f"{p.name}_{label}_{p.side_mm:g}mm.stl"
        path = output_dir / filename
        mesh.export(path)
        outputs[label] = {
            "filename": filename,
            "watertight": bool(mesh.is_watertight),
            "vertices": int(len(mesh.vertices)),
            "triangles": int(len(mesh.faces)),
            "extents_mm": [float(v) for v in mesh.extents],
            "volume_mm3": float(mesh.volume),
            "surface_area_mm2": float(mesh.area),
        }

    manifest = {
        "design": asdict(p),
        "equations": {
            "cube_radius": "r=max(|x|,|y|,|z|)/(L/2)",
            "pitch": "P(r)=P_shell+(P_core-P_shell)*(1-r^p)",
            "thickness": "tau(r)=tau_core+(tau_shell-tau_core)*r^q",
            "gyroid": "G=sin(kx)cos(ky)+sin(ky)cos(kz)+sin(kz)cos(kx), k=2*pi/P(r)",
            "nano_coupling": "K(d)=exp(-alpha*d); tau_eff=tau+nano_boost*K(d)",
            "solid_rule": "|G|<=tau_eff, union Triangle-Axe spine and 12-edge frame",
        },
        "zones_normalized": [
            {"zone": 1, "r_min": 0.00, "r_max": 0.20, "gap_weight": 1.00},
            {"zone": 2, "r_min": 0.20, "r_max": 0.40, "gap_weight": 0.75},
            {"zone": 3, "r_min": 0.40, "r_max": 0.60, "gap_weight": 0.50},
            {"zone": 4, "r_min": 0.60, "r_max": 0.80, "gap_weight": 0.35},
            {"zone": 5, "r_min": 0.80, "r_max": 0.95, "gap_weight": 0.25},
            {"zone": 6, "r_min": 0.95, "r_max": 1.00, "role": "reinforced shell/frame"},
        ],
        "outputs": outputs,
    }
    (output_dir / f"{p.name}_manifest.json").write_text(
        json.dumps(manifest, indent=2), encoding="utf-8"
    )
    return manifest


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path("AXZ_Cube_Output"))
    parser.add_argument("--side", type=float, default=63.5)
    parser.add_argument("--voxel", type=float, default=0.95)
    args = parser.parse_args()
    p = CubeParameters(side_mm=args.side, voxel_mm=args.voxel)
    export_cube(p, args.output)


if __name__ == "__main__":
    main()
