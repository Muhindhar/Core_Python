import re

def extract_numbers(t):
    return re.findall(r"\d+(?:\.\d+)?",t)

t = input("Enter text : ")
print(extract_numbers(t))
