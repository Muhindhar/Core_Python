import re
pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
email = "contact us at muhindharsv27@gmail.com"
res = re.findall(pattern,email)
if res:
    print("Email found : ",res)
else:
    print("Not found")