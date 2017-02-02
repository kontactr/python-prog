#function which is sort lists 
#takes as many arguments as you want
#variable length argument simple example

def sort_list(a,*argv):
	a.sort()
	print (a)
	for j in  argv:
		j.sort()
	#if we print (j.sort(),j)then result will be
	#None,[....]
		print(j)
		
		
list1 = [5,4,3,2,1]
list2 = [6,5,4,3,2,1]
list3 = [7,5,4,2,5,25,2]
list4 = [214,24,21,5,3632,643,64,45,]		
sort_list(list1,list2,list3,list4,[35,73467,437,34,1,24,136])
