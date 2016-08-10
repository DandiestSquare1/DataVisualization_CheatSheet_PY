"""
BarChart -- Using matplotlib / pandas
"""

var = df.groupby(['Country']).Runs.sum()
fig = plt.figure()
ax = fig.subplot(1,1,1)
ax.set_xlabel('Country')
ax.set_ylabel('Runs')
plt.title('Highest Run Getters - Country Wise')

plt.show()
