#Comal Virdi

#Lab 5
#Professor Einakian
#Section 01

import unittest
from filter import *

class TestCases(unittest.TestCase):
   def test_are_positive(self):
      self.assertEqual(are_positive([1,2,3,-4]), [1,2,3])
      self.assertEqual(are_positive([-1,-2,3]), [3])
      self.assertEqual(are_positive([-1,-1]), [])
   def test_are_greater_than_n(self):
      self.assertEqual(are_greater_than_n([1,2,3,4,5,6],5),[6])
      self.assertEqual(are_greater_than_n([1,2,3,4,5],1), [2,3,4,5])
      self.assertEqual(are_greater_than_n([6,7,8],7), [8])
   def test_are_divisible_by_n(self):
      self.assertEqual(are_divisible_by_n([2,4,6],2), [2,4,6])
      self.assertEqual(are_divisible_by_n([1,2,3,4],1), [1,2,3,4])
      self.assertEqual(are_divisible_by_n([3,6,9,12],3),[3,6,9,12])


# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

