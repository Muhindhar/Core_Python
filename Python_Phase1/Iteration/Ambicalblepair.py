x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
sumx = 0
sumy = 0
for i in range(1, x):
    if x % i == 0:
        sumx = sumx + i
for i in range(1, y):
    if y % i == 0:
        sumy = sumy + i

if sumx == y and sumy == x:
    print("true")
else:
    print("false")
