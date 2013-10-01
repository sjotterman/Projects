#! /usr/bin/python3
#test_pi_digit.py

import unittest
from pi_digit import pi_digit

class Test_pi_digit(unittest.TestCase):
	def test_pi_digit_1(self):
		self.assertEqual(pi_digit(1), 3)

	def test_pit_digit_2(self):
		self.assertEqual(pi_digit(2), 1)

if __name__ == "__main__":
   unittest.main()
