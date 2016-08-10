"""
PieChart -- Using matplotlib / pandas
"""

var = df.groupBy(['Players']).sum().stack()
temp = var.unstack()
type(temp)
x_list = temp['Runs']
lable_list = temp.index
pyplot.axis('Values')
plt.pie(x_list, labels = label_list, autopct = "%1.1f%")
plt.title('Players from a Country')
plt.show()
