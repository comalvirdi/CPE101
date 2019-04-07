import unittest
from crime import *


ob1 = Crime(1, 'ROBBERY')
ob2 = Crime(2, 'ROBBERY')
ob3 = Crime(3, 'ROBBERY')
ob4 = Crime(4, 'ROBBERY')
ob5 = Crime(5, 'ROBBERY')
class TestCases(unittest.TestCase):
          
    def test_createCrimes(self):
   		pass

    def test_sort(self):
    	
    	self.assertEqual(sort_crimes([ob1, ob2]), [ob1,ob2])
    	self.assertEqual(sort_crimes([ob2, ob3,ob4, ob1]), [ob1, ob2, ob3, ob4])
    	self.assertEqual(sort_crimes([ob3, ob5]), [ob3,ob5])
    
    def test_update_crimes(self):
    	l = ['1\tTuesday\t01/06/2015\t16:53\n', '2\tSaturday\t01/03/2015\t14:06\n', '4\tTuesday\t01/06/2015\t13:00\n', '3\tWednesday\t01/07/2015\t17:30\n']

    	self.assertEqual(update_crimes([ob1,ob2,ob3,ob4], l), [])


if __name__ == '__main__':
   unittest.main()
