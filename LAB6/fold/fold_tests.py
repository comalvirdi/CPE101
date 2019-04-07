# Lab 6
# 
# Name: Comal Virdi
# Instructor: S. Einakian
# Section: 01

import unittest
from fold import *

class TestCases(unittest.TestCase):
	def test_sum(self):
		self.assertEqual(sum([1,2,3,4,5]), 15)
		self.assertEqual(sum([1.2,3,4.3,10]),18.5)
		self.assertEqual(sum([[1,2,3],[1,2]]), 9)

	def test_index_of_smallest(self):
		self.assertEqual(index_of_smallest([1,2,3,4]),0)
		self.assertEqual(index_of_smallest([1,2,3,0,-1]), 4)
		self.assertEqual(index_of_smallest([[1,2,3], [0,-1]]), 1)
		self.assertEqual(index_of_smallest([]), -1)



# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

