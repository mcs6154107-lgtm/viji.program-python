# Electricity Bill Calculator

# Input number of months
n = int(input("Enter number of months: "))

total_units = 0

# Loop to input electricity units
for i in range(1, n + 1):
    units = float(input(f"Enter units consumed in month {i}: "))
    total_units += units

# Calculate average units
average_units = total_units / n

# Calculate bill
if average_units <= 100:
    rate = 2
elif average_units <= 200:
    rate = 4
elif average_units <= 300:
    rate = 6
else:
    rate = 8

bill = average_units * rate

# Display results
print("\n--- Electricity Result ---")
print("Total Units =", total_units)
print("Average Units =", average_units)
print("Rate per Unit =", rate)
print("Estimated Bill =", bill)
