# LAB 3 

# Name: Comal Virdi
# Instructor: S. Einakian
# Section: 01

# take in two numbers and determine which is the greater of the two
# float float --> float
def max_101(num1, num2):
	
	if num1 > num2 :
		return num1
	else :
		return num2

# takes 3 numbers and determines which of the three is the greatest
# int int int --> int
def max_of_three (num1, num2, num3):
	
	if  num2 <= num1 >= num3 :

		return num1

	elif num3 <= num2 >= num1 :

		return num2

	else :

		return num3

# takes the number of days late a book is and determines the fee 
# int --> int
def rental_late_fee (daysLate):

	if daysLate <= 0 : 

		return 0

	elif 0 < daysLate <= 5 :

		return 5

	elif 5 < daysLate <= 15 :

		return 7

	elif 15 < daysLate <= 24 :

		return 19

	else :

		return 100





