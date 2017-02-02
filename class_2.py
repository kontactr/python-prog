#declare class with members 

#self - object itself

class empl:
	first_name = ""
	last_name = ""

empl1 = empl()
empl2 = empl()
empl1.first_name = "abc"
empl1.last_name = "bcd"
empl2.first_name = "bcd"
empl2.last_name = "cde"
print(empl1.first_name+" "+empl1.last_name)
print(empl2.first_name+" "+empl2.last_name)
