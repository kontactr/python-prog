a = 0
b = 1
c = int(input("Enter number: "))
print(a)
print(b)
for i in range(2,c):
	d = a+b
	a = b
	b = d
	print (d)
