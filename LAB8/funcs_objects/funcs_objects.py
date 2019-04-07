# LAB 8
# COMAL VIRDI
# EINAKIAN
# SECTION 01

from objects import *
import math

# calculates the euclidian distance between two point objects
'''return the euclidian distance calculated with the x and y values of 
	the given points
'''
# Object Object --> int
def distance(p1,p2):
	return math.sqrt(((p1.x-p2.x)**2)+((p1.y-p2.y)**2))

#determines whether or not two circles overlap
'''calculate the sum of the radii
	calculate the distance between the circle centers
	if the distance is greater than the radii return true
'''
# Object Object --> bool
def circles_overlap(c1, c2):
	sumRadii = c1.radius + c2.radius
	distanceCP = distance(c1.center, c2.center)
	return (sumRadii>distanceCP) 
