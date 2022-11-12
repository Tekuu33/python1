import seaborn as sns
import matplotlib.pyplot as plt
import pandas
import numpy as np

# read a titanic.csv file
# from seaborn library
#df = sns.load_dataset('titanic')
#print (df)
# who v/s fare barplot
#sns.barplot(x='who',
#            y='fare',
#            data=df)

# Show the plot
ff = 23 -1
df1 = pandas.read_csv("QAC3.csv")
#xd = sns.load_dataset("df1")
sns.barplot(y='Group',
            x='Log',
            hue = "Group",
            dodge = False,
            errcolor = "gray",
            data=df1)
plt.xlim(0, 9)

print(df1["Group"])
plt.grid(axis="x", color = "gray")


plt.show()

