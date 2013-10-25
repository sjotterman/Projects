#! /usr/bin/python3
#test_pi_digit.py

from __future__ import absolute_import
import unittest
from . import pi_digit

class Test_pi_digit(unittest.TestCase):
    def test_pi_digit_1(self):
        self.assertEqual(pi_digit.pi_digit(1), 3)

    def test_pi_digit_2(self):
        self.assertEqual(pi_digit.pi_digit(2), 1)

    def test_pi_digit_3(self):
        self.assertEqual(pi_digit.pi_digit(3), 4)

    def test_pi_digit_4(self):
        self.assertEqual(pi_digit.pi_digit(4), 1)

    def test_pi_digit_5(self):
        self.assertEqual(pi_digit.pi_digit(5), 5)

    def test_pi_digit_6(self):
        self.assertEqual(pi_digit.pi_digit(6), 9)

    def test_pi_digit_15(self):
        self.assertEqual(pi_digit.pi_digit(15), 9)

if __name__ == "__main__":
   unittest.main()
