import random
import string

n = int(input("Enter password length : "))
s = string.ascii_letters+string.digits+string.punctuation
p = ""
if n>=3:
    p+=random.choice(string.ascii_letters)
    p+=random.choice(string.digits)
    p+=random.choice(string.punctuation)
for i in range(n-len(p)):
    p+=random.choice(s)
p = list(p)
random.shuffle(p)
p = "".join(p)
print("Generated password :",p)
