#declare class with only constructor

#self - object itself

class empl:
	def __init__(self,first_name,last_name):
		self.first_name = first_name
		self.last_name = last_name

emp1 = empl('abc','bcd')
emp2 = empl('bcd','cde')
emp1.email = 'a@b.com'
emp2.email = 'b@c.com'
print (emp1.first_name+" "+emp1.last_name+" "+emp1.email)
print (emp2.first_name+" "+emp2.last_name+" "+emp2.email)

