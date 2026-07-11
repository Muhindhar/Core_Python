def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def calc(oper,a,b):
    return oper(a,b)

op = input("Enter the option : ")
aa = int(input("Enter the 1st number :"))
bb = int(input("Enter the 2ns number : "))
if op == "add":
    result=calc(add,aa,bb)
    print(result)
elif op == "sub":
    result=calc(sub,aa,bb)
    print(result)
elif op=="mul":
    result=calc(mul,aa,bb)
    print(result)
else:
    print("Invalid")
    

