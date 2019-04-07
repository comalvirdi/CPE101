#Comal Virdi

#Lab 4
#Professor Einakian
#Section 01

import driver

def letter(row, col):
	if (row > 9):
		return 'Q'
	else:
		return 'R'



if __name__ == '__main__':
 driver.comparePatterns(letter)