# Proposed third-party evaluation protocol (for discussion, not a claim of completed testing)

## Stage 0 - Reconcile model and choose a print-fidelity standard

- Review supplied 63.5-mm high-resolution master, standard-resolution cube, 38.1-mm calibration cube, and source.
- Re-export meshes at 0.95, 0.60 and preferably one finer sampling resolution as computational resources permit; independently compare solid volume, area, connectivity, minimum web thickness and pore size distribution. Repair any inconsistent phase/pitch behavior before treating upgraded geometry as the same design.
- Record slicer import units as millimeters; document any model repairs or reorientation.

## Stage 1 - Fabrication feasibility

- Begin with the 38.1-mm calibration file to verify lattice openness, fused supports, frame fidelity and clear internal voids, and then perform selected 63.5-mm full-size prints.
- Fix material chemistry, manufacturer/batch, humidity/conditioning, nozzle and process parameters. Record orientation, thermal profile, nozzle diameter, build direction, wall settings, support strategy, and post-processing.
- Measure specimen mass, external dimensions, visible cracks, pore obstruction and deviations from intended minimum feature sizes; consider micro-CT where available.
- Do not mechanically compare the calibration sample directly with full-size samples as if scale were immaterial.

## Stage 2 - Design of matched comparisons

- Select appropriate reference specimens such as uniform lattice, an independently reproducible scale-rich network from the cited publication, and optionally an ungraded gyroid control.
- Match **actual** volume fraction, material, specimen envelope, loading direction and print quality. A nominally ~28.8% solid AXEZENT model is not a controlled match to ~40% reference material.
- Replicates: a minimum exploratory goal is n >= 5 per condition, with final sample count and statistical power determined by the laboratory.

## Stage 3 - Mechanical experiments

- Compression: record force, displacement, sample area, initial stiffness, plateau/crush behavior, damage initiation, densification and failure patterns; report strain rate and machine calibration.
- Impact (where equipment and safety procedures permit): control impact energy, striker geometry, supports and sample geometry; report force-time, absorbed/recovered energy and peak transmitted force.
- Vulnerability: compare pristine samples to deliberately seeded, geometrically reproducible notch/beam-removal/interface defects, with documented defect sizes and location.
- Metrics: compressive strength under a specified failure criterion, normalized stiffness E_eff/E_s, absorbed energy W = integral(F dx), specific absorbed energy W/m, peak transmitted force and damage tolerance. Give means/uncertainty for all replicates.

## Stage 4 - Computational corroboration

- Derive a mesh- and boundary-condition-converged elastic-plastic/viscoelastic model of the actual print material; include anisotropy if applicable.
- Compare pre-test predictions and experimental outcomes. No simulation has been asserted as already run for this submission.
- If useful, explore topology optimization/defect-aware reinforcement as a **future new AXEZENT version**, separate from the supplied immutable v1.0 model.

## Collaboration questions

1. Does the lab consider the files manufacturable and suited to a matched benchmark?
2. What process/material and controls would it recommend?
3. What scope, personnel, timeline, budget or institutional collaboration terms would be involved?
4. How should proprietary design information, attribution, authorship, and results-sharing be handled before testing?
