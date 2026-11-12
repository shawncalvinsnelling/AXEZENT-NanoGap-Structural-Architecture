# NanoGap geometry: mathematical verification note

**Research author:** Shawn Calvin Snelling  
**Scope:** Exact documented **v1.0 implementation**, not a proof of mechanical superiority.  
**Source:** [original Python generator](../source/AXZ_Cube_v1_0_generator.py) and [original parameter manifest](../source/AXEZENT_Original_Design_Manifest.json).

## 1. Domain and graded lattice

Take a centered cube of side `L=63.5 mm` with half-side `H=31.75 mm`.
Define the Chebyshev shell coordinate

```text
r(x,y,z) = min(1, max(abs(x),abs(y),abs(z))/31.75).
P(r) = 14 - 6*r**1.35                         [mm]
tau(r) = 0.27 + 0.21*r**1.60                  [dimensionless]
k(r) = 2*pi/P(r)                             [rad/mm]
G(x,y,z) = sin(k*x)*cos(k*y) + sin(k*y)*cos(k*z) + sin(k*z)*cos(k*x)
```

Thus `8 <= P <= 14 mm` and `0.27 <= tau <= 0.48` for `0 <= r <= 1`. The value `P` is a *nominal phase parameter*, not automatically the realized pore diameter.

## 2. Tetrahedral support and NanoGap proximity

The four endpoints are `(+h,+h,+h)`, `(+h,-h,-h)`, `(-h,+h,-h)`, `(-h,-h,+h)` where `h = 0.72*H = 22.86 mm`.
For position `q=(x,y,z)`, and endpoint `v`, the distance to the finite support segment `[0,v]` is

```text
t(q,v) = clamp(dot(q,v)/dot(v,v), 0, 1)
d(q,v) = norm(q - t(q,v)*v)
d(q)   = min over the four endpoints v of d(q,v)
```

The v1.0 *NanoGap* mathematical term is

```text
K(d) = exp(-0.22*d)                           [d in mm]
tau_eff(r,d) = tau(r) + 0.080*K(d)
F_gyro(x,y,z) = abs(G(x,y,z)) - tau_eff(r,d)
```

The gyroid part of the solid is `F_gyro<=0`. Since `d>=0`, it follows that `0<K<=1` and `tau(r)<tau_eff<=tau(r)+0.080` for finite `d`; `0.27<tau_eff<=0.56` for the finite cube. At a support, `K(0)=1`. The coupling contribution halves after `ln(2)/0.22 ≈ 3.15 mm` and drops to 10% after `ln(10)/0.22 ≈ 10.47 mm`. These are characteristics of the **formula**, not measured structural strength.

## 3. Added solids and conversion to STL

Four cylinder-like struts of radius `1.65 mm`, a center sphere of radius `3.5 mm`, and twelve edge rails with `3.8 mm` nominal width are combined by minimum-field union; a cube clipping field limits the external envelope. A sampled implicit field is meshed with marching cubes and processed with `trimesh`. These operations define a *geometric design*, not a validated load-bearing performance model.

## 4. Phase-gradient check: a known design limitation

The source uses `phi_x(x)=2*pi*x/P(r)`, where `r=x/H` along a positive x-dominant ray. Its derivative is

```text
d(phi_x)/dx = 2*pi*(P(r)-r*P'(r))/P(r)**2
P'(r) = -8.1*r**0.35
P_phase(r) = P(r)**2 / (P(r)-r*P'(r))
           = (14-6*r**1.35)**2/(14+2.1*r**1.35)       [mm]
```

At `r=1`, nominal `P(1)=8 mm` but local x-phase period `P_phase(1)=64/16.1 ≈ 3.975 mm`. This derivation applies along such a ray away from cube-shell transitions; general three-dimensional local spacing requires the full phase gradient. The result is **not** a claim that pores are 3.975 mm wide.

## 5. Mesh-resolution warning

The original manifest reports approximately `59,222.40 mm³` material volume for the standard 63.5 mm mesh and `73,683.14 mm³` for the high-resolution master — a substantial mismatch at nominally equal design settings. The reported solid fractions are approximately `23.13%` versus `28.78%` of the envelope. Before any mechanical ranking, check mesh convergence, source parameters, mesh orientation, print fidelity and consistent relative density.

## 6. Research boundary

The geometric generator does **not** contain a finite-element solver, an experimentally calibrated strength model or a closed-loop weak-point optimizer. For those capabilities, implement independent FEA and experimental validation. Do not describe `NanoGap` as demonstrated nanometer-scale fabrication, self-healing, or proof that the design is stronger than MIT/Northeastern's materials.

A standard-library-only regression suite is included at [tests/test_nanogap_equations.py](../tests/test_nanogap_equations.py) to independently verify the numeric formulas and analytic phase derivative.
