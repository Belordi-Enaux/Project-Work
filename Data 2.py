import pandas as pd
import numpy as np
import matplotlib.pyplot as plotter
from scipy import stats
import seaborn as sns

population = {
    'Cities': ["KMSI","ACCRA","TMAN","CAPE","TADI","TMLE","SYNI","HO","WA","Bolga"],
    'Men': [120,300,250,350,400,600,400,520,250,700],
    'Women':[300,400,500,350,200,450,520,800,530,780],
    'Children': [500,1000,600,900,700,900,100,350,600,420],
    'Total Polulation':[920,1700,1350,1600,1300,1950,1020,1670,1380,1900]
}

data = pd.DataFrame(population)

print("The overall data is: ",data)




plotter.bar(population["Cities"],population["Children"])
plotter.xlabel('Children')
plotter.ylabel('Cities')
plotter.title('CHILDREN POPULATION')
plotter.show()


plotter.bar(population["Cities"],population["Men"], color = "red")
plotter.xlabel('Male')
plotter.ylabel('Cities')
plotter.title('MALE POPULATION')
plotter.show()


plotter.bar(population["Cities"],population["Women"], color = "green")
plotter.xlabel('Female')
plotter.ylabel('Cities')
plotter.title('FEMALE POPULATION')
plotter.show()


plotter.bar(population["Cities"],population["Total Polulation"], color = "black")
plotter.xlabel('Total Population')
plotter.ylabel('Cities')
plotter.title('TOTAL POPULATION')
plotter.show()







population_2 = {
    'Cities': ["KMSI","ACCRA","TMAN","CAPE","TADI","TMLE","SYNI","HO","WA","Bolga"],
    'Men': [150,320,350,150,490,700,480,550,450,900],
    'Women':[450,600,590,300,400,590,600,850,750,800],
    'Children': [580,1500,1000,3500,2300,1000,900,500,900,720],
    'Total population_2': [1180,2420,1940,1450,4390,3590,2080,2300,2100,2420]
}

data_2 = pd.DataFrame(population_2)

print("The overall data for data_2 is: ",data_2)

plotter.bar(population_2["Cities"],population_2["Children"])
plotter.xlabel('Children')
plotter.ylabel('Cities')
plotter.title('CHILDREN POPULATION_2')
plotter.show()


plotter.bar(population_2["Cities"],population_2["Men"], color = "red")
plotter.xlabel('Male')
plotter.ylabel('Cities')
plotter.title('MALE POPULATION_2')
plotter.show()


plotter.bar(population_2["Cities"],population_2["Women"], color = "green")
plotter.xlabel('Female')
plotter.ylabel('Cities')
plotter.title('FEMALE POPULATION_2')
plotter.show()


plotter.bar(population_2["Cities"],population_2["Total population_2"], color = "black")
plotter.xlabel('Total Population')
plotter.ylabel('Cities')
plotter.title('TOTAL POPULATION_2')
plotter.show()

plotter.scatter(population["Total Polulation"],population_2["Total population_2"])
plotter.xlabel('total population for the first one')
plotter.ylabel('Total population for the second one')
plotter.title('Scattoer plot for the two populations')
plotter.show()

n = data.describe()
print(n)

m = data_2.describe()
print(m)

slope,intercept,p_value,y_value,cor_coef = stats.linregress(population["Total Polulation"],population_2["Total population_2"])
print("The Slope",slope)
print("The intercept",intercept)
print("The p_value",p_value)
print("The y_value",y_value)
print("The correlation coefficient",cor_coef)

