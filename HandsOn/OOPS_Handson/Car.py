class Vehicle:
    def __init__(self,b,y):
        self.brand=b
        self.year=y
    def displayInfo(self):
        print("Brand :",self.brand)
        print("Year :",self.year)

class Car(Vehicle):
    def __init__(self,b,y,m):
        super().__init__(b,y)
        self.model=m
    def displayCarInfo(self):
        print("Brand :",self.brand)
        print("Model :",self.model)
        print("Year :",self.year)

b = input("Enter brand : ")
y = int(input("Enter year : "))
m = input("Enter model : ")
c = Car(b,y,m)
c.displayInfo()
c.displayCarInfo()
