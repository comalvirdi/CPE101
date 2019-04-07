import unittest
from objects import *

class TestCases(unittest.TestCase):
   def test_equality(self):
      p0 = Point(-7,11)
      p1 = Point(1.000001,2)
      p2 = Point(1,2)
      p3 = Point(2,-1)
      p4 = Point(-2,2)
      self.assertEqual(p1,p2)
      self.assertNotEqual(p1,p3)
# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

