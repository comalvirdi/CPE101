# Lab 6
# 
# Name: Comal Virdi
# Instructor: S. Einakian
# Section: 01


# this function takes an input string argument and returns the rot-13 encoding of the input string.
'''
	iterate through letters in string
	for each letter change to encoded letter
	add encoded letter to string
	add string to final string
'''
# string --> string
def str_rot_13(inString):
	newString = ""

	for x in inString:
		charString = ""
		if ord('a') <= ord(x) <= ord('m'):
			charString += chr(ord(x)+13)
		elif ord('n') <= ord(x) <= ord('z'):
			charString += chr(ord(x)-13)
		elif ord('A') <= ord(x) <= ord('M'):
			charString += chr(ord(x)+13)
		elif ord('N') <= ord(x) <= ord('Z'):
			charString += chr(ord(x)-13)
		elif x.isalpha() == False:
			charString += x	
		newString += charString
	return newString

#
'''
	check of letter is same as old letter
	if not add old letter to the list
	if same, add new letter to list
	turn list into string
'''
#
def str_translate_101(string1, old, new):
	l = [x if x!= old else new for x in string1]
	strl = "".join(l)
	return (strl)

