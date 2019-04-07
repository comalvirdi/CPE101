# Project 4
# 
# Name: Comal Virdi and Mary McCafferty
# Instructor: S. Einakian
# Section: 01


# this function takes the 2D grid and transposes it so that each element in the new list is a column of the original grid
''' 
	Create new grid
	iterate through row indicies
	create a temporary list
	iterate through column indicies
	add the element at column index / row index to temp (as opposed to row index / column index)
	add temp to new grid
	return new grid
'''
# list --> list
def transpose(grid):
	tGrid = []		
	for i in range (len(grid)):
		temp = []
		for l in range(len(grid[i])):
			temp.append(grid[l][i])
		tGrid.append(temp)

	return tGrid


# This function creates a nested list to represent all the cage informations passed in by the user
''' 
	takes an input value from the user for number of cages
	takes input for as many cages as there are 
	places input into a list.
	returns the cage information as a nested list.
'''
# none --> list
def getCages():
	cages = int(input()) # taking out the "number of cages" within input statement so that the output matches given output
	cageLUF = []
	for x in range (cages):
		cage = input() #  "'Cage Number ' + str(x) +':'"  so that the output matches given output
		cageLUF.append(cage.split())
	cageList = [[int(i) for i in lst] for lst in cageLUF]
	return cageList

# This function takes the 2D grid and its cages checks in a for loop that the sum of all of the elements in the cage equals the required sum. 
#If the sum of the elements is greater than the required sum the function returns False.
''' 
	create check list
	traverse through individual cages
	initialize a new sum
	initialize a list to hold cells from grid at cage positions
	access cells specified by cages
	add the values of thoes cells to sum
	append the cell to list that will check how man 0s are present
	call checkPop
	if checkPop is true and the cage is valid return true
	otherwise return false 
'''
#list, list --> bool
def validateCages(grid, cages):
	check = []

	for x in cages:
		sum = 0
		popCheck = []
		for y in range (1,len(x)):
			row = x[y] // 5
			col = x[y] % 5
			sum += grid[row][col]
			popCheck.append(grid[row][col])
		if checkPop(popCheck,sum,x) == False:
			return False
	return True	
	

#This function checks that the sum of the cages is less than the required sum while the value 0 still exists in the cage or the sum of the cages
#is equal to the value in the first index of the cage list when there are no zeros left in the cage. This function is necessary to so that validate cages 
# doesn't return True or False while still in for loop
''' 
	pass in values of cage, actual sum, and intended sum
	check sum and 0 count
	if sum is less than intended and there are 0 cages or sum is equal to intended and there are no 0s return true
	otherwise return false
'''
# list int list --> bool
def checkPop(popCage, sum, cage):
	if (sum < cage[0] and popCage.count(0)>=1) or (sum == cage[0] and popCage.count(0) == 0):
		return True
	else:
		return False



#This function takes the grid and checks for each value within the row or column to make sure no values repeat
''' 
	create a check flag and a list to hold the flags
	parse through the row or column
	if the count of the value in the row is greater than 1, turn the check False
	add the check to the list
	otherwise turn the check to True and add to list
	if there are any False checks
	return False
	otherwise return True
'''
# list --> bool
def validateRows(grid):
	check = None
	listChecks = []
	for x in grid:
		for y in x:
			if x.count(y) > 1 and y!=0:
				check = False
			else:
				check = True
			listChecks.append(check)

	#print(listChecks)
	if listChecks.count(False) > 0:
		return False
	else:
		return True

#This function checks if all validation functions are true so that cell can be incremented
''' 
	calls validaterows, validatecages, and validatecols
	if they are all true returns true
	otherwise return false.
'''
# list list --> bool
def validateAll(grid, cages):
	columnGrid = transpose(grid)
	#print(columnGrid)
	if validateRows(grid) and validateCages(grid, cages) and validateRows(columnGrid):
		return True
	else:
		return False





