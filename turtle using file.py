import turtle as t
with open("command.txt","r") as file:
	a = 0;
	while True:
		command = file.readline()
		a+= True
		if(command == ""):
			break
		else:
			list_command = command.split(" ")
		if(list_command[0] == '#' or list_command[0] == '\n'):
			continue
		if(list_command[0].lower() == "fd"):
			t.forward(int(list_command[-1]))
		elif(list_command[0].lower() == "bd"):
			t.backward(int(list_command[-1]))
		elif(list_command[0].lower() == "bye"):
			t.bye()
		elif(list_command[0].lower() == "lt"):
			t.left(int(list_command[-1]))
		elif(list_command[0].lower() == "rt"):
			t.right(int(list_command[-1]))
		elif(list_command[0].lower() == "color"):
			t.color(list_command[-1])
		else:
			print("sorry we are trying to update list error command: "+str(a))
			print(list_command)
d = input("Enter any key to continue: ")

