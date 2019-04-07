# Project 1 

# Name: Comal Virdi
# Instructor: S. Einakian
# Section: 01

from funcs import *

def main():
	
	mass = poundsToKG(int(input("How much do you weigh (pounds)? ")))

	distance = float(input("How far away is your professor (meters)? "))

	objectThrown = input("Will you throw a rotten (t)omato, banana cream (p)ie, (r)ock, (l)ight saber, or lawn (g)nome? ")

	#print('')
	massObject = getMassObject(objectThrown)

	#print("OM: " + str(massObject))

	objectVelocity = getVelocityObject(distance) 

	#print("OV: " + str(objectVelocity))
	
	skaterVelocity = getVelocitySkater(mass, massObject, objectVelocity)

	#print("SV: " + str(skaterVelocity))


	print(" \nNice throw!", end=" ")

	if massObject <= 0.1 :

		print("You're going to get an F!")

	elif  0.1 < massObject <= 1.0 :

		print("Make sure your professor is OK.")

	else :

		if distance < 20 :

			print ("How far away is the hospital?")

		else :

			print ("RIP professor.")


	print("Velocity of skater: %.3f m/s"  % skaterVelocity)

	if skaterVelocity < 0.2 :

		print("My grandmother skates faster than you!")

	elif skaterVelocity >= 1.0 :

		print ("Look out for that railing!!!")






if __name__=='__main__':
	main()