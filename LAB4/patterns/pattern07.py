#Comal Virdi

#Lab 4
#Professor Einakian
#Section 01

import driver

def letter(row, col):
	
	if  col > 12 or col < 4 or row > 6 or row < 2:
		return "T"
	elif (row == 2 or row == 3) and 10 > col > 3:
		return "Z"
	elif (row == 4 or row == 5) and 7 > col > 3:
		return "Z"
	elif (row == 4 or row == 5) and 10 > col > 6:
		return "X"
	elif (row == 4 or row == 5) and 13 > col > 9:
		return "B"
	elif row == 6 and 13 > col > 6:
		return "B" 
	else:
		return "T"
	

if __name__ == '__main__':
 driver.comparePatterns(letter)
