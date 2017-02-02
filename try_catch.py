try:
	a = int(input("Enter number: "))
	b  = int(input("Enter number: "))
	try:
		print (a % b)
	except Exception as err:
		print (err)
	finally:
		print ("inner finally")
except Exception as err1:
	print (err1)
finally:
	print("outer finally")