class student:
    def __init__(self,name,age):
        self.name= name
        self.__age = age
    def getage(self):
        return self.__age
    def setage(self,age):
        self.age = self.__age
        
    def getname(self):
        return self.name
    def setname(self,name):
        self.name = self.name
stud = student("Muhindhar",21)
print("Name: ",stud.name,"Age: ",stud.getage())

stud.setage(22)
print("Name: ",stud.name,"Age: ",stud.getage())
