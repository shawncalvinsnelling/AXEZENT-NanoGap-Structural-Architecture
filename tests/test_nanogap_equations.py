"""Independent standard-library regression tests for documented NanoGap equations."""
import math
import unittest

H = 31.75
ENDPOINTS = [(sx * 0.72*H, sy*0.72*H, sz*0.72*H)
             for sx,sy,sz in [(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)]]

def pitch(r): return 14.0 - 6.0*r**1.35
def threshold(r): return 0.27 + 0.21*r**1.60
def coupling(d): return math.exp(-0.22*d)
def phase_period(r): return pitch(r)**2/(14.0+2.1*r**1.35)
def segment_distance(q,v):
    v2=sum(t*t for t in v)
    t=max(0.0,min(1.0,sum(a*b for a,b in zip(q,v))/v2))
    return math.sqrt(sum((a-t*b)**2 for a,b in zip(q,v)))
def support_distance(q): return min(segment_distance(q,v) for v in ENDPOINTS)

class NanoGapEquations(unittest.TestCase):
    def test_nominal_ranges(self):
        self.assertAlmostEqual(pitch(0),14.0)
        self.assertAlmostEqual(pitch(1),8.0)
        self.assertAlmostEqual(threshold(0),0.27)
        self.assertAlmostEqual(threshold(1),0.48)
        for i in range(101):
            r=i/100
            self.assertLessEqual(8.0,pitch(r))
            self.assertLessEqual(pitch(r),14.0)
            self.assertLessEqual(.27,threshold(r))
            self.assertLessEqual(threshold(r),.48)
    def test_tetrahedral_support_distance(self):
        self.assertAlmostEqual(support_distance((0,0,0)),0)
        self.assertAlmostEqual(support_distance(ENDPOINTS[0]),0)
        self.assertAlmostEqual(support_distance(tuple(x/2 for x in ENDPOINTS[1])),0)
    def test_coupling_decay(self):
        self.assertAlmostEqual(coupling(0),1)
        self.assertAlmostEqual(coupling(math.log(2)/.22),.5)
        self.assertAlmostEqual(coupling(math.log(10)/.22),.1)
        self.assertLess(coupling(10),coupling(5))
    def test_effective_threshold(self):
        for r in (0,.25,.5,.75,1):
            for d in (0,1,5,10,20,50):
                effective=threshold(r)+.080*coupling(d)
                self.assertGreater(effective,threshold(r))
                self.assertLessEqual(effective,threshold(r)+.080+1e-14)
    def test_x_ray_phase_derivative(self):
        r=.8
        x=r*H
        h=1.e-4
        def phi(xx): return 2*math.pi*xx/pitch(xx/H)
        numeric=(phi(x+h)-phi(x-h))/(2*h)
        theory=2*math.pi/phase_period(r)
        self.assertAlmostEqual(numeric,theory,places=7)
        self.assertAlmostEqual(phase_period(1),64/16.1,places=12)

if __name__ == "__main__":
    unittest.main()
