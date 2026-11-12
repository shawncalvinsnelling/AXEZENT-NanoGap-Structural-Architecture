# AXEZENT A–Z — Unified Research Index

**Author and public attribution:** Shawn Calvin Snelling  
**Purpose:** One navigable research record preserving historical artifacts, new reproducible studies and explicit evidence status.  
**Repository scope:** Structural geometry and closely related mathematical research. The name “A–Z” denotes the scope of proposed cross-disciplinary investigation, **not** a claim that all sciences, inventions or historical archives have been loaded, validated or automated.

## Research layers in logical chronological order

| Date / phase | Area | Artifact | Status |
|---|---|---|---|
| July 2026, baseline | Graded architected materials | [Original v1 generator](../source/AXZ_Cube_v1_0_generator.py), [parameter manifest](../source/AXEZENT_Original_Design_Manifest.json), [mathematics](MATHEMATICS.md), archived physical-model photograph and selective STL downloads | **Implemented CAD; photographed sample; mechanical strength not tested** |
| November 11, 2026 | Laboratory collaboration | [research brief](../assets/documents/AXEZENT_Research_Brief.pdf), [laboratory protocol](LAB_TEST_PROTOCOL.md), [provenance](PROVENANCE.md) | **Study proposed; external tests not yet independently reported** |
| November 12, 2026 | NanoGap v2 geometry | [v2 mathematical generator](../research/v2/source/nanogap_v2_geometry.py), [study data](../research/v2/data/GEOMETRY_METRICS.csv), [report](../research/v2/ENGINEERING_REPORT.md), [real comparison figures](../research/v2/figures/V1_V2_ACTUAL_STL_COMPARISON.png) | **Numerical CAD preflight, ray-phase correction; not a strength claim** |
| November 12, 2026 | Large logical NODES architectures | [Quintillion-scale integer addressing](LOGICAL_SCALE_AND_QUINTILLION_ADDRESSING.md), [tests](../tests/test_quintillion_addressing.py) | **Exact arithmetic for 64-bit address tuples; no physical quintillion-node cube** |
| November 12, 2026 | A–Z mathematical discovery example | [Optical chirality bias-correction model](../research/discovery_engine/CHIRALITY_MODEL.md), [Python calculator](../research/discovery_engine/chirality_calibration.py), [tests](../tests/test_chirality_calibration.py) | **Algebraic identity and synthetic-data tests only; no laboratory validation or priority claim** |

## What “A–Z” means operationally

Use a common reproducible discovery cycle:

`source → question → assumptions and units → equations/model → tests or proof → negative controls → independent reproduction → evidence status → next falsifiable experiment.`

Prioritized cross-disciplinary tracks:

| Track | Domains to combine | Candidate output | Boundary |
|---|---|---|---|
| Structural weakness mapping | Gyroid geometry, mechanics, topology, additive manufacturing, numerical optimization | Measured stress concentrations and controlled FEA benchmark | Not implemented in the v2 geometric source |
| Optical chirality | Nanophotonics, measurement calibration, statistics, nanotube optics | Cross-ratio estimator under separable-gain assumptions | Simulated/example-only |
| Sensor robustness | Photonics, signal processing, Bayesian inference, metamaterials | A blinded detection benchmark with noise and drift controls | Research hypothesis |
| Material recovery | Polymer science, material fatigue, embedded sensing | A control experiment distinguishing actual healing from sensor drift | Research hypothesis |
| Large-scale simulation bookkeeping | Integer addressing, sparse storage, topology, provenance receipts | Collision-free 64-bit logical indices and source-hash traceability | Exact indices do not imply physical storage or realized states |
| Computational music and sound | Music theory, psychoacoustics, DSP, musical synthesis | Reproducible synthesis and perceptual evaluation | Separate creative program; not evidence for material strength |
| Security and software | Cryptography, software assurance, reproducible builds | Audited software, threat models and independent benchmarks | No claims of unbreakable encryption or infallibility |

## Other historical AXEZENT works

Past discussion references higher-Lie projects, quantum transport, photonic work, mathematics atlases, beat-generation software, computer security, prototypes and architecture models. This repository does **not** claim to contain all those repositories, every song, every invention, all software history or private research records. They should each remain in their designated source repositories, with **verified links and citation metadata** added here only when appropriate.

**Important:** The independently uploaded 342-topic inventory and older 3,000-test chirality package described in the conversation were not available as verified source files for import during this GitHub update. The new chirality Python module provides a separate reproducible implementation and its own CI tests. No claim is made that it recovers a complete earlier archive.

## Research status vocabulary

- **PROVED:** general symbolic claim with all assumptions and proof present.
- **VERIFIED_FINITE:** executable or numeric claim verified for a declared finite scope.
- **SIMULATED:** model-dependent calculation, not measured physical evidence.
- **CONDITIONAL:** implication holds only with explicitly unproved assumptions.
- **HYPOTHESIS:** proposed idea requiring new calculations or testing.
- **OPEN:** unclosed proof or experimental obligation.

These labels must not be upgraded based on model appearance, high iteration counts, elapsed computation, or an author's expectation.

## Intellectual-property boundary

The repo is **public** and includes the mathematical generator and selected STL geometry; publicity can affect trade-secret or patent opportunities. Do not upload personal information, credentials, unreleased music masters or other private archives just to make the A–Z index look comprehensive. Historical artifact filenames remain unchanged for provenance, but public credit uses **Shawn Calvin Snelling**.

## Next experimental requirement

The next scientifically decisive test is *equal material mass and fabrication conditions* for v1 and v2. Construct a trustworthy finite-element stress model with measured material data and compare it with repeated laboratory compression and impact experiments. Any superiority statement must be tied to material, density, geometry, boundary conditions and uncertainty.
