# LAB 8
# COMAL VIRDI
# EINAKIAN
# SECTION 01

from objects import *
import math

# calculates the euclidian distance between two point objects
# Object Object --> int
def distance(p1,p2):
	return math.sqrt(((p1.x-p2.x)**2)+((p1.y-p2.y)**2))

def circles_overlap(c1, c2):
	sumRadii = c1.radius + c2.radius
	distanceCP = distance(c1.center, c2.center)
	return (sumRadii>distanceCP) 
