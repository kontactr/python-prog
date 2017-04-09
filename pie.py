import matplotlib.pyplot as plt
 
# Data to plot
labels = []
sizes = []
colors = []
explode = []

for k in open("hp.txt"):
    po = k.split(",")
    #print (k)
    labels.append(po[0])
    sizes.append(int(po[1]))
    colors.append(po[2])
    explode.append(float(po[3]))

 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')
plt.show() 
