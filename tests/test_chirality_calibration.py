"""Regression tests for AXEZENT chirality cross-ratio study (synthetic)."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "research" / "discovery_engine"))
from chirality_calibration import (readings, apparent_contrast,
    cross_ratio_contrast, randomized_identity_check, example, simulated_noise)


class ChiralityTests(unittest.TestCase):
    def test_3000_randomized_algebraic_identities(self):
        self.assertLess(randomized_identity_check(), 2e-14)

    def test_bias_from_1point82_percent_instrument_gain(self):
        result = example()
        self.assertGreater(abs(result.apparent_single), 10 * abs(result.true_contrast))
        self.assertAlmostEqual(result.recovered_cross_ratio, result.true_contrast, places=12)

    def test_sample_amplitude_cancelled(self):
        data = readings(.013, sample_plus=1e-3, sample_minus=30.0,
                        gain_plus=5.0, gain_minus=.2)
        self.assertAlmostEqual(cross_ratio_contrast(data), .013, places=12)

    def test_pair_specific_gain_can_reverse_sign(self):
        biased=readings(.001940,pair_specific_gain={(+1,+1):.995})
        self.assertLess(cross_ratio_contrast(biased),0)

    def test_1000_seeded_noisy_pairs(self):
        result=simulated_noise()
        self.assertEqual(result["n"],1000)
        self.assertLess(abs(result["mean"]-result["input"]),.0002)

    def test_invalid_intensities_rejected(self):
        with self.assertRaises(ValueError):
            cross_ratio_contrast({(+1,+1):1,(+1,-1):1,(-1,+1):1,(-1,-1):0})

    def test_formula_no_instrument_effect(self):
        vals = readings(.002)
        self.assertAlmostEqual(apparent_contrast(vals),.002,places=12)


if __name__ == "__main__":
    unittest.main()
