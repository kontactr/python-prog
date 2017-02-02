def push(b):
	if len(b) < a:
		c = int(input("Enter value: "))
		b.append(c)
	else:
		print ("queue overflow...")
	print()

def pop(b):
	if len(b) < 1:
		print ("queue underflow...")
	else:
		b.remove(b[0])
	print()

def sort(b):
	b.sort()
	print()

def print_(b):
	print (b)
	print()

def reverse(b):
	b.reverse()
	print()

a = int(input("Enter size: "))
b = []
flag = True
while flag:
	print ("1.insert\n2.pop\n3.display\n4.reverse\n5.sort\n6.exit")
	choice = int(input("Enter your choice: "))
	if choice == 1:
		push(b)
	elif choice == 2:
		pop(b)
	elif choice == 3:
		print_(b)
	elif choice == 4:
		reverse(b)
	elif choice == 5:
		sort(b)
	elif choice == 6:
		flag = False
	else:
		print("wrong choice..")

