class Student:
    def __init__(self,i=0,n="Unknown",a=0,g="Unknown"):
        self.id=i
        self.name=n
        self.age=a
        self.grade=g
    def display(self):
        print(self.id,self.name,self.age,self.grade)

s1 = Student()
i = int(input("Enter student id : "))
n = input("Enter student name : ")
a = int(input("Enter student age : "))
g = input("Enter student grade : ")
s2 = Student(i,n,a,g)
s1.display()
s2.display()
