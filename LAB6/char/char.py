# Lab 6
# 
# Name: Comal Virdi
# Instructor: S. Einakian
# Section: 01

#this function determines whether or not a character is uppercase or lowercase
''' get the numerical value of the character
	check if the character is within the range of a lowercase character
	if it is return true
	if it isn't return false
'''
# str --> bool
def is_lower_101(LorU):
	LorUval = ord(LorU)
	if ord('a') <= LorUval <= ord('z'):
		return True  
	else:
		return False

# this function returns the chaacter 13 places forward or backward from the original character passed in
''' check what type of charater is passed in (upper or lower case)
	if the character is between a and m add 13 to the value and return the char at that index
	if the character is between n and z subtract 13 to the value and return the char at that index
	if the character is not an alpha character, return the original char
'''	
# string --> string
def char_rot13(inChar):
	if ord('a') <= ord(inChar) <= ord('m'):
		return chr(ord(inChar)+13)
	elif ord('n') <= ord(inChar) <= ord('z'):
		return chr(ord(inChar)-13)
	elif ord('A') <= ord(inChar) <= ord('M'):
		return chr(ord(inChar)+13)
	elif ord('N') <= ord(inChar) <= ord('Z'):
		return chr(ord(inChar)-13)
	elif inChar.isalpha() == False:
		return inChar

