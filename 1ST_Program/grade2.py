# Employee Salary Analyzer

# Input number of employees
n = int(input("Enter number of employees: "))

total_salary = 0

# Loop to input salaries
for i in range(1, n + 1):
    salary = float(input(f"Enter salary of employee {i}: "))
    total_salary += salary

# Calculate average salary
average_salary = total_salary / n

# Classify salary range
if average_salary >= 100000:
    category = "High Salary"
elif average_salary >= 50000:
    category = "Good Salary"
elif average_salary >= 25000:
    category = "Average Salary"
else:
    category = "Low Salary"

# Display results
print("\n--- Salary Result ---")
print("Total Salary =", total_salary)
print("Average Salary =", average_salary)
print("Category =", category)
