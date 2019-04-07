#Comal Virdi

#Lab 5
#Professor Einakian
#Section 01
import unittest
from map import *

class TestCases(unittest.TestCase):
	def test_square_all(self):
		self.assertEqual(square_all([2,3,4,5]),[4,9,16,25])
		self.assertEqual(square_all([4,-6,8,22,3,5]),[16,36,64,484,9,25])
		self.assertEqual(square_all([1,3,5,7,8,9,11]),[1,9,25,49,64,81,121])

	def test_add_n_all(self):
		self.assertEqual(add_n_all([2,3,4,5],10),[12,13,14,15])
		self.assertEqual(add_n_all([1,-5,3], -2),[-1, -7, 1])
		self.assertEqual(add_n_all([2,3, 70, 5], 1),[3, 4, 71, 6])

	def test_even_or_odd_all(self):
		self.assertEqual(even_or_odd_all([2,3,4,5,6,20]), [True, False, True, False, True, True])
		self.assertEqual(even_or_odd_all([2,4,6,8,10]), [True,True,True, True, True])
		self.assertEqual(even_or_odd_all([1,3,5]), [ False,False,False])


# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

