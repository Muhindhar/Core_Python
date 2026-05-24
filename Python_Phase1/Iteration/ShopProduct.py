price = int(input("Enter price: "))
minimum = 101
maximum = 0
total = 0
count = 0
while price != -1:
    if price < minimum:
        minimum = price
    if price > maximum:
        maximum = price
    if price >= 5 and price <= 30:
        total = total + price
        count = count + 1
    price = int(input("Enter price: "))
average = total // count
print(maximum, minimum, average)
