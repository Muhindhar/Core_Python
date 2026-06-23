name = input("enter the name")
count = int(input("Enter no of item"))
if(count>=10 and count<=99):
    print(name,count*10)
elif(count>=100):
    print(name,count*7)
elif(count<10):
    print(name,count*12)
else:
    print("Invalid")