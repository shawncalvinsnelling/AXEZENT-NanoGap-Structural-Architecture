# Geometry-validation findings and research limitations

**Mesh structure:** All five binary STL files are structurally parsable, with actual byte lengths equal to `84 + 50*(facet count)`; each has a nonzero facet count. The original manifest reports watertight checks. Structural parsing is not an independent fabrication or safety certification.

**High-resolution geometry (original STL):** 63.50-mm nominal cubic envelope; 1,696,350 triangles; 73,683.14 mm3 modeled volume; 202,927.50 mm2 modeled area; ~28.777% modeled solid fraction.

**Standard-resolution geometry (original manifest):** 672,786 triangles and 59,222.40 mm3 volume; ~23.13% solid fraction. Difference is ~24.42% relative to standard, a substantial mesh-convergence warning. Do NOT assume both represent the same quantity of material in mechanics simulations.

**Phase-gradient issue:** Nominal `P(r)` is not the local wavelength when phase is `phi_x = 2*pi*x/P(r)`; where x dominates Chebyshev radius, the phase period is `P_phase = P(r)^2/(P(r)-r*P_prime(r))`, e.g. `P_phase ~= 3.975 mm` at `r=1` versus nominal `P(1)=8 mm`. This does not directly give pore diameter. Validate phase continuity and local feature distributions before redesign.

**Physical status:** No independent fabrication receipt, micro-CT, force-displacement curve, impact trace, elastic-property fit, fatigue test, or validated finite-element prediction was available in the supplied original package. No proof of superior strength or impact protection. No tested wall geometry.

**Print-readiness controls:** examine wall thickness and minimum gaps, unsupported overhangs, trapped support/uncured material, build orientation, slicer healing, mesh normals, specimen-to-specimen variation, and as-printed versus CAD mass/dimensions. The previous print README provides illustrative settings, not an experimentally qualified process.

**Test interpretation:** match polymer batch/process, specimen envelope and relative density. Compare both intact and intentionally damaged samples; document actual relative density, maximum stress, stiffness, energy absorption and uncertainty. Different performance metrics may produce different winners.
