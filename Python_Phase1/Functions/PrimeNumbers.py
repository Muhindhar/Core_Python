def prime(number):
    if number<=1:
        print("Not a prime")
    for i in range(2,number):
        if number%i==0:
            print("Not a Prime number ")
            return   
    print("prime")
n = int(input("enter a number : "))
prime(n)
