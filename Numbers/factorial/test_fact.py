#! /usr/bin/python3
#testfact.py

import unittest
from factorial import fact_recto

class TestFib(unittest.TestCase):
    def test_fact_rec_0(self):
        self.assertEqual(fact_rec(0), 1)

if __name__ == "__main__":
       unittest.main()
