import math

class Circle:
    def __init__(self,r=1.0,c="red"):
        self.__radius=r
        self.__color=c
    def getRadius(self):
        return self.__radius
    def getColor(self):
        return self.__color
    def setRadius(self,r):
        self.__radius=r
    def setColor(self,c):
        self.__color=c
    def toString(self):
        return f"Circle[radius={self.__radius},color={self.__color}]"
    def getArea(self):
        return math.pi*self.__radius*self.__radius

c1 = Circle()
c2 = Circle(2.0)
c3 = Circle(3.0,"blue")
c1.setRadius(4.0)
c1.setColor("green")
print(c1.getRadius())
print(c1.getColor())
print(c1.toString())
print(c2.toString())
print(c3.toString())
print(c3.getArea())
