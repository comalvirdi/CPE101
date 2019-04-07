# Project 1 

# Name: Comal Virdi
# Instructor: S. Einakian
# Section: 01

import unittest
from funcs import *

class TestCases(unittest.TestCase):
          
   def test_poundsToKG1(self):

   		self.assertAlmostEqual(poundsToKG(10), 4.53592)
   		self.assertAlmostEqual(poundsToKG(7), 3.175144)


   def test_getMassObject(self):

   		self.assertAlmostEqual(getMassObject("t"), 0.1)
   		self.assertAlmostEqual(getMassObject("p"), 1.0)
   		self.assertAlmostEqual(getMassObject("r"), 3.0)
   		self.assertAlmostEqual(getMassObject("g"), 5.3)
   		self.assertAlmostEqual(getMassObject("l"), 9.07)
   		self.assertAlmostEqual(getMassObject(""), 0.0)


   def test_getVelocityObject(self):

    	self.assertAlmostEqual(getVelocityObject(0), 0)
    	self.assertAlmostEqual(getVelocityObject(170), 28.861739379323627)
    	self.assertAlmostEqual(getVelocityObject(15.9), 8.826664149)


   def test_getVelocitySkater(self):
    	
    	self.assertAlmostEqual(getVelocitySkater(5, 0.1, 28.861), .57722)
    	self.assertAlmostEqual(getVelocitySkater(70, 1.0, 8.82), .126)
    	self.assertAlmostEqual(getVelocitySkater(105, 3.0, 28.861), .8246)
    	self.assertAlmostEqual(getVelocitySkater(5,5.3, 8.82), 9.3492)
    	self.assertAlmostEqual(getVelocitySkater(70, 9.07, 28.861), 3.739561)
    	self.assertAlmostEqual(getVelocitySkater(105, 0.0, 8.82), 0.0)

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

