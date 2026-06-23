import re

def validate_username(u):
    if re.fullmatch(r"[A-Za-z0-9]{5,15}",u):
        return "Valid"
    return "Invalid"

u = input("Enter username : ")
print(validate_username(u))
