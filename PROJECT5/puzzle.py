# PROJECT 5
# 
# Name: Comal Virdi 
# Instructor: S. Einakian
# Section: 01

# this function determines whether or not to open the file / if the proper amount of arguments were provided and creates the lists of the file info
''' check the length of arguments provided
	raise error and print statement if length is incorrect // close program
	attempt to open file provided in arguments
	if file is invalid, raise error, print statement, and close program
	otherwise create 2D list holding cells gathered from input file
	return this list
	close the input file
'''
# list --> list
def getPuzzle(arguments):
	

	try:
		 if len(arguments) != 2:
		 	raise TypeError
	except:
		print('Usage: python3 puzzle.py image_file.ppm')
		exit()
	try: 
		fin = open(arguments[1], 'r')
	except:
		print ('Unable to open', arguments[1])
		exit()


	hugeList = []
	i = 0
	for line in fin:
		if i <3:
			hugeList.append(line.rstrip())
		else:
			hugeList.append((int(line.rstrip())))
		i+=1
	#print (hugeList)
	
	list1=[]
	for x in range(0,len(hugeList),3):
		list1.append(hugeList[x:x+3])
	fin.close()
	return list1

# this function calculates and returns new RGB values for each of the cells
''' create new output file
	add first cell to file
	iterate through list of input cells
	multiply all red values by 10
	if value is greater than 255, set new value equal to 255
	add new values output file
	close file
'''
#list --> file
def changeRGBVals(list1):
	fout = open('hidden.ppm', 'w+')
	for y in list1[0]:
		fout.write(str(y) +'\n')
	for x in range (1, len(list1)):
		newRvalue = list1[x][0] * 10
		if newRvalue > 255:
			newRvalue = 255
		for x in range(3):
			fout.write(str(newRvalue)+ '\n')
	fout.close()

