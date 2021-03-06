# Project 4
# 
# Name: Comal Virdi and Mary McCafferty
# Instructor: S. Einakian
# Section: 01



import unittest
from func_calcudoku import *

class TestCases(unittest.TestCase):

	def test_validateCages(self):
		self.assertTrue(validateCages( [[1, 2, 3, 4, 5], [2, 4, 1, 5, 3], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]] , [[3, 0, 1], [14, 2, 3, 8, 13], [8, 4, 9], [7, 5, 10], [5, 6, 7], [9, 11, 16], [1, 12], [2, 14], [14, 15, 20, 21, 22], [12, 17, 18, 19, 23, 24]] ))
		self.assertTrue(validateCages([[1, 4, 2, 5, 3],[2, 5, 4, 3, 1],[5, 2, 3, 1, 4],[4, 3, 1, 2, 5],[3, 1, 5, 4, 2]],[[7, 0, 1, 2], [12, 3, 4, 8, 9], [17, 5, 7, 10, 11, 12, 13], [5, 6], [11, 14, 19, 24],[7, 15, 20],[5, 16, 17, 21], [11, 18, 22, 23]]))
		self.assertTrue(validateCages([[3, 5, 2, 1, 4], [5, 1, 3, 4, 2], [2, 4, 1, 5, 3], [1, 2, 4, 3, 5], [4, 3, 5, 2, 1]],[[9, 0, 5, 6], [7, 1, 2], [10, 3, 8, 13], [14, 4, 9, 14, 19], [3, 7], [8, 10, 11, 16], [13, 12, 17, 21, 22], [5, 15, 20], [6, 18, 23, 24]]))
	
	def test_validateRows(self):
		self.assertTrue(validateRows([[1,2,3,4,5], [1,2,3,4,5],[1,2,3,4,5]]))
		self.assertFalse(validateRows([[1,2,2,3,4], [1,2,4,4,5], [1,2,3,4,5]]))
		self.assertTrue(validateRows([[3, 5, 2, 1, 4], [5, 1, 3, 4, 2], [2, 4, 1, 5, 3], [1, 2, 4, 3, 5], [4, 3, 5, 2, 1]]))
	
	def test_validateAll(self):
		
		self.assertTrue(validateAll([[3, 5, 2, 1, 4], [5, 1, 3, 4, 2], [2, 4, 1, 5, 3], [1, 2, 4, 3, 5], [4, 3, 5, 2, 1]],[[9, 0, 5, 6], [7, 1, 2], [10, 3, 8, 13], [14, 4, 9, 14, 19], [3, 7], [8, 10, 11, 16], [13, 12, 17, 21, 22], [5, 15, 20], [6, 18, 23, 24]]))
		self.assertTrue(validateAll([[1,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0],], [[9, 0, 5, 6], [7, 1, 2], [10, 3, 8, 13], [14, 4, 9, 14, 19], [3, 7], [8, 10, 11, 16], [13, 12, 17, 21, 22], [5, 15, 20], [6, 18, 23, 24]]))
		self.assertFalse(validateAll([[1,1,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0],], [[9, 0, 5, 6], [7, 1, 2], [10, 3, 8, 13], [14, 4, 9, 14, 19], [3, 7], [8, 10, 11, 16], [13, 12, 17, 21, 22], [5, 15, 20], [6, 18, 23, 24]]))
		self.assertFalse(validateAll([[1,0,0,0,0], [1,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0],], [[9, 0, 5, 6], [7, 1, 2], [10, 3, 8, 13], [14, 4, 9, 14, 19], [3, 7], [8, 10, 11, 16], [13, 12, 17, 21, 22], [5, 15, 20], [6, 18, 23, 24]]))

	def test_transpose(self):
		self.assertEqual(transpose([[3, 5, 2, 1, 4], [5, 1, 3, 4, 2], [2, 4, 1, 5, 3], [1, 2, 4, 3, 5], [4, 3, 5, 2, 1]]),[[3, 5, 2, 1, 4], [5, 1, 4, 2, 3], [2, 3, 1, 4, 5], [1, 4, 5, 3, 2], [4, 2, 3, 5, 1]])
		self.assertEqual(transpose([[1, 2, 3, 4, 5], [3, 1, 4, 5, 2], [2, 5, 1, 3, 4], [5, 4, 2, 1, 3], [4, 3, 5, 2, 1]]), [[1, 3, 2, 5, 4], [2, 1, 5, 4, 3], [3, 4, 1, 2, 5], [4, 5, 3, 1, 2], [5, 2, 4, 3, 1]])
		self.assertEqual(transpose([[1, 4, 2, 5, 3], [2, 5, 4, 3, 1], [5, 2, 3, 1, 4], [4, 3, 1, 2, 5], [3, 1, 5, 4, 2]]), [[1, 2, 5, 4, 3], [4, 5, 2, 3, 1], [2, 4, 3, 1, 5], [5, 3, 1, 2, 4], [3, 1, 4, 5, 2]])

if __name__ == '__main__':
	unittest.main()