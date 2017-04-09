import matplotlib.pyplot as plt
import xlrd
from xlrd import open_workbook, cellname
 
# Data to plot
labels = []
sizes = []
colors = []
explode = []

li = [labels,sizes,colors,explode]

book = open_workbook(r"C:\Users\Sony\Desktop\Book1.xlsx","r")
print (book)
sheet = book.sheet_by_index(0)

for col in range(sheet.ncols):
    for row in range(sheet.nrows):
        li[col].append(sheet.cell(row,col).value)


#print (li)

# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')
plt.show() 
