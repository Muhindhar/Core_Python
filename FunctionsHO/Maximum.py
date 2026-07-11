def findMax(*numbers):
    max_value = numbers[0]
    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value
max1 = findMax(25, 12, 18, 30)
max2 = findMax(8, 15, 22, 17, 12)
print("maximum value among four integers:", max1)
print("maximum value among five integers:", max2)