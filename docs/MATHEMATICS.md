# Mathematical architecture — v1.0 as implemented

Source of truth: `source/AXZ_Cube_v1_0_generator.py`, `source/AXEZENT_Original_Design_Manifest.json`.

Use local coordinates (x,y,z) centered on the 63.5 mm cube, with half-edge H=31.75 mm and clipped cube-shell radius `r = min(1, max(|x|, |y|, |z|)/H)`.

- Nominal pitch: `P(r) = 8 + (14-8)(1-r^1.35) = 14 - 6r^1.35` mm.
- Grading threshold: `tau(r)=0.27+(0.48-0.27)r^1.60` (dimensionless implicit-level parameter).
- Gyroid: `G=sin(kx)cos(ky)+sin(ky)cos(kz)+sin(kz)cos(kx)`, with `k=2*pi/P(r)`.
- Tetrahedral endpoints: `(h,h,h)`, `(h,-h,-h)`, `(-h,h,-h)`, `(-h,-h,h)`, with `h=0.72*31.75=22.86 mm`.
- `d` is Euclidean distance to the nearest line segment joining origin and one endpoint.
- NanoGap: `K(d)=exp(-0.22*d)`, `tau_eff=tau+0.08*K(d)`.
- Gyroid sheet solid: `abs(G)<=tau_eff`.
- Union with four struts of radius 1.65 mm, central sphere radius 3.5 mm and twelve edge rails of width 3.8 mm; clipped to the 63.5 mm envelope.
- Marching-cubes triangulation via `scikit-image`, mesh processing/export via `trimesh` and array fields via `numpy`.

### Audit of the local phase

The implementation uses `phi_x(x)=2*pi*x/P(r)` (and analogously for y,z). On a ray where `r=x/H` (x>0), `d phi_x/dx = (2*pi/P(r)^2)*(P(r)-r P'(r))`. Therefore:

`P_phase(r) = P(r)^2/[P(r)-r P'(r)]`.

At r=1, `P(1)=8 mm`, but `P_phase(1)≈3.975 mm`. This is a local phase period, **not** a physical pore diameter or material strength. The original finite mesh volumes also differ materially by resolution and cannot both be treated as a mesh-converged material fraction.

### Scope of the “NanoGap” label

The project name describes the exponential proximity-coupling rule; it does **not** establish nanometer physical features or a proven autonomous weakness scanner. Mechanical optimization and force-dependent reinforcement remain planned research.
