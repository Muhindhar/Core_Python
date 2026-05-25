l = int(input("Enter the lower limit"))
u = int(input("Enter the upper limit"))
print("The prime number between L and U are :")
for num in range(l, u + 1):
    if num >= 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
            else:
                print(num)