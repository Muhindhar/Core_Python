num = int(input("Enter number: "))
temp = num
count = len(str(num))
total = 0

while temp > 0:
    digit = temp % 10
    total = total + digit ** count
    temp = temp // 10

if total == num:
    print("true")
else:
    print("false")
