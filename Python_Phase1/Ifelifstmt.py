mark = int(input("Enter the mark"))
if mark>90:
    print("Grade : O")
elif mark>81 and mark<90:
    print("Grade : A")
elif mark>71 and mark<80:
    print("Grade : B")
elif mark>61 and mark<70:
    print("Grade : C")
elif mark>50 and mark<60:
    print("Grade : D")
else:
    print("Grade F")