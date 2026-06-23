import re

def extract_hashtags(t):
    return re.findall(r"#[A-Za-z0-9_]+",t)

t = input("Enter text : ")
print(extract_hashtags(t))
