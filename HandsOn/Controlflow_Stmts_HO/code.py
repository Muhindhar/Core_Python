code = int(input("enter the code"))
if(code==1):
    a = float(input("enter 1st number : "))
    b = float(input("enter 2nd number : "))
    print(a+b)
elif code==2:
     a = float(input("enter 1st number : "))
     b = float(input("enter 2nd number : "))
     print(a*b)
elif code ==3:
     a = str(input("enter 1st str : "))
     b = str(input("enter 2nd str : "))
     print(a+b)
else:
    print("invalid")