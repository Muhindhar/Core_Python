class Triangle:
    def __init__(self):
        self.a=3
        self.b=4
        self.c=5
    def area(self):
        s=(self.a+self.b+self.c)/2
        return (s*(s-self.a)*(s-self.b)*(s-self.c))**0.5
    def perimeter(self):
        return self.a+self.b+self.c

t = Triangle()
print("Area :",t.area())
print("Perimeter :",t.perimeter())
