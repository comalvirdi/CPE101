# LAB 8
# COMAL VIRDI
# EINAKIAN
# SECTION 01

import unittest
from objects import *
from funcs_objects import *

class TestCases(unittest.TestCase):
   def test_point(self):
      p0 = Point(-7,11)
      p1 = Point(1,2)
      p2 = Point(1,2)
      p3 = Point(2,-1)
      p4 = Point(-2,2)
      p5 = Point(5,6)
      self.assertEqual(p1.x, 1)
      self.assertEqual(p1.y, 2)
      self.assertEqual(distance(p1,p2), 0)
      self.assertEqual(distance(p3,p4), 5)
      self.assertEqual(distance(p5,p0), 13)

   def test_circle(self):
      c1 = Circle(Point(2,3), 5)
      c2 = Circle(Point(2,3), 5)
      c3 = Circle(Point(10,10), 1)
      c4 = Circle(Point(5,5), 20)
      self.assertEqual(c1.center.x, 2)
      self.assertEqual(c1.center.y, 3)
      self.assertEqual(c1.radius, 5)
      self.assertTrue(circles_overlap(c1,c2))
      self.assertFalse(circles_overlap(c3,c2))
      self.assertTrue(circles_overlap(c3,c4))


# Run the unit tests.
if __name__ == '__main__':
   unittest.main()
