# Lab 7
# 
# Name: Comal Virdi 
# Instructor: S. Einakian
# Section: 01

import unittest
from groups import *

class TestString(unittest.TestCase):
	def test_groups_of_3(self):
		self.assertEqual(groups_of_3([1,2,3,4,5,6,7,8,9]), [[1,2,3], [4,5,6], [7,8,9]])
		self.assertEqual(groups_of_3([1,2,3,4,5,6,7,8]), [[1,2,3], [4,5,6], [7,8]])

if __name__ == '__main__':
   unittest.main()

