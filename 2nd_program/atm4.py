bill = 0

while True:
    print("\n===== ELECTRICITY MENU =====")
    print("1. Enter Units")
    print("2. Show Bill")
    print("3. Pay Bill")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        units = int(input("Enter electricity units: "))

        if units <= 100:
            bill = units * 2
        elif units <= 200:
            bill = units * 3
        else:
            bill = units * 5

        print("Bill calculated successfully")

    elif choice == 2:
        print("Your Electricity Bill is:", bill)

    elif choice == 3:
        if bill > 0:
            print("Bill Paid Successfully")
            bill = 0
        else:
            print("No bill to pay")

    elif choice == 4:
        print("Thank you!")
        break

    else:
        print("Invalid choice")
