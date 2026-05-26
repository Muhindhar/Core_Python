str1 = input("Enter the string : ")
low =""
up=""
for ch in str1:
    if ch.islower():
        low+=ch
    else:
        up+=ch
print(low+up)