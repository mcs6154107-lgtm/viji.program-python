balance = 5000

while True:
    print("\n===== BANK MENU =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Current Balance:", balance)

    elif choice == 2:
        amount = float(input("Enter deposit amount: "))

        if amount > 0:
            balance += amount
            print("Money deposited successfully")
        else:
            print("Invalid amount")

    elif choice == 3:
        amount = float(input("Enter withdrawal amount: "))

        if amount > 0 and amount <= balance:
            balance -= amount
            print("Money withdrawn successfully")
        elif amount > balance:
            print("Insufficient balance")
        else:
            print("Invalid amount")

    elif choice == 4:
        print("Thank you for using the bank")
        break

    else:
        print("Invalid choice")
