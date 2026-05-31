class myclass:
    def __init__(self,radius=1.0,color="yellow"):
        self.radius = radius
        self.color = color
    @classmethod
    def withradius(cls,radius):
        return cls(radius)
    @classmethod
    def withcolor(cls,color):
        return cls(color=color)
    @classmethod
    def withradandcol(cls,radius,color):
        return cls(radius,color)
    def getrad(self):
        return self.radius
    def getcolor(self):
        return self.color
    
obj = myclass()
r=(myclass.withradius(2.3))
c=(myclass.withcolor("red"))
print(r.getrad())
print(c.getcolor())
    
        