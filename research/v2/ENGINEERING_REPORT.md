# AXEZENT NanoGap v2.0 — controlled geometric preflight

**Author:** Shawn Calvin Snelling  
**Study date:** November 12, 2026  
**Evidence level:** Numerically generated CAD and analytical verification, **not a mechanical-strength experiment**.

## Research question

Can the original July 2026 63.5-mm graded gyroid cube's variable pitch be implemented with a mathematically corrected phase so that the local phase period along each cube-face-normal dominant ray agrees with the specified `P(r)=14-6r^1.35` mm, while keeping the rest of the cube architecture fixed?

**Answer:** Yes, as an explicit phase construction; two preliminary STL mesh resolutions were generated successfully and tested for mesh consistency.

## Actual baseline

The original cube computes the Chebyshev radius `r = max(|x|,|y|,|z|)/31.75` (clamped to [0,1]), the pitch `P(r)=14-6r^1.35` mm, the graded threshold `tau(r)=0.27+0.21r^1.60`, and phase `phi_i = 2*pi*x_i/P(r)`. Along a ray where x is the positive dominant coordinate (`x=31.75r`), the original local x-phase period is:

```
P_original_phase(r) = P(r)^2/(P(r)-r*P'(r))
                    = (14-6*r^1.35)^2/(14+2.1*r^1.35) mm.
```

At r=1, the nominal pitch is 8 mm, but the local phase period is approximately **3.9752 mm**. This mathematical phase period is not necessarily the pore diameter.

## New design: ray-integrated phase

Retain the original `P`, `tau`, tetrahedral struts, frame and NanoGap coupling. Define the one-dimensional cumulative phase primitive:

```
I(r) = integral from 0 to r of (1/P(t)) dt.
k_eff(r) = 2*pi*I(r)/r   for r>0;
k_eff(0) = 2*pi/14.
phi_i(x,y,z) = k_eff(r) * x_i.
```

For each dominant-axis positive ray with `x_i=31.75r` and `dr/dx_i=1/31.75`, `phi_i=2*pi*31.75*I(r)`. Hence the derivative is `dphi_i/dx_i = 2*pi/P(r)`, and the local phase period on that ray equals `P(r)`. The same applies on negative signed rays using phase symmetry. The integral is calculated by numerical quadrature and interpolated, introducing a small controllable numerical approximation.

**Limit:** This is a *ray-corrected* phase. It does not enforce isotropic 8–14 mm lattice wavelengths in every arbitrary spatial direction, nor does it constitute an eikonal PDE solution. The Chebyshev shell gradient has nondifferentiable sector boundaries; gradient and connectivity checks remain appropriate at shell transitions.

The gyroid is still:

```
G = sin(phi_x)*cos(phi_y) + sin(phi_y)*cos(phi_z) + sin(phi_z)*cos(phi_x)
```

The unchanged NanoGap proximity rule:

```
K(d) = exp(-0.22*d), d in mm to nearest tetrahedral strut
T_eff = tau(r) + 0.080*K(d)
solid gyroid sheet when abs(G) <= T_eff.
```

Four support segments extend from the center toward alternating tetrahedral points with coordinate magnitude `h=0.72*31.75=22.86 mm`; center sphere radius 3.5 mm; strut radius 1.65 mm; 12 outer-edge rails with nominal width 3.8 mm. The complete solid is an implicit union clipped by the 63.5-mm cube envelope, then converted to STL via marching cubes.

## Measured geometric results (not force or stress results)

| Geometry | Requested sampling pitch | STL facets | Closed mesh | Modeled material volume (mm³) | Material fraction |
|---|---:|---:|---|---:|---:|
| Reconstructed v1-style control | 0.85 mm | 858,662 | yes | 62,558.57 | 24.43% |
| Reconstructed v1-style control | 0.60 mm | 1,696,350 | yes | 73,683.14 | 28.78% |
| v2 ray-phase-corrected | 0.85 mm | 635,618 | yes | 76,946.42 | 30.05% |
| v2 ray-phase-corrected | 0.60 mm | 1,225,826 | yes | 76,252.02 | 29.78% |

All four meshes are reported watertight with consistent winding. The 0.60-mm v1-style reconstruction matches the previous high-resolution master **facet count** and volume to approximately 0.00013 mm³, providing an independent baseline consistency check; its STL checksum is not asserted equal to the historical master because triangulation/serialization may differ.

Between the two sampling resolutions, the modeled volume difference relative to the fine mesh is **15.10% for v1** and **0.91% for v2**. This is preliminary evidence of *improved numerical mesh stability* of the v2 construction within this two-resolution experiment. Additional finer-mesh testing and topology checks are required to establish convergence rigorously.

At the same 0.60-mm sampling, v2 has about **one percentage point more modeled material** (29.78% vs. 28.78%), so the two structures are **not matched-density specimens**. Density-normalized strength or absorption comparisons cannot be inferred.

## What has actually passed

1. Seven source-math unit tests, including the ray-phase derivative test.
2. Watertight and consistently oriented triangular surfaces for all four computational outputs.
3. File checksums, triangle counts, dimensions and volume recorded in `models/*.json`.
4. Agreement of baseline fine-mesh facet count and volume with the historic high-resolution cube.
5. A real geometric cross-section and STL surface comparison, rendered from computational data, not synthetic imagery.

## Critical unresolved work

- **Printability:** mesh watertightness is insufficient; check closed cavities, trapped resin/powder, minimum feature size, overhangs, support strategy, shrinkage and metrology. Validate on chosen manufacturing process and material.
- **Convergence:** evaluate at additional spatial sampling and compare local connected components and genus, not volume alone.
- **Constant density:** tune or normalize `tau_core`, `tau_shell`, or member dimensions to equalize material volume before comparing strength or energy absorption.
- **Mechanics:** specify a material constitutive model, boundary conditions, compression planes, impact speeds, mesh-quality checks, and use validated finite-element methods; perform physical replicates.
- **Defect intelligence:** the v2 generator does NOT yet locate weak points under load or independently adapt material thickness to calculated stress. That is a proposed *future algorithm*, not an implemented result.
- **Scientific comparisons:** MIT/Northeastern's scale-rich network has established published results in particular tested materials and geometries; there is no evidence from this geometric experiment that AXEZENT is stronger or better in impact absorption.

## Next experimental protocol

1. Preserve and hash v1.0 master STL as control. Use the v2 fine STL only for geometric evaluation until print settings are validated.
2. Produce constant-mass geometry variants in identical CAD envelope.
3. Perform 3D printability and metrology review; check final measured density and thickness distributions.
4. Use matched-material compression and impact mechanical tests with multiple specimens and transparent raw force-displacement records.
5. Report absorbed energy per mass, initial stiffness, peak and failure forces, damage locations and uncertainty bounds. Keep finite computation, conditional predictions and empirical findings distinct.

**Distribution update (Nov. 12, 2026):** the v2 source and numerical results are now included in this public research repository at the author's direction. The binary STL files are recorded by SHA-256 but are not included as Git blobs here. No v2 STL has been emailed to the MIT/Northeastern team, and no mechanical test is claimed.