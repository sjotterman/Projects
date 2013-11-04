#! /usr/bin/python
#test_palindrome.py

from __future__ import absolute_import
import unittest
from . import palindrome

class Test_palindrome(unittest.TestCase):
    def test_is_palindrome_bob(self):
        self.assertEqual(palindrome.is_palindrome("bob"), True)

    def test_is_palindrome_sam(self):
        self.assertEqual(palindrome.is_palindrome("sam"), False)

    def test_is_palindrome_racecar(self):
        self.assertEqual(palindrome.is_palindrome("racecar"), True)
if __name__ == "__main__":
       unittest.main()
