
import unittest
from athena_3dviz import utils
import numpy as np

class TestUtils(unittest.TestCase):

    def test_switch_phi_r(self):
        v_in = np.arange(2*3*4*5).reshape((2,3,4,5))
        v_in[0,1,2,3] = 9
        v_out = utils.switch_phi_r(v_in)
        for ib in range(2):
            for iphi in range(3):
                for itheta in range(4):
                    for ir in range(5):
                        self.assertEqual(v_out[ib, ir, itheta, iphi], v_in[ib, iphi, itheta, ir])
        self.assertEqual(v_out[0,3,2,1], 9)
