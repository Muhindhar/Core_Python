name = str(input("Enter the string : "))
dig=0
alpha=0

for i in name:
    if i.isnumeric():
        dig+=1
    elif i.isalpha():
        alpha+=1
    else:
        pass
print("Digits : ",dig)
print("Alphabets : ",alpha)