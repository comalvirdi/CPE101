#COMAL VIRDI
#EINAKIAN
#SECTION 1
#PROJECT 6

def main():
	'''ob = Crime(150084225, 'ROBBERY')
	ob.set_time('Wednesday', '09/30/2015', '23:53')
	print(ob)
	x = get_crimes()
	
	y = create_crimes(x)
	times = get_times()
	update_crimes(y,times)'''

	crimes = get_crimes()
	times = get_times()
	robberyObs = create_crimes(crimes)
	#print (robberyObs)
	sorts = sort_crimes(robberyObs)
	#print(sorts)
	l = (update_crimes(sorts, times))
	for x in l:
		print (x)



class Crime(object):
	# this is the class that creates crime objects

	"""docstring for Crime"""
	def __init__(self, ID, category):
		self.ID = ID
		self.category = category
		self.day = None
		self.month = None
		self.hour = None
	#this function defines equity for the objects
	#object object —> bool

	def __eq__(self, other):
		return type(other) == type(self) and self.ID == other.ID

	# this function defines the representation for the object when printed
	# object —> string

	def __repr__(self):
		return ('{}    {}    {}    {}    {}').format(self.ID, self.category, self.day, self.month, self.hour)
	# this function sets the time information for the object based on the time file
	# object, string, string, string —> none
	‘’’ create a list of the months, grab the original two number representation of the month, 			subtract one, and assign that element from the months list to the self.month
	grab the hour representation, if it is greater than 13, subtract 12 and add PM, If it is = 0 			or 12 set the time equal to 12 AM and PM respectively, if the time is anything else, set 			
	the time to that number AM’’’
	def set_time(self, day_of_week, month, hour):
		self.day = day_of_week
		months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
		newMonth = month[0:2]
		self.month = months[int(newMonth) - 1]
		hourC = int(hour[0:2])
		if hourC >= 13:
			self.hour = str(hourC - 12 ) +'PM'
		elif hourC == 12:
			self.hour = '12PM'
		elif hourC == 0:
			self.hour = "12AM"
		else:
			self.hour = str(hourC) +'AM'

		
 # this function gets the crimes and puts them into a list by iterating through each line of the crimes file and appending it to a list
 # none --> list
def get_crimes():
	fin = open('tester.py')
	fin.readline()
	crimes = []
	for line in fin:
		crimes.append(line)
	return crimes
# this function gets the times and puts them into a list by iterating through each line of the times file and appending it to a list
 # none --> list
def get_times():
	fin = open('testerTimes.tsv')
	fin.readline()
	times = []
	for line in fin:
		times.append(line)
	return times

#this function creates crime objects that are both unrepeated and of category ROBBERY
''' create three empty lists
	iterate through the given list, splitting each line
	for each split line check if the type robbery 
	if its is, check if it id is in the ID list 
	if not, append the id to the id check, and create an objecct of the element and add that to 
	the robbery list
	return the robbery list
'''
# list --> list
def create_crimes(crimes):
	crimeList = []
	checkIDs = []
	robberyObs = []
	for x in crimes:
		l = x.split()
		crimeList.append(l)
	for x in crimeList:
		if x[1] == 'ROBBERY':
			if x[0] not in checkIDs:
				checkIDs.append(x[0])
				robOb = Crime(x[0], x[1])
				robberyObs.append(robOb)
	return robberyObs

def sort_crimes(crimes):
	return(sorted(crimes, key = lambda x: int(x.ID)))
	return crimes.sort()

def update_crimes(crimes, lines):
	times =[]
	upCrimes = []
	for y in lines:
		times = y.split()
		print (times[0])
		crimeOB = (find_crime(crimes, times[0]))

		if crimeOB == None:
			continue
		crimeOB.set_time(times[1], times[2], times[3])
		#print(y, times[1], times[2], times[3])
		upCrimes.append(crimeOB)
	return cut_crimes(sort_crimes(upCrimes))

def cut_crimes(crimes):
	checkIDs = []
	robberyObs = []
	for x in crimes:
		if x.ID not in checkIDs:
			checkIDs.append(x.ID)
			robberyObs.append(x)
	return robberyObs

def find_crime(cri,Id):
	first = 0
	last = len(cri)-1
	found = False
	while first<=last and not found:
		midpoint = (first + last)//2
		if cri[midpoint].ID == Id:
			#print (cri[midpoint].ID, Id)
			found = True
			return cri[midpoint]


		else:
			if int(Id) < int(cri[midpoint].ID): 
				last = midpoint-1
			else:
				first = midpoint+1 
	
	


if __name__ == '__main__':
	#x =  (get_times())
	#print(x)
	#main()
	ob1 = Crime(1, 'ROBBERY')
	ob2 = Crime(2, 'ROBBERY')
	ob3 = Crime(3, 'ROBBERY')
	ob4 = Crime(4, 'ROBBERY')
	x = update_crimes([ob1,ob2,ob3,ob4], ['1\tTuesday\t01/06/2015\t16:53\n', '2\tSaturday\t01/03/2015\t14:06\n', '4\tTuesday\t01/06/2015\t13:00\n', '3\tWednesday\t01/07/2015\t17:30\n'])
	print (x)	