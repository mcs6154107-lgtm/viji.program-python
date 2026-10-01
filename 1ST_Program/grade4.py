# Temperature Analyzer

# Input number of days
n = int(input("Enter number of days: "))

total_temperature = 0

# Loop to input temperatures
for i in range(1, n + 1):
    temperature = float(input(f"Enter temperature for day {i}: "))
    total_temperature += temperature

# Calculate average temperature
average_temperature = total_temperature / n

# Determine weather condition
if average_temperature >= 35:
    condition = "Very Hot"
elif average_temperature >= 30:
    condition = "Hot"
elif average_temperature >= 20:
    condition = "Moderate"
else:
    condition = "Cold"

# Display results
print("\n--- Temperature Result ---")
print("Total Temperature =", total_temperature)
print("Average Temperature =", average_temperature)
print("Condition =", condition)

