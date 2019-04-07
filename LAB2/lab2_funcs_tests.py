#Lab 2 Test Cases
#Name:comal virdi
#Section:01
##############################################################
import unittest
import funcs

class TestCases(unittest.TestCase):
   def test_math_func1(self):
      self.assertAlmostEqual(funcs.math_func1(1,1), 0.16666666666666666)
      self.assertAlmostEqual(funcs.math_func1(0,1), 0.142857143)

   def test_math_func2(self):
      self.assertAlmostEqual(funcs.math_func2(1,4,-21), 3) 
      self.assertAlmostEqual(funcs.math_func2(1,4,1), -0.2679491924311228)

   def test_d(self):
      self.assertAlmostEqual(funcs.d(2,-1,-2,2), 5)
      self.assertAlmostEqual(funcs.d(5,5,1,2), 5)

   def test_is_negative(self):
      self.assertTrue(funcs.is_negative(-5))
      self.assertFalse(funcs.is_negative(5))

   def test_dividable_by_5(self):
      self.assertTrue(funcs.dividable_by_5(10))
      self.assertFalse(funcs.dividable_by_5(8))

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

