# LAB 3 

# Name: Comal Virdi
# Instructor: S. Einakian
# Section: 01

import unittest
from logic import *


class TestCases(unittest.TestCase):

   def test_is_even(self):
      self.assertTrue(is_even(4))
      self.assertTrue(is_even(0))
      self.assertTrue(is_even(2))
      self.assertTrue(is_even(109477532))
      self.assertTrue(is_even(486))
      self.assertFalse(is_even(39))
      self.assertFalse(is_even(27))
      self.assertFalse(is_even(111867))
      self.assertFalse(is_even(1))

   def test_in_an_interval(self):
      self.assertFalse(in_an_interval(10))
      self.assertFalse(in_an_interval(9))
      self.assertTrue(in_an_interval(20))
      self.assertTrue(in_an_interval(0))
      self.assertTrue(in_an_interval(122))
      self.assertTrue(in_an_interval(127))



#-10, 0, 9, 20, 122, 127.
# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

