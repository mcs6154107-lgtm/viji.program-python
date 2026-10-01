import re

def validate_password(password):
    errors = []

    if len(password) < 8:
        errors.append("At least 8 characters are required.")

    if not re.search(r"[A-Z]", password):
        errors.append("At least one uppercase letter is required.")

    if not re.search(r"[a-z]", password):
        errors.append("At least one lowercase letter is required.")

    if not re.search(r"[0-9]", password):
        errors.append("At least one number is required.")

    if not re.search(r"[@#$%!&*]", password):
        errors.append("At least one special character is required.")

    return errors


def xor_encrypt(password, key=25):
    encrypted = []

    for char in password:
        encrypted.append(ord(char) ^ key)

    return " ".join(map(str, encrypted))


password = input("Enter your password: ")

errors = validate_password(password)

if errors:
    print("\nPassword validation failed:")
    for error in errors:
        print("-", error)
else:
    encrypted = xor_encrypt(password)

    with open("encrypted_passwords.txt", "a") as file:
        file.write(encrypted + "\n")

    print("\nPassword is valid.")
    print("Encrypted password:", encrypted)
    print("Data saved to encrypted_passwords.txt")
