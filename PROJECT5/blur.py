# PROJECT 5
# 
# Name: Comal Virdi 
# Instructor: S. Einakian
# Section: 01


def start(arguments):
	try:
		 if len(arguments) > 3:
		 	raise TypeError
	except:
		print('Usage: python3 blur.py', arguments[1], '<OPTIONAL:reach>')
		exit()
	try: 
		fin = open(arguments[1])
	except:
		print ('Unable to open', arguments[1])
		exit()

	if len(arguments) == 3:
		reach = arguments[2]
	else:
		reach = 4

	oneD =[]
	i = 0
	for line in fin:
		if i < 3:
			oneD.append(line.rstrip())
		else:
			oneD.append((int(line.rstrip())))
		i+=1

	wH= str(oneD[1]).split()
	w = int(wH[0])
	h = int(wH[1])

	twoD = []
	for x in range(0,len(oneD),3):
		twoD.append(oneD[x:x+3])
		
	threeD = []
	for y in range (1, len(twoD),w ):
		threeD.append(twoD[y:y+w])
	fin.close()

	return threeD, reach, twoD[0]

def blur(threeD, reach, firstCell):
	fout = open('blurred.ppm', 'w+')
	for x in firstCell:
		fout.write(str(x) +'\n')

	for x in range (len(threeD)):
		for y in range (len(threeD[x])):
			for RGB in range(3):
				
				rowReachL = x - int(reach)
				if rowReachL < 0:
					rowReachL = 0

				rowReachR = x + int(reach)
				if rowReachR > len(threeD):
					rowReachR = len(threeD) - 1

				colReachU = y - int(reach)
				if colReachU < 0:
					colReachU = 0

				colReachD = y + int(reach)
				if colReachD > len(threeD[x]):
					colReachD = len(threeD[x]) - 1

				total = 0
				count = 0
				for rowRGBVal in range (rowReachL, rowReachR):
					for colRGBVal in range (colReachU, colReachD):
							total += threeD[rowRGBVal][colRGBVal][RGB]-1
							count +=1
				fout.write(str(int(total/count))+ '\n')
	fout.close()
