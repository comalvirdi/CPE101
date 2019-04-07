# Project 4
# 
# Name: Comal Virdi and Mary McCafferty
# Instructor: S. Einakian
# Section: 01

from func_calcudoku import *

def main():

	cages = getCages()

	grid =[]
	for x in range(5):
		grid.append(5*[0])

	cell = 0
	row = 0
	col = 0

	while cell < 25:
		row = cell // 5
		col = cell % 5
		grid[row][col] += 1

		if grid[row][col] > 5:
			grid[row][col] = 0
			cell -=1

		else:
			
			if validateAll(grid, cages):
				cell += 1

	for compRow in grid:
		print (*compRow, sep=" ")

		
	

if __name__ == "__main__":
    main()