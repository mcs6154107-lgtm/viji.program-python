import re

def check_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[0-9]", password):
        score += 1
    if re.search(r"[^A-Za-z0-9]", password):
        score += 1

    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    else:
        return "Strong"


def encrypt(password):
    encrypted = ""

    for char in password:
        encrypted += chr((ord(char) + 3) % 256)

    return encrypted


password = input("Enter your password: ")

strength = check_strength(password)
print("Password Strength:", strength)

if strength == "Weak":
    print("Password is too weak.")
else:
    encrypted_password = encrypt(password)

    with open("passwords.txt", "a") as file:
        file.write(encrypted_password + "\n")

    print("Encrypted password saved successfully.")
