#declare members and class methods

#cls - classname

class emp:
	first_name = ""
	last_name = ""
	working_days = 5
	def __init__(self,first_name,last_name):
		self.first_name = first_name
		self.last_name = last_name

	def print_data(self):
		return (self.first_name+" "+self.last_name+" "+str(self.working_days)+" "\
			+self.project_name)

	#class method may be used to declare some attributes just same like constructor
	#only access through classname.class_method_name(<parameter>)
	@classmethod
	def change(cls,project_name):
		#class attribute create and also add all the objects
		cls.project_name = project_name

	@classmethod
	def retun_obj(cls,first_name,last_name):
		return cls(first_name,last_name)


emp1 = emp('abc','bcd')
emp2 = emp('bcd','cde')

#class method it also return new object
emp.change("python")
print(emp1.print_data())
print(emp2.print_data())


emp.change("flask")
print(emp1.print_data())
print(emp2.print_data())

#return object
print(emp.retun_obj("hello","world").print_data())
