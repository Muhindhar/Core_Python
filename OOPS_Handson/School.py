class School:
    totalStudents=0
    MAX_CAPACITY=500
    def enrollStudent(self):
        if School.totalStudents<School.MAX_CAPACITY:
            School.totalStudents+=1
    def getTotalStudents(self):
        return School.totalStudents

n = int(input("Enter number of students : "))
s = School()
for i in range(n):
    s.enrollStudent()
print("Total students :",s.getTotalStudents())
print("Maximum capacity :",School.MAX_CAPACITY)
