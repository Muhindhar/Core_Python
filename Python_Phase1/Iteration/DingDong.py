start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

for num in range(start, end + 1):
    if num % 10 == 0:
        print("dong", end=" ")
    elif num % 5 == 0:
        print("ding", end=" ")
    else:
        print(num, end=" ")
