# LAB 8
# COMAL VIRDI
# EINAKIAN
# SECTION 01

from utility import *

class Point:
	#define the attributes
	def __init__(self, x, y):
		self.x = x
		self.y = y
	#define the equality function
	# x values and y values are equal, points are equal
	def __eq__(self, other):
		return epsilon_equal(self.x, other.x) and epsilon_equal(self.y, other.y) 

class Circle:
	#define the attributes
	def __init__(self, cP, r = 1):
		self.center = cP
		self.radius = r
 