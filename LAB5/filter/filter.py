#Comal Virdi

#Lab 5
#Professor Einakian
#Section 01

# this function returns all the positive numbers in a list
# list --> list 
def are_positive(list1):
	positive = lambda x:x>0
	return list(filter(positive,list1))

# this function returns all the numbers in a list greater than a given value 
# list int --> list 
def are_greater_than_n(list1, n):
	newList = []
	for x in list1:
		if x > n:
			newList.append(x)
	return newList

# this function returns all the elements of a list that are divisible by the given value
# list int --> list 
def are_divisible_by_n(list1,n):
	newList = []
	i = 0
	while i < len(list1):
		if list1[i] % n ==0:
			newList.append(list1[i])
			i+=1
	return newList


