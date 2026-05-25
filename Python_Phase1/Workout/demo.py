#number
num = 10
print(type(num),num)
#String
name = "muhindhar"
print(type(name),name);
#float
numberf = 11.2;
print(type(numberf),numberf)
check = True
print(type(check),check)
com = 4+3j
print(type(com),com)
listex = [12,"muhi",1.3,]
print(type(listex[1]))
print(type(listex),listex)
#tuples
tuples = (10,20,30)
print(type(tuples),type(tuples[1]))
#sets
sets = {10,"khds",1.2}
t = 10
for x in sets:
    if(x==t):
        print(x)
print(type(sets))
#none
myvar = None
print(type(myvar))

#dictionary
student = {"name":"muhi","age":21,"gender":"male"}
print(student)
print(type(student))
#access from dict
print(student['name'])

#Literals
x = (1==True)
y = (1==True)
res = True+4
print(res)
ans = (False+10)
print(ans)

#Identity - Is
num1 = 5
num2 = num1
print(type(num1) is not int)
print(type(num2) is not int)

#In
a=[1,2,3]
print(4 in a)