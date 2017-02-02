#constructor overloading....

from pythonlangutil.overload import Overload, signature

class emp(object):
	name = ""
	def __init__(self,name):
		self.name = name

class man(emp):
	department = ""
	@Overload
	@signature("str","str")
	def __init__(self,department,name):
		emp.__init__(self,name)
		self.department = department

	@__init__.overload
	@signature()
	def __init__(self):
		emp.__init__(self,"Admin")

man1 = man("abc","bcd")
man2 = man()
#man1.hello("abc","bcd")
print (man1.name+" "+man1.department)
print (man2.name+" "+man2.department)
		
	