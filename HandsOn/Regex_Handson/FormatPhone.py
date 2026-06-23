import re

def format_phone_number(n):
    n = re.sub(r"\D","",n)
    m = re.fullmatch(r"(\d{3})(\d{3})(\d{4})",n)
    if m:
        return "+1-"+m.group(1)+"-"+m.group(2)+"-"+m.group(3)
    return "Invalid number"

n = input("Enter phone number : ")
print(format_phone_number(n))
