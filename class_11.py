class emp:
	def data_name(self,name):
		pass
	def data_department(self,department):
		pass

class emp_grp_1(emp):
	def data_name(self,name):
		emp.name = name + " grp_1"
	def data_department(self,department):
		emp.department = department + " grp_1"

class emp_grp_2(emp):
	def data_name(self,name):
		emp.name = name + " grp_2"
	def data_department(self,department):
		emp.department = department + " grp_2"

emp1 = emp_grp_1()
emp1.data_name("abc")
emp1.data_department("a.inc")
print (emp1.name+" "+emp1.department)
obj_child = emp_grp_1()
obj_parent = obj_child.emp()
