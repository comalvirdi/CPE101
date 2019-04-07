# Project 2 - Moonlander Functions
# Author: Comal Virdi
# Instructor: S. Einakian
# Section: 01

from landerFuncs import *

def main():

	elapsedTime = 0
	fuelRate = 0
	velocity = 0.00
	gravity = 1.62

	showWelcome()
	altitude = getAltitude()
	fuelAmount = getFuel()
	print("\n")

	print ("LM state at retrorocket cutoff")
	displayLMState(elapsedTime, altitude, velocity, fuelAmount, fuelRate)
	print(" ")

	while altitude > 0.00 and fuelAmount > 0:

		fuelRate = getFuelRate(fuelAmount)
		fuelAmount = updateFuel(fuelAmount, fuelRate)	
		elapsedTime += 1
		acceleration = updateAcceleration(gravity, fuelRate)
		altitude = updateAltitude(altitude, velocity, acceleration)
		velocity = updateVelocity(velocity, acceleration)
		
		if fuelAmount == 0:
			continue
		
		if altitude == 0:
			print("\nLM state at landing/impact ")
			displayLMState(elapsedTime, altitude, velocity, fuelAmount, fuelRate)
			print(" ")
			displayLMLandingStatus(velocity)
			break

		displayLMState(elapsedTime, altitude, velocity, fuelAmount, fuelRate)
		print(" ")

	else:

		if fuelAmount == 0:
			
			fuelRate = 0
			
			while altitude > 0.00:

				print("OUT OF FUEL - Elapsed Time:{:4d} Altitude:{:8.2f} Velocity:{:8.2f}" .format(elapsedTime, altitude, velocity))
				elapsedTime +=1
				acceleration = updateAcceleration(gravity, fuelRate)
				altitude = updateAltitude(altitude, velocity, acceleration)
				velocity = updateVelocity(velocity, acceleration)

			else:

				altitude = 0
				print("\nLM state at landing/impact ")
				displayLMState(elapsedTime, altitude, velocity, fuelAmount, fuelRate)
				print(" ")
				displayLMLandingStatus(velocity)
				

if __name__ == "__main__":
   main()