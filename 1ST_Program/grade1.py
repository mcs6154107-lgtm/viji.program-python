# Student Grade Analyzer

# Input number of subjects
n = int(input("Enter number of subjects: "))

total = 0

# Loop to input marks
for i in range(1, n + 1):
    mark = float(input(f"Enter marks for subject {i}: "))
    total += mark

# Calculate average
average = total / n

# Assign grade using conditions
if average >= 90:
    grade = 'A+'
elif average >= 75:
    grade = 'A'
elif average >= 60:
    grade = 'B'
elif average >= 50:
    grade = 'C'
else:
    grade = 'Fail'

# Display results
print("\n--- Result ---")
print("Total Marks =", total)
print("Average =", average)
print("Grade =", grade)