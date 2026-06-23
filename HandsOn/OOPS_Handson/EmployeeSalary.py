class Employee:
    def getInfo(self,s,h):
        self.s=s
        self.h=h
    def AddSal(self):
        if self.s<500:
            self.s+=10
    def AddWork(self):
        if self.h>6:
            self.s+=5

s = float(input("Enter salary : "))
h = int(input("Enter working hours : "))
e = Employee()
e.getInfo(s,h)
e.AddSal()
e.AddWork()
print("Final salary :",e.s)
