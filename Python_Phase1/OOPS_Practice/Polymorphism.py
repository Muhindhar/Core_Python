class vehicle:
    def __init__(self,name,color,price):
        self.name  = name
        self.color = color
        self.price = price
    def show(self):
        print("Details : ",self.name,self.color,self.price)
    def maxspeed(self):
        print("Maximum speed is 100km/hr")
    def changegear(self):
        print("Gear changned to 5th")

class car(vehicle):
    def maxspeed(self):
        return super().maxspeed()
        print("Car maximum speed in 120 km/hr")
    def changegear(self):
        return super().changegear()
        print("Car gear changed to 6th")

Car = car("BMW","black",200000)
Car.show()
Car.maxspeed()
Car.changegear()

Vehicle = vehicle("Kia","Red",876552)
Vehicle.show()
Vehicle.maxspeed()
Vehicle.changegear()