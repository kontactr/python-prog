#declare class with members and constuctor

#self - object itself

class empl:
	first_name = ""
	last_name = ""
	def __init__(self,first_name,last_name):
		self.first_name = first_name
		self.last_name = last_name

emp1 = empl("abc","bcd")
emp2 = empl("bcd","cde")
print(emp1.first_name+" "+emp1.last_name)
print(emp2.first_name+" "+emp2.last_name)
