#! /usr/bin/python3
#testfib.py

import unittest
from fib import fib

class TestFib(unittest.TestCase):
    def test_fib_0(self):
        self.assertEqual(fib(0), 0)

    def test_fib_1(self):
        self.assertEqual(fib(1), 1)

    def test_fib_2(self):
        self.assertEqual(fib(2), 1)

if __name__ == "__main__":
       unittest.main()
