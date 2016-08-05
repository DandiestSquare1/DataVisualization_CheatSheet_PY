"""
Histogram -- Using matplotlib / pandas
"""

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.hist(df['Matches'], bins = 5)
plt.title('Highest Run Getters - ODI')
plt.xlabel('Matches')
plt.ylabel('No of Players')
plt.show()
