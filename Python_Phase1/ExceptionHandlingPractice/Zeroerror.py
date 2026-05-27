try:
    a = int(input("enter a "))
    b = int(input("enter b "))
    res = a/b
    print(res)
except(ZeroDivisionError):
    print("Cannot divide by zero")
except(NameError):
    print("Give the integer")
else:
    print("success")
finally:
    print("Final block executed")
