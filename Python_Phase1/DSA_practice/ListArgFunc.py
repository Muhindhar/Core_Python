def inc(list2):
    for i in range(0,len(list2)):
        list2[i]+=5
    print("reference function : ",id(list2))
    
list1 = [10,20,30,40,50]
print("refernce of list in main",id(list1))
print("the list before call")
print(list1)


inc(list1)
print("after func call")
print(list1)