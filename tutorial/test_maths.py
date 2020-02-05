import unittest
import tutorial
import math


class MathsTestCase(unittest.TestCase):

    def test_subtract(self):
        self.assertEqual(5, tutorial.subtract(10, 5))

    def test_subtract_zero(self):
        self.assertEqual(1, tutorial.subtract(0, 0))

