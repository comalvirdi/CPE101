# LAB 8
# COMAL VIRDI
# EINAKIAN
# SECTION 01

from funcs_objects import *
from objects import *

# returns all the distances from the origin of a list of points
''' in a list comprehension, compare calculate the distance of every
	point in the  given list, from the origin
'''
# list --> list
def distance_all(pointL):
	p0 = Point(0,0)
	l = list(map(lambda x: distance(x,p0), pointL))
	return l

#determines what points in a list are in Q1 
'''
	filter through list of points
	check if x and y values are greater than 0
	if they are add them to returned list
'''
# list --> list
def are_in_first_quadrant(pointL):
	l = list(filter(lambda x: x.x > 0 and x.y > 0, pointL))
	return l
