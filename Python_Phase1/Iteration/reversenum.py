m = int(input("Enter number to reverse : "))
if len(str(m)) > 4:
    rev = 0
    while m > 0:
        digit = m % 10
        rev = rev * 10 + digit
        m = m // 10
    print(rev)
else:
    print("Not a valid number")