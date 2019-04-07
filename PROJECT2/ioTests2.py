from landerFuncs import *

def main():
   showWelcome()
   getFuel()
   getAltitude()
   displayLMState(1, 1, -54, 48, 10)
   
   # call twice to test with requesting too much fuel
   rate = getFuelRate(45)
   print ('rate:', rate)
   rate = getFuelRate(4)
   print ('rate:', rate)
   
   # call three times to display each possible comment
   displayLMLandingStatus(10)
   displayLMLandingStatus(-9)
   displayLMLandingStatus(-19)

if __name__ == '__main__':
   main()