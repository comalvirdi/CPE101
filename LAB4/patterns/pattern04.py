#Comal Virdi

#Lab 4
#Professor Einakian
#Section 01

import driver

def letter(row, col):
	if (row >= 2 and row <= 4 and col >= 3 and col <= 6):
		return 'M'
	else:
		return 'S'



if __name__ == '__main__':
 driver.comparePatterns(letter)

