# test_word_count.py

from __future__ import absolute_import
import unittest
from . import word_count
    
class Test_word_count(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(word_count.my_count(""), 0)
        
if __name__ == "__main__":
    unittest.main()