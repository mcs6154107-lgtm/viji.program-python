import pandas as pd
import numpy as np

data = {
    'Product': ['Laptop', 'Mobile', 'Tablet', 'Laptop', 'Mobile'],
    'Quantity': [5, 10, 7, 3, 8],
    'Price': [50000, 20000, 15000, 50000, 20000]
}

df = pd.DataFrame(data)

df['Total_Sales'] = df['Quantity'] * df['Price']

# Group sales by product
product_sales = df.groupby('Product')['Total_Sales'].sum()

print("Product-wise Sales:")
print(product_sales)

# Find product with maximum sales
highest_product = product_sales.idxmax()
highest_sales = product_sales.max()

print("\nProduct with Highest Sales:", highest_product)
print("Highest Sales Amount:", highest_sales)