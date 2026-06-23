import re

def extract_dates(t):
    return re.findall(r"\b\d{2}/\d{2}/\d{4}\b",t)

t = input("Enter text : ")
print(extract_dates(t))
