
# For every function write purpose statement and signature
# Project 2 - Moonlander Functions
# Author: Comal Virdi
# Instructor: S. Einakian
# Section: 01

# shows the welcome message to user at launch of program
# none --> none  (nothing returned but string is printed)
def showWelcome():
   print("Welcome aboard the Lunar Module Flight Simulator\n \n   To begin you must specify the LM's initial altitude\n   and fuel level. To simulate the actual LM use\n   values of 1300 meters and 500 liters, respectively.\n \n   Good luck and may the force be with you!")

# prompts user for positive integer and returns it
# none --> int
def getFuel():
   
    while True:
        fuel = input("Enter the initial amount of fuel on board the LM (in liters): ")
        try:
            if int(fuel) < 0:
                print("ERROR: Amount of fuel must be positive, please try again")
                continue
            break
        except ValueError:
           print("ERROR: Amount of fuel must be positive, please try again")
    return int(fuel)


# prompts user for altitude value and returns it
# none --> int
def getAltitude():

    while True:
        altitude = input("Enter the initial altitude of the LM (in meters): ")
        try:
            if int(altitude) < 0 or int(altitude) > 9999:
                print("ERROR: Altitude must be between 1 and 9999, inclusive, please try again")
                continue
            break
        except ValueError:
            print("ERROR: Altitude must be between 1 and 9999, inclusive, please try again")
    return float(altitude)

 
 # displays elapsedTime, altitude, velocity, fuelAmount and fuelRate
 # int int int int int --> none (solely prints the values with some text)
def displayLMState(elapsedTime, altitude, velocity, fuelAmount, fuelRate):
    
    print("%15s" %"Elapsed Time:" "%5d" %elapsedTime, "s")
    print("%16s" %"Fuel:" "%5d" %fuelAmount, "l")
    print("%16s" %"Rate:" "%5d" %fuelRate, "l/s")
    print("%18s" %"Altitude:" "%8.2f" %altitude, "m")
    print("%18s" %"Velocity:" "%8.2f" %velocity, "m/s" )

# prompts user for fuel rate and depending on chosen rate, returns that fuel rate or current fuel rate
# int --> int
def getFuelRate(currentFuel):

    while True:
        fuelRate = input("Enter fuel rate (0-9, 0=freefall, 5=constant velocity, 9=max thrust): ")
        try:
            if int(fuelRate) < 0 or int(fuelRate) > 9:
                print("ERROR: Fuel rate must be between 0 and 9, inclusive")
                continue
            break
        except ValueError:
            print("ERROR: Fuel rate must be between 0 and 9, inclusive")

    if int(fuelRate) > currentFuel:
        return int(currentFuel)
    else:
        return int(fuelRate)        
 
# calculates and returns acceleration
# float int --> float
def updateAcceleration(gravity, fuelRate):
   
   return gravity * ((fuelRate / 5) - 1)

# calculates and returns altitude
# double double double --> double 
def updateAltitude(altitude, velocity, acceleration):
   
   altitude1 = altitude + velocity + (acceleration / 2)

   if altitude1 < 0.00:
      return  0
   
   return altitude1

# calculates and returns velocity
# double double --> double
def updateVelocity(velocity, acceleration):
   
    return velocity + acceleration   


# calculates fuel and returns it
# int int --> int
def updateFuel(fuelAmount, fuelRate):
    
    return fuelAmount - fuelRate

# displays status at landing
# int --> none 
def displayLMLandingStatus(velocity):
   
    if velocity <= 0 and velocity >= -1:

        print("Status at landing - The eagle has landed!")

    elif velocity < -1 and velocity > -10:

        print("Status at landing - Enjoy your oxygen while it lasts!")

    elif velocity <= -10:

        print ("Status at landing - Ouch - that hurt!")









