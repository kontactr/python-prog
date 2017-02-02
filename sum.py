#input file = input.txt.txt
#output file = output.txt.txt
#windows sum.py < input.txt.txt > output.txt.txt
flag = True
sum1 = 0
while flag:
	try:
		a = int(input())
		sum1 += a
	except Exception as err:
		flag = False
print (sum1)