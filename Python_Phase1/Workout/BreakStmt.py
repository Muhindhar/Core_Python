n = int(input("Enter the number : "))
i = 1
sum = 0
while i < n:
    n = int(input("Enter the number : "))
    if n == 1:
        break
    else:
        sum += 1
    i += 1
    print(sum)
