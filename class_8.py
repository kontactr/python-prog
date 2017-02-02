#static method and class

#classmethod - to set general value to all 
#if we set some value to object and then use classmethod
#it also affect object value


#staticmethod - use only by  class name
#general property
#static method cannot set particular object attribute directly
#instead  we pass it in it in parameter and then change

#cls - classname
#self - object itself
#self and cls both use to work same as procedure oriented approch
#if we doesn't write it in <parameter> it will may be raise error
#when we use as object oriented it will implicitly pass it as an first argument like

#procedure oriented
#emp.method_name(<object_name>,<parameter>....)

#object oriented
#object_name.method_name.(<parameter>...) generally we call
#internally it translated into procedure approch as upper mentioned.



class emp:
	def __init__(self,first_name,last_name):
		self.first_name = first_name
		self.last_name = last_name
	@classmethod
	def company_info(cls,name,working_days):
		cls.name = name
		cls.working_days = working_days
		cls.time = cls.working_time()
	@staticmethod
	#static method have not implicitly parameter like cls or self
	def working_time():
		return ("9:00:00 to 6:00:00")
	def print_data(self):
		return (self.first_name+" "+self.last_name+" "+self.name+" "+str(self.working_days)+" "+emp.working_time())
		#in upper line static method is used in object method


#create object
emp1 = emp('abc','bcd')
emp2 = emp('bcd','cde')

#set class varaible and print result
emp.company_info("a.inc",5)
print(emp1.print_data())

#again change class varaible and print result
emp.company_info("a.inc",7)
print(emp1.print_data())
print(emp2.print_data())

#set particular object class varaible value and print result
emp1.working_days = 6
print(emp1.print_data())
print(emp2.print_data())

#print static method data
print(emp.working_time())