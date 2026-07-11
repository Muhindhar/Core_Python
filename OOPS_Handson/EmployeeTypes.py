from abc import ABC,abstractmethod

class Employee(ABC):
    def __init__(self,i,n):
        self.employeeID=i
        self.name=n
    def displayInfo(self):
        print("Employee ID :",self.employeeID)
        print("Name :",self.name)
    @abstractmethod
    def calculateSalary(self):
        pass

class FullTimeEmployee(Employee):
    def __init__(self,i,n,s):
        super().__init__(i,n)
        self.salary=s
    def calculateSalary(self):
        return self.salary

class PartTimeEmployee(Employee):
    def __init__(self,i,n,r,h):
        super().__init__(i,n)
        self.hourlyRate=r
        self.hoursWorked=h
    def calculateSalary(self):
        return self.hourlyRate*self.hoursWorked

class ContractEmployee(Employee):
    def __init__(self,i,n,d,p):
        super().__init__(i,n)
        self.contractDuration=d
        self.pay=p
    def calculateSalary(self):
        return self.contractDuration*self.pay

e1 = FullTimeEmployee(1,"Arun",30000)
e2 = PartTimeEmployee(2,"Bala",200,80)
e3 = ContractEmployee(3,"Charan",6,25000)
for e in [e1,e2,e3]:
    e.displayInfo()
    print("Salary :",e.calculateSalary())
