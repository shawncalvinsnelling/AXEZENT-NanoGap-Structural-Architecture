"""AXEZENT A-Z research example: chirality contrast calibration under a declared model.

Author: Shawn Calvin Snelling
Evidence: algebraic identity and deterministic synthetic-data tests ONLY.
Not a claim of experimentally validated optics or scientific novelty.

Model: I[s,p] = A_s * G_p * (1 + s*p*g/2), s,p in {-1,+1}.
Allows sample amplitude A_s and polarization-only gain G_p.
"""
from __future__ import annotations

import math
import random
from dataclasses import dataclass


@dataclass(frozen=True)
class ContrastResult:
    true_contrast: float
    apparent_single: float
    recovered_cross_ratio: float
    gain_ratio: float


def readings(
    contrast: float,
    gain_plus: float = 1.0,
    gain_minus: float = 1.0,
    sample_plus: float = 1.0,
    sample_minus: float = 1.0,
    pair_specific_gain=None,
):
    if not (-2.0 < contrast < 2.0):
        raise ValueError("Contrast must be between -2 and +2.")
    if min(gain_plus, gain_minus, sample_plus, sample_minus) <= 0:
        raise ValueError("All gains/amplitudes must be positive.")
    values = {}
    for sample in (-1, +1):
        a = sample_plus if sample == 1 else sample_minus
        for pol in (-1, +1):
            g = gain_plus if pol == 1 else gain_minus
            special = 1.0 if pair_specific_gain is None else pair_specific_gain.get((sample, pol), 1.0)
            if special <= 0:
                raise ValueError("Pair-specific gains must be positive.")
            values[(sample, pol)] = a * g * (1.0 + sample * pol * contrast / 2) * special
    return values


def apparent_contrast(intensities, sample=1):
    plus = intensities[(sample, +1)]
    minus = intensities[(sample, -1)]
    return 2 * (plus - minus) / (plus + minus)


def cross_ratio_contrast(intensities):
    """Cancels separable A_s and G_p exactly; not sample-dependent gains."""
    a = intensities[(+1, +1)]
    b = intensities[(+1, -1)]
    c = intensities[(-1, +1)]
    d = intensities[(-1, -1)]
    if min(a, b, c, d) <= 0:
        raise ValueError("Intensities must be strictly positive.")
    # sqrt(ad/bc)=(1+g/2)/(1-g/2).
    log_r = 0.5 * (math.log(a) + math.log(d) - math.log(b) - math.log(c))
    return 2 * math.tanh(log_r / 2)


def example(contrast=0.001940, gain_ratio=1.0182):
    data = readings(contrast, gain_plus=gain_ratio)
    return ContrastResult(
        true_contrast=contrast,
        apparent_single=apparent_contrast(data),
        recovered_cross_ratio=cross_ratio_contrast(data),
        gain_ratio=gain_ratio,
    )


def randomized_identity_check(trials=3000, seed=20261112):
    rng = random.Random(seed)
    max_error = 0.0
    for _ in range(trials):
        contrast = rng.uniform(-0.15, 0.15)
        vals = readings(contrast,
                        gain_plus=math.exp(rng.uniform(-2,2)),
                        gain_minus=math.exp(rng.uniform(-2,2)),
                        sample_plus=math.exp(rng.uniform(-2,2)),
                        sample_minus=math.exp(rng.uniform(-2,2)))
        max_error = max(max_error, abs(cross_ratio_contrast(vals)-contrast))
    return max_error


def simulated_noise(num_pairs=1000, rel_sigma=.0015, seed=20261112):
    rng = random.Random(seed)
    base = readings(.001940, gain_plus=1.0182, sample_plus=.93, sample_minus=1.11)
    estimates = []
    for _ in range(num_pairs):
        noisy = {key: value * math.exp(rng.gauss(0.0, rel_sigma)) for key, value in base.items()}
        estimates.append(cross_ratio_contrast(noisy))
    return {"n":num_pairs,"mean":sum(estimates)/num_pairs,
            "min":min(estimates),"max":max(estimates),"input":.001940}


if __name__ == "__main__":
    result = example()
    print(result)
    print("max absolute identity error (3,000 tests):", randomized_identity_check())
    print("synthetic noise:", simulated_noise())
    print("0.5% sample-dependent gain violation:",
          cross_ratio_contrast(readings(.001940,
            pair_specific_gain={(+1,+1):.995})))
