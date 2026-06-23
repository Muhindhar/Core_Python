age = int(input("Enter the age"))
if age>0 and age<=10:
    print(" Cartoon Club")
elif age>=11 and age<=20:
    print("Teens Club")
elif age>20:
    print("Not Allowed")
else:
    print("Invalid Age")