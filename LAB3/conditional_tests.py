# LAB 3 

# Name: Comal Virdi
# Instructor: S. Einakian
# Section: 01

import unittest
from conditional import *

class TestCases(unittest.TestCase):
   def test_max_101(self):
      self.assertEqual(max_101(5,7), 7)
      self.assertEqual(max_101(9,7), 9)
      self.assertEqual(max_101(1,1.09), 1.09)
      self.assertEqual(max_101(7005,1), 7005)
      self.assertEqual(max_101(53,7), 53)

   def test_max_of_three(self):
   	  self.assertEqual(max_of_three(5,8,9),9)
   	  self.assertEqual(max_of_three(5,8.01,8),8.01)
   	  self.assertEqual(max_of_three(6,1,2),6)

   def test_rental_late_fee(self):
   	  self.assertEqual(rental_late_fee(17), 19)
   	  self.assertEqual(rental_late_fee(0), 0)
   	  self.assertEqual(rental_late_fee(3), 5)
   	  self.assertEqual(rental_late_fee(9), 7)
   	  self.assertEqual(rental_late_fee(18), 19)
   	  self.assertEqual(rental_late_fee(100), 100)

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

