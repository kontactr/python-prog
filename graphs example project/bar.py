

#import matplotlib.pyplot as plt; plt.rcdefaults()

#numpy module is used for mathematical operations and for array
import numpy as np

#matplotlib module is used for graph
import matplotlib.pyplot as plt


#x-axis
objects = []
#y-axis
performance = []

for k in open("input.txt","r"):
	temp = k.split(",")
	objects.append(temp[0])
	performance.append(int(temp[1]))

objects = tuple(objects)
	
#create x axis data into array
x_pos = np.arange(len(objects))




#create object for bar chart and put upper range
plt.bar(x_pos, performance, align='center', alpha=0.5)

#add into x-axis and y-axis

plt.xticks(x_pos, objects)

#put y-axis title
plt.ylabel('Usage')

#graph title
plt.title('Programming language usage')

#used for show  
plt.show()
