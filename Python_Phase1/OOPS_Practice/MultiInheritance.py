class student:
    def getinfo(self):
        self.__rollno = input("Enter the roll number : ")
        self.__name = input("Enter the name of the student : ")

    def printinfo(self):
        print("Roll number : ", self.__rollno)
        print("Name : ", self.__name)


class marks(student):
    def getmark(self):
        self.getinfo()

        self.__mark1 = float(input("Enter the mark1 : "))
        self.__mark2 = float(input("Enter the mark2 : "))
        self.__mark3 = float(input("Enter the mark3 : "))

    def printmark(self):
        self.printinfo()
        print("Mark1 : ", self.__mark1)
        print("Mark2 : ", self.__mark2)
        print("Mark3 : ", self.__mark3)
    def tot(self):
        total = self.__mark1 + self.__mark2 + self.__mark3
        return total
class res(marks):
    def getresult(self):
        self.getmark()
    def putres(self):
        self.printmark()
        print("Total marks out of 300 :", self.tot())
obj = res()
obj.getresult()
obj.putres()