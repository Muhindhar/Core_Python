class student:
    def __init__(self):
        self.name = "Muhi"
        self.__age = 21
        self._dept = "ece"
    def dispage(self):
        return self.__age
obj = student()
print(obj.name)
print(obj.dispage())
print(obj._dept)