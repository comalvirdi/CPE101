# Lab 6
# 
# Name: Comal Virdi
# Instructor: S. Einakian
# Section: 01

# this function calculates the sum of the elements of a list
""" iterate through elements of list
 	if element is int or float, add that value to the total
 	if element is list, iterate through elements of sublist
 	add sublist element values to the total
 	return the total
"""
# list --> int or float
def sum(l1):
	total = 0
	for x in l1:
		if type(x) == int or type(x)==float:
			total+= x
		else:
			for y in x:
				total += y

	return total


# this function returns the index of the smallest element in a list
''' create a variable to hold the min value
	check if the length of the list is greater than 0
	if not return -1
	if greater than 0 set the min to the first value in the list
	check the element in the list if it is iterable
	if not check if the element is less than the min
	if it is less, set min equal to that element
	if the element is iterable, iterate through the elements of that list
	check if the sub-elements are less than the min
	if they are less, set min equal to that sub-element
	when done checking all elements return the index of the min value
'''
# list -- > int
def index_of_smallest(l1):

	min = 0
	index = 0 
	if len(l1) == 0:
		return -1
	else:
		for x in range (len(l1)):
			if type(l1[x]) == int or type(l1[x])==float: 
				if l1[x] < min:
					min = l1[x]
					index = x
			else:
				for y in range (len(l1[x])):
					if l1[x][y] < min:
						min = l1[x][y]
						index = x
	return index
	