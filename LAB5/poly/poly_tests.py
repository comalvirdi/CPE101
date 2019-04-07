import unittest
from poly import  *

class TestPoly(unittest.TestCase):
   #do not delete this part use this to comapre two list
	def assertListAlmostEqual(self, l1, l2):
		self.assertEqual(len(l1), len(l2))
		for el1, el2 in zip(l1, l2):
			self.assertAlmostEqual(el1, el2)


   # Add tests here

	def test_poly_add2(self):
		poly1 = [2.3, 4.7, 1.0]
		poly2 = [1.2, 2.1, -3.2]
		poly3 = poly_add2(poly1, poly2)
		self.assertListAlmostEqual(poly3, [3.5,6.8,-2.2])

		p1 = [6.9, 4.3, 1.4]
		p2 = [1.7, 2.9, -6.4]
		p3 = poly_add2(p1, p2)
		self.assertListAlmostEqual(p3, [8.6,7.2,-5.0])
	
	def test_poly_mult2(self):
		poly1 = [2,5,2]
		poly2 = [2,5,2]
		poly3 = poly_mult2(poly1,poly2)
		self.assertListAlmostEqual(poly3, [4, 20, 33, 20, 4])

		p1 = [3,2,1]
		p2 = [3,2,1]
		p3 = poly_mult2(p1,p2)
		self.assertListAlmostEqual(p3, [9, 12, 10, 4, 1])
if __name__ == '__main__':
	unittest.main()
