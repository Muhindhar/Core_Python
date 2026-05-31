class myclass:
    def __init__(self, *args):
        if len(args) == 0:
            self.radius = 1.0
            self.color = "yellow"
        elif len(args) == 1:
            self.radius = args[0]
            self.color = "yellow"
        elif len(args) == 2:
            self.radius = args[0]
            self.color = args[1]
    def getrad(self):
        return self.radius
    def getcolor(self):
        return self.color
obj1 = myclass()
obj2 = myclass(2.5)
obj3 = myclass(3.5, "red")
print(obj1.getrad(), obj1.getcolor())
print(obj2.getrad(), obj2.getcolor())
print(obj3.getrad(), obj3.getcolor())