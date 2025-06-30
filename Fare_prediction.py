import pandas as pd
from sklearn.linear_model import LinearRegression

Data = {
    'Distance': [3.2,5.1,2.0,7.5,4.0,2.8,8.3,1.5],
    'Time_of_day': [10,18,8,20,15,9,22,7],
    'Fare': [12.5,18.3,9.8,22.4,15.2,11.0,25,7.5]
}

Dataf = pd.DataFrame(Data)

X = Dataf[['Distance', 'Time_of_day']]
Y = Dataf['Fare']

model = LinearRegression()

model.fit(X,Y)

new_trip = [[23,15]]

new_fare = model.predict(new_trip)

print(f"Predicted fare : $ {new_fare[0]: .2f}")
