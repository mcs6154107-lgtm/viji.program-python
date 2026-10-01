import re

def validate_password(password):
    return (
        len(password) >= 8 and
        re.search(r"[A-Z]", password) and
        re.search(r"[a-z]", password) and
        re.search(r"[0-9]", password) and
        re.search(r"[^A-Za-z0-9]", password)
    )


def vigenere_encrypt(text, key):
    result = ""
    key_index = 0

    for char in text:
        shift = ord(key[key_index % len(key)])

        encrypted_char = chr((ord(char) + shift) % 256)
        result += encrypted_char

        key_index += 1

    return result


password = input("Enter password: ")

if validate_password(password):
    key = input("Enter encryption key: ")

    if not key:
        print("Encryption key cannot be empty.")
    else:
        encrypted = vigenere_encrypt(password, key)

        with open("secure_data.txt", "a") as file:
            file.write(encrypted + "\n")

        print("Password is valid.")
        print("Encrypted password:", encrypted)
        print("Saved successfully.")

else:
    print("Invalid password.")
    print("Password must contain:")
    print("- At least 8 characters")
    print("- Uppercase letter")
    print("- Lowercase letter")
    print("- Number")
    print("- Special character")
