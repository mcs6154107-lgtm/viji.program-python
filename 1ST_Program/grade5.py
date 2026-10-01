# Product Price Analyzer

# Input number of products
n = int(input("Enter number of products: "))

total_price = 0

# Loop to input product prices
for i in range(1, n + 1):
    price = float(input(f"Enter price of product {i}: "))
    total_price += price

# Calculate average price
average_price = total_price / n

# Determine product category
if average_price >= 10000:
    category = "Luxury"
elif average_price >= 5000:
    category = "Premium"
elif average_price >= 1000:
    category = "Standard"
else:
    category = "Budget"

# Display results
print("\n--- Product Result ---")
print("Total Price =", total_price)
print("Average Price =", average_price)
print("Category =", category)
