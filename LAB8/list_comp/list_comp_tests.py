# LAB 8
# COMAL VIRDI
# EINAKIAN
# SECTION 01

import unittest
from list_comp import *
from objects import *

class TestCases(unittest.TestCase):
	def test_distance(self):
		p0 = Point(-7,11)
		p1 = Point(1,2)
		p2 = Point(1,2)
		p3 = Point(2,-1)
		p4 = Point(-2,2)
		p5 = Point(5,6)
		l = [p0,p1,p4]
		l2 =[p5,p3,p2]
		l3 = [Point(0,0), Point(0,0), Point(0,0)]
		self.assertEqual(distance_all(l), [13.038404810405298, 2.23606797749979, 2.8284271247461903])
		self.assertEqual(distance_all(l2), [7.810249675906654,2.23606797749979,2.23606797749979])
		self.assertEqual(distance_all(l3),[0,0,0])

	def test_are_in_first_quadrant(self):
		p0 = Point(-7,11)
		p1 = Point(1,2)
		p2 = Point(1,2)
		p3 = Point(2,-1)
		p4 = Point(-2,2)
		p5 = Point(5,6)
		l = [p0,p1,p4]
		l2 =[p5,p3,p2]
		self.assertEqual(are_in_first_quadrant(l),[Point(1,2)])
		self.assertEqual(are_in_first_quadrant(l2), [Point(5,6), Point(1,2)])
		self.assertEqual(are_in_first_quadrant([Point(1,2), Point(3,2),Point(1,-1)]),[Point(1,2), Point(3,2)])
# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

