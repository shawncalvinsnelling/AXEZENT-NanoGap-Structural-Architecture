# AXEZENT A–Z Discovery Laboratory: Optical Chirality Calibration

**Research author:** Shawn Calvin Snelling  
**Status:** Verified algebra in a stated model; simulated numerical sensitivity. **No laboratory measurement or priority claim.**

## Problem

An observed optical circular-polarization contrast may mix the specimen's intrinsic dichroism with unequal instrument amplification. A small gain imbalance can overwhelm a small real signal. This example explores a bias-cancelling estimator and an explicit failure mode. It is not a structural strength simulation or evidence that the existing STL has optical functionality.

Let \`s∈{-1,+1}\` denote two samples of opposite handedness and \`p∈{-1,+1}\` denote two circular polarizations. Assume all intensities are positive and

\`\`\`text
I[s,p] = A[s] * G[p] * (1 + s*p*g/2)
\`\`\`

where \`A[s]>0\` is sample-specific amplitude, \`G[p]>0\` is polarization-specific gain shared between samples, and \`g∈(-2,2)\` is true intrinsic contrast. This factorization is a **hypothesis**, not a universal optical law.

The usual single-sample estimator is

\`\`\`text
g_apparent = 2 * (I[+,+]-I[+,-])/(I[+,+]+I[+,-]).
\`\`\`

Instead form the gain-cancelling cross ratio

\`\`\`text
R = sqrt(I[+,+]*I[-,-] / (I[+,-]*I[-,+]))
  = (1+g/2)/(1-g/2).
g_recovered = 2*(R-1)/(R+1).
\`\`\`

Using \`log(R)\` with \`2*tanh(log(R)/2)\` is more numerically stable when \`R\` is close to 1.

**Proof:** Numerator cancels the \`A[+]*A[-]*G[+]*G[-]\` product in the denominator; the remaining contrast factors are \`(1+g/2)^2\` and \`(1-g/2)^2\`. For \`|g|<2\`, the positive square root gives the stated identity.

## Deterministic checks

\`research/discovery_engine/chirality_calibration.py\` runs **3,000 randomized algebraic cases** and an independent **1,000-pair synthetic-noise experiment**. The seed is fixed. The tests are included in the main GitHub Actions CI, and use only the Python standard library.

Illustration: with \`g=0.001940\` and a polarization gain ratio of \`1.0182\`, the single-sample apparent contrast is over ten times larger than the real contrast, but the cross ratio recovers the input **within the factorized model**.

The approach can **fail** when the polarization gain depends on sample handedness, or when additive backgrounds, mixing, detector nonlinearities, misregistration or systematic drift violate the assumptions. The tests intentionally introduce a 0.5% pair-specific gain perturbation that can reverse the recovered sign.

## Scientific status

This is a reproducible **model-level calibration result**. It has not been validated on nanotube trions, plasmonic nanogaps, manufactured photonic devices, or experimental measurements. The estimator's novelty has not been established: cross-ratio techniques and gain cancellation already occur in several fields. An appropriate literature-priority audit and independent laboratory calibration would be needed before publication claims.

## Next falsifiable experiment

Use left/right circular measurements from two sample handednesses, acquire gains and blanks under randomized measurement order, vary instrument gain imbalance deliberately, and evaluate recovery bias with bootstrap uncertainty. Design controls where the factorization fails. Publish raw instrument responses and a preregistered analysis protocol.

Related project mathematics: [NanoGap structural geometry](../../docs/NANOGAP_MATHEMATICAL_AUDIT.md), [v2 geometry](../v2/README.md), and [A–Z research index](../../docs/AZ_RESEARCH_INDEX.md).
