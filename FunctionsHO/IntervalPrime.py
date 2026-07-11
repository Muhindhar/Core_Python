def prime(a,b):
    for i in range(a,b+1):
        if i > 1:
            for num in range(2,i):
             if i%num==0:
                break
            else:
                print(i)
        
start = int(input("enter the starting number"))
end = int(input("enter the ending range : " ))
prime(start,end)
