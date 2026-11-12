# AXEZENT NanoGap — V1→V2 Engineering Research (2026-11-12)

**Author: Shawn Calvin Snelling.** This is one **continuing research repository** with a frozen original baseline and a separate, reproducible improvement. Version labels identify engineering states—not claims of perfection.

## Start here

- [Engineering report](ENGINEERING_REPORT.md): equations, model assumptions, four measured meshes, limitations and next experiment.
- [V2 generator](source/nanogap_v2_geometry.py): exact reproducible design algorithm, with both \`v1\` (historical-style control) and \`v2\` (ray-integrated phase) options.
- [Measured results](data/GEOMETRY_METRICS.csv): reported STL facets, geometry volume, surface area, material fraction, and SHA-256 for four numerical output files.
- [Mathematical and scale notes](../../docs/LOGICAL_SCALE_AND_QUINTILLION_ADDRESSING.md): separately labeled NODES address mathematics, not a claim about physical structures.
- [Main site](../../index.html) and [original v1 mathematics](../../docs/MATHEMATICS.md).

## Precisely what changed

The original uses \`phi_j = 2*pi*x_j/P(r)\`, with \`P(r)=14-6*r^1.35\` mm and \`r=max(|x|,|y|,|z|)/31.75\` clipped to [0,1]. On a dominant-axis ray, the actual phase period can differ from nominal \`P\`.

The new design uses \`I(r)=∫_0^r dt/P(t)\` and \`phi_j=2*pi*x_j*I(r)/r\`, with its continuous limit at \`r=0\`. Along a coordinate-dominant ray, \`dphi_j/dx_j=2*pi/P(r)\`, so the local phase period on that ray equals nominal \`P(r)\`. This is **not** a proof of isotropic local period everywhere in 3D.

The original tetrahedral internal struts, node, twelve edge rails, and distance-dependent NanoGap threshold boost are intentionally unchanged.

## Numerical preflight results

| Mesh setting (mm) | V1 fraction | V2 fraction |
|---|---:|---:|
| Target 0.85 | 24.43% | 30.05% |
| Target 0.60 | 28.78% | 29.78% |

Reported discrepancy in material volume between those two resolutions, relative to fine mesh: **15.10% v1** versus **0.91% v2**. These are comparisons of *reported CAD geometry*, not material strength, elasticity, or physical validation. The meshes are not density-matched; a strength ranking is not supported.

## Run the study yourself

Requires Python 3.11+; for actual meshing install \`numpy scipy scikit-image trimesh\` (see the source for imports). Depending on resolution and system libraries, meshing may use >1 GB RAM.

\`\`\`bash
python -m pip install numpy scipy scikit-image trimesh
python research/v2/source/nanogap_v2_geometry.py --output out --method v2 --voxel 0.85
python research/v2/source/nanogap_v2_geometry.py --output out --method v2 --voxel 0.6
python research/v2/source/nanogap_v2_geometry.py --output out --method v1 --voxel 0.85
python research/v2/source/nanogap_v2_geometry.py --output out --method v1 --voxel 0.6
python -m unittest discover -s tests -v
\`\`\`

Use the generated JSON receipts to compare bounds, volume, signed winding, facets, mesh closure and SHA-256. Mesh-byte checksums can change with dependency versions and serialization; numerical results must be checked independently.

### Model file policy

This repository contains the **full v2 generator and numerical receipts**. The four binary STL outputs are significantly larger than text artifacts and are not implied to be present just because hashes are listed. The original research archive contains the binaries; generate from source to obtain new files. Before physical strength testing, perform minimum feature-size checks, mesh convergence, density matching and actual fabrication characterization.

### Evidence boundaries

- **Verified:** mathematical formula manipulations; source tests; archived mesh diagnostics and SHA-256 receipts.
- **Preliminary:** numerical volume variation across two sampling resolutions.
- **Not established:** actual load capacity, impact advantage, manufacturing repeatability, structural failure predictions, nanometer-scale fabricated gaps, autonomous weak-point repair, or strength superiority to MIT/Northeastern.
