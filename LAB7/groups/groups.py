# Lab 7
# 
# Name: Comal Virdi 
# Instructor: S. Einakian
# Section: 01

def groups_of_3 (list1):
	list2  = []
	for x in range (0, len(list1), 3):
		list2.append(list1[x:x+3])
	return list2