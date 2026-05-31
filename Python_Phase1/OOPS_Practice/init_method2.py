class circle:
    def __init__(self, radius=1.0, color="red"):
        self.radius = radius
        self.color = color
    def getradius(self):
        return self.radius
    def getcolor(self):
        return self.color
    def setradius(self, radius):
        self.radius = radius
    def setcolor(self, color):
        self.color = color
    def getarea(self):
        return 3.14159 * self.radius * self.radius
    def __str__(self):
        return f"Circle[radius={self.radius}, colour={self.color}]"
circle1 = circle()
print(circle1)
circle2 = circle(2.5)
print(circle2)
circle3 = circle(3.5, "blue")
print(circle3)
