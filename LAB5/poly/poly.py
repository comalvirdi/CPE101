#Comal Virdi

#Lab 5
#Professor Einakian
#Section 01



# this function adds the coefficients of two lists of polynomials
# list list --> list
def poly_add2(p1, p2):
	
	poly3 = [p1[0]+p2[0],p1[1]+p2[1],p1[2]+p2[2]]
	return poly3


# this function multiplies two polynomials together
# list list --> list
def poly_mult2(p1,p2):

	f1 = [p1[0] * p2[0], p1[0] * p2[1], p1[0] * p2[2], 0, 0]
	
	f2 = [0, p1[1] * p2[0], p1[1] * p2[1], p1[1] * p2[2], 0]
	
	f3 = [0, 0, p1[2] * p2[0], p1[2] * p2[1], p1[2] * p2[2]]
	
	poly3 = [f1[0]+f2[0]+f3[0],f1[1]+f2[1]+f3[1],f1[2]+f2[2]+f3[2],f1[3]+f2[3]+f3[3], f1[4]+f2[4]+f3[4]]
	return poly3

