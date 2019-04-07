# Lab 7
# 
# Name: Comal Virdi 
# Instructor: S. Einakian
# Section: 01

import sys




def commandLineStuff():
	arguments = sys.argv
	ints = 0
	floats = 0
	other = 0
	sum1 = 0
	
	if len(arguments) > 3 or len(arguments)< 2 \
		or ((len(arguments) == 3 and arguments[2] != '-s') \
	 	and arguments[1] != '-s'):
		print("Usage: [-s] file_name")
		exit()
	try:
		if ((len(arguments) == 3 and arguments[2] == '-s') or len(arguments)==2):
			fin = open(arguments[1])
		else:
			fin = open(arguments[2])
	except Exception as err:
		print('Unable to open ' + arguments[0], err)
		exit()

	for line in fin:
		values = line.split()
		for x in range (len(values)):
			try:
				int(values[x])
				ints+=1
				sum1 += int(values[x])
			except:
				try:
					float(values[x])
					floats +=1
					sum1 += float(values[x])
				except:
					other +=1
			
	print ('Ints: ' + str(ints) + '\nFloats: ' + str(floats) + '\nOther: ' + str(other))
	if ((len(arguments) == 3 and arguments[2] == '-s') or arguments[1] == '-s'):
		print('Sum:' + str(sum1))

commandLineStuff()