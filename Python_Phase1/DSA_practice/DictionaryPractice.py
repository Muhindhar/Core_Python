mydict = {}
print(type(mydict))
mydict={1:"cse",'name':'Muhindhar','list':[1,3,5],'tuple':(3,4,"muhi")}
print(mydict)
print(type(mydict['name']))

#using keyword
num = dict(x=5,y=0)
print(type(num))
print(num)

#mapping
numbers = dict({'x':4,'y':8})
print(type(numbers))
print(numbers)

#using iterable
numq = dict([('x',5),('y',8)])
print(type(numq['x']))
print(numq)

#nested dictionary
Mycars = {{"child1":{"name":"muhi","year":2005}},{"child2":{"name":"sv","year":7553}}}
print(Mycars)

#indexing dictionary
dict={'name':'muhu','age':20,'year':2005}
print(dict['age'])

#addingelement in dict
diction={"name":"muhi","age":20}
print(diction)
diction['colour']=['yellow']
print(diction)

#ex
diction={"name":"muhi","age":20}
for x in diction:
    print(x,diction[x])
    
#update dict
d={1:"one",2:"three"}
d1={2:"two"}
d.update(d1)
print(d)

#dictionary pair
square={}
for x in range(5):
    square[x]=x*x 
print(square)