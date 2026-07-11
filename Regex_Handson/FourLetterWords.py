import re

def extract_words(t):
    return re.findall(r"\b[A-Za-z]{4}\b",t)

t = input("Enter text : ")
print(extract_words(t))
