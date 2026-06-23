from abc import ABC,abstractmethod
import math

class IShape(ABC):
    @abstractmethod
    def CalculateArea(self):
        pass
    @abstractmethod
    def CalculatePerimeter(self):
        pass

class Rectangle(IShape):
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def CalculateArea(self):
        return self.l*self.b
    def CalculatePerimeter(self):
        return 2*(self.l+self.b)

class Circle(IShape):
    def __init__(self,r):
        self.r=r
    def CalculateArea(self):
        return math.pi*self.r*self.r
    def CalculatePerimeter(self):
        return 2*math.pi*self.r

l = float(input("Enter length : "))
b = float(input("Enter breadth : "))
r = float(input("Enter radius : "))
s1 = Rectangle(l,b)
s2 = Circle(r)
print("Rectangle area :",s1.CalculateArea())
print("Rectangle perimeter :",s1.CalculatePerimeter())
print("Circle area :",s2.CalculateArea())
print("Circle perimeter :",s2.CalculatePerimeter())
