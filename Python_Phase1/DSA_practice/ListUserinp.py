#normal way
lista=[]
n = int(input("Enter the number of elements : "))
for i in range(0,n):
    print("Emter element : {}: ".format(i+1))
    elm=int(input())
    lista.append(elm)
print("the entered list is : ",lista)

#split function and getting inp from user
lista=[] 
n = int(input("Enter the number of elements : "))
lista = input("Enter the elements by comma : ").split(',')
print(lista)

#by using maps(int-key,inp=value)
t=list(map(int,input("Enter the value by space : ").split()))
print(t)