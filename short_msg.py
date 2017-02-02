#convert short form to full form 
#file abb.txt
while True:
	string = input("Enter your string or done to exit: ")
	if (string == "done" ):
		break
	answer = ""
	flag = False
	list_abb = ""
	list_str = string.split(" ")
	for j in list_str:
		flag = False
		with open("abb.txt","r") as file:
			while True:
				line = file.readline()
				list_abb = line.split(",")
#				print(j+" "+str(flag)+" "+list_abb[0])
				if(list_abb[0] == ''):
					break
				if(j == list_abb[0]):
					flag = True
#					print(j+" "+str(flag)+" "+list_abb[0])
					break
			if(flag):
				print(list_abb[-1],end="")
			else:
				print(j,end="\n")
	print()