a = int(input("Enter number: "))
import math as m
flag = True
for i in range(1,int(m.sqrt(a))):
	if (a % i) == 0 :
		flag = False
		break
if(flag):
	print("prime number",a)
else:
	print("not prime number",a)