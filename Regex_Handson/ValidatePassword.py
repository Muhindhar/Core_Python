import re

def validate_password(p):
    x = r"(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*]).{8,}"
    return bool(re.fullmatch(x,p))

p = input("Enter password : ")
print(validate_password(p))
