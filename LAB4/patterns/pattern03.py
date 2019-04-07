#Comal Virdi

#Lab 4
#Professor Einakian
#Section 01

import driver

def letter(row, col):
	if (col > 9):
		return 'O'
	else:
		return 'X'



if __name__ == '__main__':
 driver.comparePatterns(letter)