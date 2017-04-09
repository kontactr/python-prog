import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
import xlrd
from xlrd import open_workbook,cellname

objects = []
performance = []

li = [objects,performance]

book = open_workbook(r"C:\Users\Sony\Desktop\Book1.xlsx","r")
print (book)
sheet = book.sheet_by_index(1)

for col in range(sheet.ncols):
    for row in range(sheet.nrows):
        li[col].append(sheet.cell(row,col).value)

y_pos = np.arange(len(tuple(objects)))

 
plt.bar(y_pos, performance, align='center', alpha=0.5, color="red")
plt.xticks(y_pos, objects)
plt.ylabel('Usage')
plt.title('Programming language usage')
 
plt.show()
