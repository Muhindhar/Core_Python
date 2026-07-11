def set_comprehension(n):
    return {i*i for i in range(1, n+1)}
n = int(input("Enter the count : "))
print(set_comprehension(n))