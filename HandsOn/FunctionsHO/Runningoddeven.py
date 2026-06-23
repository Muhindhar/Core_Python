def runningodd(lb,ub):
    odd=0
    for i in range(lb,ub+1):
        if i%2!=0:
            odd+=i
    return odd
def runningeven(lb,ub):
    even=0
    for i in range(lb,ub+1):
        if i%2==0:
            even+=i
    return even
        
lb = int(input("Enter lower bound : "))
ub = int(input("Enter the upper bound :"))
evensum = runningeven(lb, ub)
oddsum = runningodd(lb, ub)
diff= abs(evensum-oddsum)
print("Sum of even numbers : ",evensum)
print("Sum of odd numbers : ",oddsum)
print("Absolute difference between is : ",diff)