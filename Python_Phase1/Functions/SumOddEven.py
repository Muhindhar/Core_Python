def sum_even_odd(numbers):
    even = odd = 0
    for i in numbers:
        if i % 2 == 0:
            even += i
        else:
            odd += i
    print("Sum of Even Numbers :", even)
    print("Sum of Odd Numbers  :", odd)
nums = [1,4,5,7,3,9]
sum_even_odd(nums)