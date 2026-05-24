n = int(input("Enter number: "))
factor = 2
while n >1:
    if n % factor== 0:
        print(factor, end=" ")
        n = n//factor
    else:
        factor = factor + 1
