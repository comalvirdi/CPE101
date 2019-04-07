# PROJECT 5
# 
# Name: Comal Virdi 
# Instructor: S. Einakian
# Section: 01

from puzzle import *
from fade import *
import sys
from blur import *

def main():

	arguments = sys.argv

	if len(arguments) == 2:
		l = getPuzzle(arguments)
		changeRGBVals(l)
		
	elif len(arguments) == 5:
		y = getPuzzleFade(arguments)
		fade(y[0], y[1], y[2],y[0][0])

	else:
		s = start(arguments)
		blur(s[0], s[1], s[2])





if __name__ == '__main__':
    main()