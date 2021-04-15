# File: levelingTest.py
# Author: Danielle Dishop
# Description: This file contains testing code for Leveling.py, using the unittest framework

import unittest
from random import randrange

from ..src.Leveling import LEVEL_BREAKPOINTS, CalcLevel

class TestLeveling(unittest.TestCase):

    # Tests that CalcLevel returns the right level
    def test_calc_level(self):
        # Define an array of random exp values, each corresponding to a different level
        exp = []
        for i in range(1,20):
            exp.append(randrange(LEVEL_BREAKPOINTS.get(i),LEVEL_BREAKPOINTS.get(i+1)))
        exp.append(randrange(LEVEL_BREAKPOINTS.get(20),500000))

        #Check that each Level is correct
        Flag = True
        for i in range(len(exp)):
            level = CalcLevel(exp[i])
            if level != i + 1:
                print(level, " found, ", i + 1, " expected")
                Flag = False

        self.assertTrue(Flag)