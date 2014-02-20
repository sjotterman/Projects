#! /usr/bin/python
#test_caesar.py

from __future__ import absolute_import
import unittest
from . import caesar

class Test_caesar(unittest.TestCase):
    def test_shift_a_1(self):
        self.assertEqual(caesar.shift("a", 1), "b")

    def test_shift_b_1(self):
        self.assertEqual(caesar.shift("b", 1), "c")

    def test_shift_c_1(self):
        self.assertEqual(caesar.shift("c", 1), "d")

    def test_shift_d_1(self):
        self.assertEqual(caesar.shift("d", 1), "e")

    def test_shift_A_1(self):
        self.assertEqual(caesar.shift("A", 1), "B")

    def test_shift_d_1(self):
        self.assertEqual(caesar.shift("d", 1), "e")

    def test_shift_z_1(self):
        self.assertEqual(caesar.shift("z", 1), "a")

    def test_shift_Z_1(self):
        self.assertEqual(caesar.shift("Z", 1), "A")

    def test_shift_a_1(self):
        self.assertEqual(caesar.shift("a", 2), "c")

    def test_shift_b_1(self):
        self.assertEqual(caesar.shift("b", 2), "d")

    def test_shift_c_1(self):
        self.assertEqual(caesar.shift("c", 2), "e")

    def test_shift_d_1(self):
        self.assertEqual(caesar.shift("d", 2), "f")

    def test_shift_A_1(self):
        self.assertEqual(caesar.shift("A", 2), "C")

    def test_shift_d_1(self):
        self.assertEqual(caesar.shift("d", 2), "f")

    def test_shift_z_1(self):
        self.assertEqual(caesar.shift("z", 2), "b")

    def test_shift_Z_1(self):
        self.assertEqual(caesar.shift("Z", 2), "B")

    def test_shift_a_5(self):
        self.assertEqual(caesar.shift("a", 5), "f")

    def test_shift_G_10(self):
        self.assertEqual(caesar.shift("G", 10), "Q")

    def test_shift_Z_25(self):
        self.assertEqual(caesar.shift("Z", 25), "Y")

    def test_shift_a_52(self):
        self.assertEqual(caesar.shift("a", 52), "a")

    def test_shift_A_52(self):
        self.assertEqual(caesar.shift("A", 52), "A")

    def test_shift_HAL_1(self):
        self.assertEqual(caesar.shift("HAL", 1),"IBM")

    def test_shift_Sam_1(self):
        self.assertEqual(caesar.shift("Sam", 1),"Tbn")

    def test_shift_a_neg1(self):
        self.assertEqual(caesar.shift("a", -1), "z")

    def test_shift_a_neg27(self):
        self.assertEqual(caesar.shift("a", -27), "z")

    def test_shift_A_neg27(self):
        self.assertEqual(caesar.shift("A", -27), "Z")

    def test_shift_A_1point3(self):
        self.assertEqual(caesar.shift("A", 1.3), "B")

    def test_shift_a_1point3(self):
        self.assertEqual(caesar.shift("a", 1.3), "b")

    def test_shift_Sam_string1(self):
        self.assertEqual(caesar.shift("Sam", "1"),"Tbn")

    def test_shift_hello_world(self):
        self.assertEqual(caesar.shift("Hello, World!", "1"),"Ifmmp, Xpsme!")

    def test_shift_punctuation(self):
        self.assertEqual(caesar.shift("!@#$%^&*()", "1"),"!@#$%^&*()")

    def test_shift_numbers(self):
        self.assertEqual(caesar.shift("123", "1"),"123")

if __name__ == "__main__":
       unittest.main()
