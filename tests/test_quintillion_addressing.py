"""Exact 64-bit AXEZENT NODES address arithmetic; no physical-node claims."""
import math
import random
import unittest

SHELL_BITS = 11
CHANNEL_BITS = 16
LEAF_BITS = 37
LEAF_MASK = (1 << LEAF_BITS) - 1
CHANNEL_MASK = (1 << CHANNEL_BITS) - 1
SHELL_MASK = (1 << SHELL_BITS) - 1

def encode(s, c, i):
    if not (0 <= s <= SHELL_MASK and 0 <= c <= CHANNEL_MASK and 0 <= i <= LEAF_MASK):
        raise ValueError("field out of range")
    return (s << 53) | (c << 37) | i

def decode(a):
    if not (0 <= a < (1 << 64)):
        raise ValueError("address out of range")
    return ((a >> 53) & SHELL_MASK, (a >> 37) & CHANNEL_MASK, a & LEAF_MASK)

class AddressMathTests(unittest.TestCase):
    def test_total_count(self):
        self.assertEqual((1<<11)*(1<<16)*(1<<37), 1<<64)
        self.assertEqual(1<<64, 18446744073709551616)
    def test_extremes(self):
        self.assertEqual(encode(0,0,0),0)
        self.assertEqual(encode(SHELL_MASK,CHANNEL_MASK,LEAF_MASK), (1<<64)-1)
        self.assertEqual(decode((1<<64)-1),(SHELL_MASK,CHANNEL_MASK,LEAF_MASK))
    def test_boundary_probes(self):
        for s in (0,1,1023,2047):
            for c in (0,1,32767,65535):
                for i in (0,1,1<<36,LEAF_MASK):
                    self.assertEqual(decode(encode(s,c,i)),(s,c,i))
    def test_random_exact_roundtrips(self):
        rng=random.Random(20261112)
        for _ in range(20000):
            s=rng.randrange(1<<11);c=rng.randrange(1<<16);i=rng.randrange(1<<37)
            self.assertEqual(decode(encode(s,c,i)),(s,c,i))
    def test_out_of_range(self):
        for tup in [(-1,0,0),(2048,0,0),(0,65536,0),(0,0,1<<37)]:
            with self.assertRaises(ValueError): encode(*tup)
    def test_ball_cube_fraction(self):
        f=1-math.pi/6
        from_formula=1-math.pi**(3/2)/(8*math.gamma(3/2+1))
        self.assertAlmostEqual(f,from_formula,places=13)
    def test_sphere_sagitta(self):
        R=1.0; rho=.001
        h=R-math.sqrt(R*R-rho*rho)
        self.assertAlmostEqual(h,rho*rho/(2*R),delta=1e-12)

if __name__=="__main__":
    unittest.main()
