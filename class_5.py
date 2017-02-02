#declare class members and constructor

#self - object itself

class emp:
	first_name = ""
	last_name = ""
	email = ""
	def __init__(self,first_name,last_name,email):
		self.first_name = first_name
		self.last_name = last_name
		self.email = email
	def print_data(self):
		return (self.first_name+" "+self.last_name+" "+self.email)

emp1 = emp('abc','bcd','a@b.com')
emp2 = emp('bcd','cde','b@c.com')
print (emp1.print_data())
print (emp2.print_data())
