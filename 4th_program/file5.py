import json

contacts = []

try:
    with open("contacts.txt", "r") as file:
        contacts = json.load(file)
except FileNotFoundError:
    contacts = []


while True:

    print("\n===== CONTACT MANAGEMENT =====")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. View Contacts")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        name = input("Enter name: ")
        phone = input("Enter phone: ")
        email = input("Enter email: ")

        contact = {
            "name": name,
            "phone": phone,
            "email": email
        }

        contacts.append(contact)

        with open("contacts.txt", "w") as file:
            json.dump(contacts, file, indent=4)

        print("Contact saved.")

    elif choice == "2":

        name = input("Enter name: ")

        found = False

        for contact in contacts:
            if contact["name"].lower() == name.lower():

                print("\nContact Details")
                print("Name:", contact["name"])
                print("Phone:", contact["phone"])
                print("Email:", contact["email"])

                found = True

        if not found:
            print("Contact not found.")

    elif choice == "3":

        phone = input("Enter phone number: ")

        for contact in contacts:

            if contact["phone"] == phone:

                contacts.remove(contact)

                with open("contacts.txt", "w") as file:
                    json.dump(contacts, file, indent=4)

                print("Contact deleted.")
                break

        else:
            print("Contact not found.")

    elif choice == "4":

        print("\n--- ALL CONTACTS ---")

        if len(contacts) == 0:
            print("No contacts available.")

        for contact in contacts:
            print(
                contact["name"],
                "|",
                contact["phone"],
                "|",
                contact["email"]
            )

    elif choice == "5":

        print("Thank you!")
        break

    else:
        print("Invalid choice!")
