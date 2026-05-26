mytup = (12,3.14,"ram",[1,2,3])
print(type(mytup[3][2]))

#edit/modify
t=(10,30,20,40)
print(id(t))
t=(100,)+t[1:]
print(t)
print(id(t))

#expression
a,b = 2+1,2+3
res=(a,b)
print(type(res))

#user,domain
addr = "muhi@gmail.com"
uname,dom = addr.split("@")
print(f"username : {uname} and domain : {dom}")

#quotient/rem
quo,rem = divmod(7,3)
print(quo,rem)

#swap
a=10
b=20
a=a+b
b=a-b
a=a-b
print(a,b)