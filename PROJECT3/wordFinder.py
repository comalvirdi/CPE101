# Project 3
# 
# Name: Comal Virdi and Mary McCafferty
# Instructor: S. Einakian
# Section: 01

from funcs import *

def main():
	
	
	puzzle = getPuzzleComponents()

	wordList = getwords()
	forwardIndex = findForward(wordList, wordList, puzzle)
	backwardIndex = findBackward(wordList,forwardIndex, puzzle)
	print (wordList)
	print (puzzle)

	downwardIndex = findDownward(wordList, backwardIndex, puzzle)
	upwardIndex = findUpward(wordList, downwardIndex, puzzle)
	print (upwardIndex)

	print ("Puzzle:")
	print (" ")
	for y in puzzle:
		print (y)
	print (" ")
	for x in wordNotFound(upwardIndex):
		print (x)

	
		


if __name__ == '__main__':
	main()
