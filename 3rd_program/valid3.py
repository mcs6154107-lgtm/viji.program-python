import base64
import string

def password_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1

    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    else:
        return "Strong"


def encode_password(password):
    data = password.encode("utf-8")
    return base64.b64encode(data).decode("utf-8")


username = input("Enter username: ")
password = input("Enter password: ")

strength = password_strength(password)

print("Password Strength:", strength)

if strength == "Strong":
    encoded = encode_password(password)

    with open("users.txt", "a") as file:
        file.write(f"{username}:{encoded}\n")

    print("User information saved successfully.")
else:
    print("Please choose a stronger password.")
