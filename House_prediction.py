import numpy as np
import pandas as pd
import matplotlib.pyplot as plotter
from scipy import stats

Data1 = (3,4,5,6,8,9,10,12,15 )
Data2 = (3,8,8,9,9,9,10,10,15 )

min1 = np.min(Data1)
min2 = np.min(Data2)
max1 = np.max(Data1)
max2 = np.max(Data2)
avg1 = np.average(Data1)
avg2 = np.average(Data2)

print("The minimum values are: ", min1, min2)
print("The maximun values are: ", max1, max2)
print("The Averages are: ", avg1, avg2)

plotter.scatter(Data1,Data2)
plotter.title('A scatter plot')
plotter.xlabel('First dataset')
plotter.ylabel('Second data')
plotter.grid('true')
plotter.show()

