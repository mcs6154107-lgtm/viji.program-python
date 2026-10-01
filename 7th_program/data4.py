import pandas as pd
import numpy as np

data = {
    'Product': ['Laptop', 'Mobile', 'Tablet', 'Laptop', 'Mobile'],
    'Quantity': [5, 10, 7, 3, 8],
    'Price': [50000, 20000, 15000, 50000, 20000]
}

df = pd.DataFrame(data)

df['Total_Sales'] = df['Quantity'] * df['Price']

sales = df['Total_Sales'].to_numpy()

# Statistical calculations
mean = np.mean(sales)
median = np.median(sales)
std_dev = np.std(sales)
variance = np.var(sales)

print("Sales Statistics")
print("----------------")
print("Mean Sales:", mean)
print("Median Sales:", median)
print("Standard Deviation:", std_dev)
print("Variance:", variance)

# Sales above average
above_average = df[df['Total_Sales'] > mean]

print("\nSales Above Average:")
print(above_average)