a = [0,1]
for i in range(2,int(input("Enter number: "))):
	a.append(a[i-1] + a[i - 2])
print(a)