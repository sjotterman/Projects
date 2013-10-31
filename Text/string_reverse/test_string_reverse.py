#! /usr/bin/python
#test_string_reverse.py

from __future__ import absolute_import
import unittest
from . import string_reverse

class Test_string_reverse(unittest.TestCase):
    def test_reverse_sam(self):
        self.assertEqual(string_reverse.reverse("sam"),"mas")

    def test_reverse_allie(self):
        self.assertEqual(string_reverse.reverse("allie"), "eilla")

    def test_reverse_allie(self):
        self.assertEqual(string_reverse.reverse("allie"), "eilla")

    def test_reverse_scout(self):
        self.assertEqual(string_reverse.reverse("scout"), "tuocs")

    def test_reverse_beer(self):
        self.assertEqual(string_reverse.reverse("beer"), "reeb")

    def test_reverse_otterman(self):
        self.assertEqual(string_reverse.reverse("otterman"), "namretto")

    def test_reverse_semper_fidelis(self):
        self.assertEqual(string_reverse.reverse("Semper Fidelis"), "silediF repmeS")

if __name__ == "__main__":
       unittest.main()
