#! /usr/bin/python
#test_caesar.py

from __future__ import absolute_import
import unittest
from . import caesar

class Test_caesar(unittest.TestCase):
    def test_shift_a_1(self):
        self.assertEqual(caesar.shift("a", 1), "b")

    def test_shift_b_1(self):
        self.assertEqual(caesar.shift("b", 2), "c")

if __name__ == "__main__":
       unittest.main()
