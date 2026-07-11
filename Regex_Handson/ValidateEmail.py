import re

def validate_email(e):
    p = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
    return bool(re.fullmatch(p,e))

e = input("Enter email : ")
print(validate_email(e))
