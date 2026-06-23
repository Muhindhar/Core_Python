wrd = input("Enter the sentence : ")
lc=0
upc=0
nonl=0
for i in wrd:
    if i.islower():
        lc+=1
    elif i.isupper():
        upc+=1
    else:
        nonl+=1
print("Lower case: ",lc)
print("upper case : ",upc)
print("Non letters : ",nonl)
