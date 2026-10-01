import hashlib
import re

def check_password(password):
    if len(password) < 8:
        return False

    if not re.search(r"[A-Z]", password):
        return False

    if not re.search(r"[a-z]", password):
        return False

    if not re.search(r"[0-9]", password):
        return False

    if not re.search(r"[^A-Za-z0-9]", password):
        return False

    return True


def hash_password(password):
    return hashlib.sha256(
        password.encode("utf-8")
    ).hexdigest()


username = input("Enter username: ")
password = input("Enter password: ")

if check_password(password):

    hashed_password = hash_password(password)

    with open("password_database.txt", "a") as file:
        file.write(f"{username}:{hashed_password}\n")

    print("\nPassword accepted.")
    print("SHA-256 hash:", hashed_password)
    print("Hash saved successfully.")

else:
    print("\nPassword rejected.")
    print("Password must contain:")
    print("1. At least 8 characters")
    print("2. Uppercase letter")
    print("3. Lowercase letter")
    print("4. Number")
    print("5. Special character")
