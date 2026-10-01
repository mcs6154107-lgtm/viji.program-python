import pandas as pd
import numpy as np

data = {
    'Product': ['Laptop', 'Mobile', 'Tablet', 'Laptop', 'Mobile'],
    'Quantity': [5, 10, 7, 3, 8],
    'Price': [50000, 20000, 15000, 50000, 20000]
}

df = pd.DataFrame(data)

# Calculate total sales
df['Total_Sales'] = df['Quantity'] * df['Price']

# Product-wise analysis
product_summary = df.groupby('Product').agg(
    Total_Quantity=('Quantity', 'sum'),
    Total_Sales=('Total_Sales', 'sum'),
    Average_Sales=('Total_Sales', 'mean')
)

print("Product Sales Summary:")
print(product_summary)

# Overall statistics
total_sales = np.sum(df['Total_Sales'])
average_sales = np.mean(df['Total_Sales'])

print("\nSales Insights")
print("--------------")
print("Total Revenue:", total_sales)
print("Average Transaction Sales:", average_sales)

# Identify highest-selling product by quantity
quantity_by_product = df.groupby('Product')['Quantity'].sum()
highest_quantity_product = quantity_by_product.idxmax()

print("Most Sold Product:", highest_quantity_product)

# Identify highest revenue product
revenue_by_product = df.groupby('Product')['Total_Sales'].sum()
highest_revenue_product = revenue_by_product.idxmax()

print("Highest Revenue Product:", highest_revenue_product)