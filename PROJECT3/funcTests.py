# Project 3
# 
# Name: Comal Virdi and Mary McCafferty
# Instructor: S. Einakian
# Section: 01



import unittest
from funcs import *

class TestCases(unittest.TestCase):

	def test_reverseList(self):
		self.assertEqual(reverseList(["A11111111B","A11111111B","A11111111B","A11111111B","A11111111B","A11111111B","A11111111B","A11111111B","A11111111B","A11111111B"]),["B11111111A","B11111111A","B11111111A","B11111111A","B11111111A","B11111111A","B11111111A","B11111111A","B11111111A","B11111111A"])
		self.assertEqual(reverseList(["ABCDEFGHIJ","ABCDEFGHIJ","ABCDEFGHIJ","ABCDEFGHIJ","ABCDEFGHIJ","ABCDEFGHIJ","ABCDEFGHIJ","ABCDEFGHIJ","ABCDEFGHIJ","ABCDEFGHIJ"]),["JIHGFEDCBA","JIHGFEDCBA","JIHGFEDCBA","JIHGFEDCBA","JIHGFEDCBA","JIHGFEDCBA","JIHGFEDCBA","JIHGFEDCBA","JIHGFEDCBA","JIHGFEDCBA"])
	
	def test_listDownward(self):
		self.assertEqual(listDownward(["ABCDEFGHIJ","ABCDEFGHIJ","ABCDEFGHIJ","ABCDEFGHIJ","ABCDEFGHIJ","ABCDEFGHIJ","ABCDEFGHIJ","ABCDEFGHIJ","ABCDEFGHIJ","ABCDEFGHIJ"]),["AAAAAAAAAA", "BBBBBBBBBB", "CCCCCCCCCC", "DDDDDDDDDD", "EEEEEEEEEE", "FFFFFFFFFF", "GGGGGGGGGG", "HHHHHHHHHH", "IIIIIIIIII", "JJJJJJJJJJ" ])
		self.assertEqual(listDownward(["ABABABABAB","ABABABABAB","ABABABABAB","ABABABABAB","ABABABABAB","ABABABABAB","ABABABABAB","ABABABABAB","ABABABABAB","ABABABABAB"]),["AAAAAAAAAA", "BBBBBBBBBB", "AAAAAAAAAA", "BBBBBBBBBB", "AAAAAAAAAA", "BBBBBBBBBB", "AAAAAAAAAA", "BBBBBBBBBB", "AAAAAAAAAA", "BBBBBBBBBB" ])
		
	def test_findForward(self):
		self.assertEqual(findForward(["cat", "dog", "fish", "house", "back"],["cat", "dog", "fish", "house", "back"],["A111cat11B","A111dog11B","A1fish111B","A11111111B","A11111111B","A11111111B","A1house11B","A11111111B","A1back111B","A11111111B"]), ["cat: (FORWARD) row: 0 column: 4", "dog: (FORWARD) row: 1 column: 4", "fish: (FORWARD) row: 2 column: 2", "house: (FORWARD) row: 6 column: 2", "back: (FORWARD) row: 8 column: 2"])
		self.assertEqual(findForward(["hey","how","are","you"],["hey","how","are","you"],["hey111111","A111111how","are111111B","you111111B"]),["hey: (FORWARD) row: 0 column: 0", "how: (FORWARD) row: 1 column: 7", "are: (FORWARD) row: 2 column: 0", "you: (FORWARD) row: 3 column: 0"])

		
	def test_findBackward(self):
		self.assertEqual(findBackward(["cat", "dog", "fish", "house", "back"],["cat", "dog", "fish", "house", "back"],["A111tac11B","A111god11B","A1hsif111B","A11111111B","A11111111B","A11111111B","A1esuoh11B","A11111111B","A1kcab111B","A11111111B"]), ["cat: (BACKWARD) row: 0 column: 6", "dog: (BACKWARD) row: 1 column: 6", "fish: (BACKWARD) row: 2 column: 5", "house: (BACKWARD) row: 6 column: 6", "back: (BACKWARD) row: 8 column: 5"])
		self.assertEqual(findBackward(["hey","how","are","you"],["hey","how","are","you"],["A11yeh1AAA","A111111woh","era111111B","uoy111111B"]),["hey: (BACKWARD) row: 0 column: 5", "how: (BACKWARD) row: 1 column: 9", "are: (BACKWARD) row: 2 column: 2", "you: (BACKWARD) row: 3 column: 2"])
		
		

if __name__ == '__main__':
	unittest.main()