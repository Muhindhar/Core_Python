class num:
    def __init__(self):
        self.x = 20
        self.y = 30
    def  addnum(self):
     self.z = self.x + self.y
     print("Sum : ",self.z)
     
class sub(num):
    def __init__(self):
       self.x = 20
       self.y = 30
       
    def  subnum(self):
         self.z = self.x - self.y
         print("Sum : ",self.z)

obj2 = sub()
obj2.addnum()
obj2.subnum()