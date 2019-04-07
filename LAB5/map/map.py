#Comal Virdi

#Lab 5
#Professor Einakian
#Section 01


# this function takes a list and returns a new list with the squares of the parameter
# list --> list
def square_all(inList):
	newL=[x**2 for x in inList]
	return newL

# this takes a list and any value and returns a list with the sum of the input and each element   
# list int/float --> list
def add_n_all(list,n):
	newL = []
	i = 0
	while i < len(list):
		sumNL = list[i]+n
		newL.append(sumNL)
		i += 1
	return newL

# this function takes a list and returns a list of true or false values depending on whether or not the elements of the parameter list are even or odd
# list (ints) --> list(bools)
def even_or_odd_all(intList):
	newL = []
	for i in intList:
		if i % 2 == 0:
			newL.append(True)
		else:
			newL.append(False)
	return newL

 

	

