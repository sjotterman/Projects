#! /usr/bin/python3
#testfact.py
from __future__ import absolute_import
import unittest
from . import factorial

class TestFact(unittest.TestCase):
    def test_fact_rec_0(self):
        self.assertEqual(factorial.fact_rec(0), 1)

    def test_fact_rec_1(self):
        self.assertEqual(factorial.fact_rec(1), 1)

if __name__ == "__main__":
       unittest.main()
