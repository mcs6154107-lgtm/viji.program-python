import pandas as pd
import numpy as np

data = {
    'Product': ['Laptop', 'Mobile', 'Tablet', 'Laptop', 'Mobile'],
    'Quantity': [5, 10, 7, 3, 8],
    'Price': [50000, 20000, 15000, 50000, 20000]
}

df = pd.DataFrame(data)

# Calculate sales
df['Total_Sales'] = df['Quantity'] * df['Price']

# NumPy statistical calculations
total_sales = np.sum(df['Total_Sales'])
average_sales = np.mean(df['Total_Sales'])
maximum_sales = np.max(df['Total_Sales'])
minimum_sales = np.min(df['Total_Sales'])

print("Total Sales:", total_sales)
print("Average Sales:", average_sales)
print("Maximum Sales:", maximum_sales)
print("Minimum Sales:", minimum_sales)
