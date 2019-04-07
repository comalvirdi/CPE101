# Lab 6
# 
# Name: Comal Virdi
# Instructor: S. Einakian
# Section: 01

import unittest
from char import *

class TestChar(unittest.TestCase):
	def test_lower(self):
		self.assertEqual(is_lower_101("a"), True)
		self.assertEqual(is_lower_101("Z"), False)
		self.assertEqual(is_lower_101("2"), False)
	def test_char_rot13(self):
		self.assertEqual(char_rot13('a'), "n")
		self.assertEqual(char_rot13('X'), "K")
		self.assertEqual(char_rot13('1'), "1")

if __name__ == '__main__':
   unittest.main()

