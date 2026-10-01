import pandas as pd
import numpy as np

# Create sales dataset
data = {
    'Product': ['Laptop', 'Mobile', 'Tablet', 'Laptop', 'Mobile'],
    'Quantity': [5, 10, 7, 3, 8],
    'Price': [50000, 20000, 15000, 50000, 20000]
}

df = pd.DataFrame(data)

# Calculate total sales
df['Total_Sales'] = df['Quantity'] * df['Price']

print("Sales Data:")
print(df)

print("\nDataset Information:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe()) 