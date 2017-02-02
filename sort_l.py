def sort_l(l):
	k = len(l)
	for j in range(k-1):
		for p in range(j,k):
			if l[j] > l[p]:
				temp = l[j]
				l[j] = l[p]
				l[p] = temp
	return l

string  = input("Enter your element to be sort with space sep: ").split(" ")
l = []
for j in string:
	l.append(int(j))
l = sort_l(l)
print (l)
if(input("Want sorted set?  yes or no: ") == "yes"):
	l = set(l)
	print(l)
else:
	pass