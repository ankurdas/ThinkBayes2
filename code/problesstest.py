import unittest
import thinkstats2

class Test(unittest.TestCase):

    def testPmfProbLess(self):
        d6 = thinkstats2.Pmf(range(1,7))
        self.assertEqual(d6.ProbLess(4), 0.5)
        self.assertEqual(d6.ProbGreater(3), 0.5)
        two = d6 + d6
        three = two + d6
        self.assertAlmostEqual(two > three, 0.15200617)
        self.assertAlmostEqual(two < three, 0.77854938)
        self.assertAlmostEqual(
            two.ProbGreater(three), 0.152006)
        self.assertAlmostEqual(
            two.ProbLess(three), 0.778549)
