class Area:
    def setDim(self,l,b):
        self.l=l
        self.b=b
    def getArea(self):
        return self.l*self.b

l = int(input("Enter length : "))
b = int(input("Enter breadth : "))
a = Area()
a.setDim(l,b)
print("Area :",a.getArea())
