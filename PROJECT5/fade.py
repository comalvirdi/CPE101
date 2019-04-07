# PROJECT 5
# 
# Name: Comal Virdi 
# Instructor: S. Einakian
# Section: 01

import math

# this function determines whether or not the arguments provided by the user are valid and if they are
# formats the lines of the file inot a 2D list
''' if there are more or less than 5 arguments, raise an error , print the appropriate error statement and exit the program
	if the arguments are valid, open the file provided in the arguments
	if the file is invalid, print an error statement
	if no errors are caught, collect the row, column and radius from the arguments
	
	create a list to hold the values in the file
	create a counter
	iterate through the lines in the file
	if the counter is less than three, strip the lines and add them to the huge list
	if the counter is greater than three, strip the lines, cast them to ints and add them to the huge list
	increment the counter

	create another list
	increment through the huge list, stepping by 3
	add a list ofthree consecutive values to the  list
	
	close the file
	return the list, row, column and radius in a list
'''
# list --> list
def getPuzzleFade(arguments):
	

	try:
		 if len(arguments) != 5:
		 	raise TypeError
	except:
		print('Usage: python3 fade.py <image> <row> <column> <radius>')
		exit()
	try: 
		fin = open(arguments[1])
	except:
		print ('Unable to open', arguments[1])
		exit()

	row = arguments[2]
	column = arguments[3]
	radius = arguments [4]

	hugeList = []	
	i = 0
	for line in fin:
		if i <3:
			hugeList.append(line.rstrip())
		else:
			hugeList.append((int(line.rstrip())))
		i+=1

	list1=[]
	for x in range(0,len(hugeList),3):
		list1.append(hugeList[x:x+3])

	fin.close()
	return [list1, row, column, radius]


# this function creates the fade for the image
''' grab the first values of the first cell (which hold the dimensions) split this
	cast the width and height to ints
	open the file
	iterate throught the first cell and add these elements to the file
	iterate through the list of cells and determine the row and column values
	calculate the distance of the point from the provided column and radius	
	calculate the scale based off of the distance
	iterate through the RGB values of the pixels 
	calculate the new scaled RGB values 
	write these to the output file
	close the output file
'''
#list str str list --> file
def fade(l,radius,column, firstCell):
	wH= str(l[0][1]).split()
	w = int(wH[0])
	h = int(wH[1])
	fout = open('faded.ppm', 'w+')
	for y in firstCell:
		fout.write(str(y) +'\n')
	for x in range (1,len(l)):
		row = x//h
		col = x % w
		#print (row,col)
		d = math.sqrt(((col-int(column))**2)+((row-int(radius))**2))
		scale = (int(radius) - d) / int(radius)
		for RGB in l[x]:
			if scale < 0.2:
				newRGB = int(RGB *0.2)
			else:
				newRGB = int(RGB * scale)
			fout.write(str(newRGB) +'\n')
	fout.close()


# original functions that were too long and iterated through the list of cells too many times

	'''for x in distance:
		scale = (int(radius) - x) / int(radius)
		for pixel in range  (1, len(l)):
			for RGB in l[pixel]:
				#print (x,RGB, scale)
				if scale < 0.2:
					newRGB = RGB *0.2
				else:
					newRGB = RGB * scale
				fin2.write(str(newRGB) +'')
	fin.close()

	def distance(l, r, c):
		wH= str(l[0][1]).split()
		w = int(wH[0])
		h = int(wH[1])
		dL = []
		print (w,h)
		print (l)
		for x in range (1,len(l)):
			row = x//w
			col = x % h
			print (row,col)
			d = math.sqrt(((col-int(c))**2)+((row-int(r))**2))
			dL.append(d)
	return dL'''
	







