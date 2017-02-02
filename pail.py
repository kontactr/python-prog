str = input("enter your string: ")
flag = 0
for i in range(0,len(str),1):
    if (str[i] == str[-(i+1)]):
        continue
    else:
        flag = 1
        break
if (flag == 0):
        print ("yes")
else:
        print ("no")
