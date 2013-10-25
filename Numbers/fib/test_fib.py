#! /usr/bin/python3
#testfib.py


from __future__ import absolute_import
import unittest
from . import fib

class TestFib(unittest.TestCase):
    def test_fib_0(self):
        self.assertEqual(fib.fib(0), 0)

    def test_fib_1(self):
        self.assertEqual(fib.fib(1), 1)

    def test_fib_2(self):
        self.assertEqual(fib.fib(2), 1)

    def test_fib_range(self):
        for x in range(2,13):
            self.assertEqual(fib.fib(x), fib.fib(x - 1) + fib.fib(x - 2))

if __name__ == "__main__":
       unittest.main()
