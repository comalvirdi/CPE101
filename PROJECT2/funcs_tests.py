# Project 2 - Moonlander Functions
# Author: Comal Virdi
# Instructor: S. Einakian
# Section: 01

#at least 3 test cases for each function
import unittest
from landerFuncs import *

class TestCases(unittest.TestCase):
   #first test for updateAcceleration
   def test_updateAcceleration_1(self):

      self.assertAlmostEqual(updateAcceleration(1.62,0), -1.62)
      self.assertAlmostEqual(updateAcceleration(9.8,3), -3.92) 
      self.assertAlmostEqual(updateAcceleration(1.62,5), 0) 
      self.assertAlmostEqual(updateAcceleration(9.8,7), 3.92) 
      self.assertAlmostEqual(updateAcceleration(1.62,9), 1.296) 

   #first test for updateAltitude
   def test_updateAltitude(self):
   	  self.assertAlmostEqual(updateAltitude(0.00, 5.00, 5.00), 0)
   	  self.assertAlmostEqual(updateAltitude(-1.00, 5.00, 5.00), 0)
   	  self.assertAlmostEqual(updateAltitude(1034.28, -54.33, 4.00), 981.95)
   	  self.assertAlmostEqual(updateAltitude(25.15, -25.33, 72.00 ), 35.82)
   	  self.assertAlmostEqual(updateAltitude(200.34, -10.32, -31.20 ), 174.42)

   #first test for updateVelocity
   def test_updateVelocity(self):
   	  self.assertAlmostEqual(updateVelocity(-53.45, 43.00), -10.45)
   	  self.assertAlmostEqual(updateVelocity(-23.33, 400.21), 376.88)
   	  self.assertAlmostEqual(updateVelocity(-3.4, 21.15), 17.75)
   	  self.assertAlmostEqual(updateVelocity(53.45, 13.13), 66.58)

   def test_updateFuel(self):
   	  self.assertAlmostEqual(updateFuel(400,0), 400)
   	  self.assertAlmostEqual(updateFuel(1300, 3), 1297)
   	  self.assertAlmostEqual(updateFuel(500,5), 495)
   	  self.assertAlmostEqual(updateFuel(9,7), 2)
   	  self.assertAlmostEqual(updateFuel(15, 9), 6)

      

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

