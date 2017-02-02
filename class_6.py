#declare members and access through class

#self - object itself

class emp:
	first_name = ""
	last_name = ""
	working_days = 5
	def __init__(self,first_name,last_name):
		self.first_name = first_name
		self.last_name = last_name
	def print_data(self):
		return (self.first_name+" "+self.last_name+" "+str(self.working_days)+" "\
			+str(self.val))

emp1 = emp('abc','bcd')
emp2 = emp('bcd','cde')

#add attribute through class
emp.val = 10

print(emp1.print_data())
print(emp2.print_data())

#this is also work so,that we can write self in the method
print(emp.print_data(emp1))
print(emp.print_data(emp2))

#variable access through class
print(emp.working_days)

#change that value
emp.working_days = 6

#print the change
print ("working day objet 1: "+str(emp1.working_days))
print ("working day objet 2: "+str(emp2.working_days))


#if we change the value of one of the object it only affect on that
emp1.working_days = 4
print ("working day objet 1: "+str(emp1.working_days))
print ("working day objet 2: "+str(emp2.working_days))


