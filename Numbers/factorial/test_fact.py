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

    def test_fact_rec_2(self):
        self.assertEqual(factorial.fact_rec(2), 2)

    def test_fact_rec_12(self):
        self.assertEqual(factorial.fact_rec(12), 479001600)

    def test_fact_rec_neg1(self):
        self.assertEqual(factorial.fact_rec(-1), 0)

    def test_fact_it_neg1(self):
        self.assertEqual(factorial.fact_it(-1), 0)

    def test_fact_it_0(self):
        self.assertEqual(factorial.fact_it(0), 1)

    def test_fact_it_1(self):
        self.assertEqual(factorial.fact_it(1), 1)

    def test_fact_it_2(self):
        self.assertEqual(factorial.fact_it(2), 2)

    def test_fact_it_12(self):
        self.assertEqual(factorial.fact_it(12), 479001600)

if __name__ == "__main__":
       unittest.main()
