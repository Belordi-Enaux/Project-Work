import pandas as pd
import numpy as np
import matplotlib.pyplot as plotter

# Sample data for map visualization
data = {
    "Country": [
        "United States", "United Kingdom", "France", "Germany", "India",
        "Brazil", "Japan", "Australia", "Canada", "South Africa"
    ],
    "City": [
        "New York", "London", "Paris", "Berlin", "Mumbai",
        "São Paulo", "Tokyo", "Sydney", "Toronto", "Cape Town"
    ],
    "Sales": [
        150000, 120000, 100000, 95000, 110000,
        85000, 130000, 90000, 80000, 70000
    ],
    "Latitude": [
        40.7128, 51.5074, 48.8566, 52.5200, 19.0760,
        -23.5505, 35.6895, -33.8688, 43.6510, -33.9249
    ],
    "Longitude": [
        -74.0060, -0.1278, 2.3522, 13.4050, 72.8777,
        -46.6333, 139.6917, 151.2093, -79.3470, 18.4241
    ]
}

# Create a DataFrame
df = pd.DataFrame(data)

print(df)

plotter.bar(data["City"], data["Sales"])
plotter.title('CITIES AND THEIR SALES')
plotter.xlabel('Cities')
plotter.ylabel('Sales made')
plotter.show()
full_health = df.describe()
print(full_health)
