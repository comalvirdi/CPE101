# Lab 2 Functions
#Name: Comal Virdi
#Section: 01

import math 

#this function evaluates x and y in an equation((x^3+y^3)/5x+7))
#2 ints --> int
def math_func1(x,y):
   return (x**3 + y**3) / (5*x + 7)

#this function is the quadratic formula
#3 ints --> int
def math_func2(a,b,c):
   return (-b + (math.sqrt(b**2 - 4*a*c)))/(2*a)

#this function computes the euclidian distance
#4 ints --> int
def d(x1,y1,x2,y2):
   return math.sqrt(((x1-x2)**2)+((y1-y2)**2))

#this function determines whether or not a number is negative
#int --> bool
def is_negative(x):
   return x<0   

#this function determines whether or not a number is dividable by 5
#int --> bool
def dividable_by_5(x):
   return x % 5 == 0
