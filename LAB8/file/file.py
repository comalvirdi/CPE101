# LAB 8
# COMAL VIRDI
# EINAKIAN
# SECTION 01


# this function prints each line in the file, print the line number, 
# the number of characters in the line, and the line itself
''' open file
	set line num tracker to 0
	for each line in file, print the line, line number, and the number of characters
	increment the line num tracker
'''
#
def fileStuff():
	fin = open('in.txt', 'r')
	lineNum = 0
	for line in fin:
		print('Line ', lineNum, '(', len(line.rstrip()), 'chars): ', line, end ='')
		lineNum +=1


fileStuff()