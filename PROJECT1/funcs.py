# Project 1 

# Name: Comal Virdi
# Instructor: S. Einakian
# Section: 01

import math

# convert pounds to kilograms
# int --> int
def poundsToKG (pounds):
	

	kilograms = pounds * 0.453592

	return kilograms

# determine the mass of the object and convert the mass to kilograms 
# int --> int
def getMassObject (object):

	str(object)

	if object == "t" :
		massObject = 0.1

	elif object == "p" :
		massObject = 1.0

	elif object == "r" :
		massObject = 3.0

	elif object == "g" :
		massObject = 5.3

	elif object == "l" :
		massObject = 9.07

	else :
		massObject = 0.0

	return (massObject)


# determine the velocity of the object given the distance from the professor
# int --> int
def getVelocityObject(distance):

	velocityObject = math.sqrt((9.8 * distance)/2)

	return velocityObject

	

# determines the velocity of the skater given the mass of the skater and the object and the velocity of the object
# 3 ints --> int
def getVelocitySkater (massSkater, massObject, velObject):

	velocitySkater = (massObject * velObject) / massSkater

	return velocitySkater





