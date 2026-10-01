total = 0

while True:
    print("\n===== SHOPPING MENU =====")
    print("1. Add Item")
    print("2. Show Total")
    print("3. Apply Discount")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        price = float(input("Enter item price: "))

        if price > 0:
            total += price
            print("Item added successfully")
        else:
            print("Invalid price")

    elif choice == 2:
        print("Total Amount:", total)

    elif choice == 3:
        if total > 1000:
            discount = total * 0.10
            total -= discount
            print("10% discount applied")
            print("New Total:", total)
        else:
            print("No discount available")

    elif choice == 4:
        print("Thank you for shopping!")
        break

    else:
        print("Invalid choice")

