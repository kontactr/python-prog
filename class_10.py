# multiple inheritance

class project:
	project_name = ""
	@classmethod
	def project(cls,name):
			cls.project_name = name

project.project("python")

class emp(object):
	name = ""
	def __init__(self,name):
		self.name = name

	def print_data(self):
		print (self.name)

class man(emp,project):
	department = ""
	def __init__(self,name,department):
		self.department = department
		super().__init__(name)

	def print_data(self):
		super().print_data()
		print (self.department)

man1 = man("abc","a.inc")
man1.print_data()
man("bcd","b.inc").print_data()
print()
#classmethod change data and print
print (man1.project_name)
man1.project("flask")
print (man1.project_name)
print (project.project_name)
project.project("flask")
print(man1.project_name)
print(project.project_name)

