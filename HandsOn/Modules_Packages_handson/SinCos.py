from math import sin,cos

n = int(input("Enter degree : "))
r = n*3.14159/180
print("sin(",n,") =",round(sin(r),1))
print("cos(",n,") =",round(cos(r),1))
