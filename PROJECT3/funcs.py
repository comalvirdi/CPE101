# Project 3
# 
# Name: Comal Virdi and Mary McCafferty
# Instructor: S. Einakian
# Section: 01


# this function takes the input from the user and puts every ten letters into a string within a list
# none --> list
def getPuzzleComponents():
	letters = input()
	puzzle = []
	for i in range (0, len(letters), 10):
		puzzle.append(letters[i : i + 10])
	return puzzle[:10]

# this function takes the words input by the user and splits them into elements of a list
# none --> list
def getwords():
	words = input()
	wordList = words.split()
	return wordList

# this function takes the puzzle list and reverses each of the elements 
# list --> list
def reverseList(puzzle):
	reversedPuzzle = []
	for i in puzzle:
		substring = ""
		for x in i:
			substring = x + substring
		reversedPuzzle.append(substring)
	return reversedPuzzle

# this function takes the puzzle list an creates a new list of the letters in each column as each element
# list --> list
def listDownward(puzzle):
	list2 = []			
	for i in range (10):
		substr = ""
		for l in puzzle:
			substr = substr + l[i]
		list2.append(substr)
	return list2

# this function finds all the words that are forward facing
# list list list ---> list
def findForward(wordList,wordInfoList, puzzle):
	for i in range (len(puzzle)):
		for l in wordList:
			if l in puzzle[i]:
				wordInfo = str(l) + ": (FORWARD) row: " + str(i) + " column: " + str(puzzle[i].index(l))
				wordInfoList[wordList.index(l)] = wordInfo
	return wordInfoList

# this function finds all the words that are downwards facing
# list list list ---> list
def findDownward(wordList, wordInfoList, puzzle):
	newPuzzle = listDownward(puzzle)
	allDownward = []
	for i in range (len(newPuzzle)):
		for l in wordList:
			if l in newPuzzle[i]:
				wordInfo = str(l) + ": (DOWN) row: "+ str(newPuzzle[i].index(l)) + " column: " + str(i)
				wordInfoList[wordList.index(l)] = wordInfo
	return wordInfoList

# this function finds all the words that are backwards
# list list list ---> list
def findBackward(wordList, wordInfoList, puzzle):
	newPuzzle = reverseList(puzzle)
	allBackward = []
	for i in range (len(newPuzzle)):
		for l in wordList:
			if l in newPuzzle[i]:
				wordInfo = str(l) + ": (BACKWARD) row: "+ str(i) + " column: " + str(9-newPuzzle[i].index(l))
				wordInfoList[wordList.index(l)] = wordInfo
	return wordInfoList

# this functio finds all the words that are upwards in the puzzle
# list list list ---> list
def findUpward(wordList,wordInfoList, puzzle):
	newPuzzle = reverseList(listDownward(puzzle))
	allUpward = []
	for i in range (len(newPuzzle)):
		for l in wordList:
			if l in newPuzzle[i]:
				wordInfo = str(l) + ": (UP) row: "+ str(9 - newPuzzle[i].index(l)) + " column: " + str(i)
				wordInfoList[wordList.index(l)] = wordInfo
	return wordInfoList

# this function adds the "word not found" string to the words that are not present in the puzzle
# list --> list
def wordNotFound (wordInfoList):
	for y in wordInfoList:
			if len(y) < 11:
				wordInfoList[wordInfoList.index(y)] = y + ": word not found" 
	return wordInfoList



