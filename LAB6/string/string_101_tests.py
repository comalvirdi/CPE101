# Lab 6
# 
# Name: Comal Virdi
# Instructor: S. Einakian
# Section: 01

import unittest
from string_101 import *

class TestString(unittest.TestCase):
	def test_str_rot_13(self):
		self.assertEqual(str_rot_13("abcde"), "nopqr")
		self.assertEqual(str_rot_13("ace"), "npr")
		self.assertEqual(str_rot_13("comal"), "pbzny")
	def test_str_translate_101(self):
		self.assertEqual(str_translate_101("abcdcba", "a","x" ), "xbcdcbx")
		self.assertEqual(str_translate_101("abcdcba", "b","y" ), "aycdcya")
		self.assertEqual(str_translate_101("abcdcba", "i","x" ), "abcdcba")

if __name__ == '__main__':
   unittest.main()

