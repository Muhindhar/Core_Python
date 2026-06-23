def salary(oldsal,hike):
    newsal = oldsal+(oldsal*hike/100)
    print("New salary : ",newsal)

hikes = float(input("Enter the hike percentage : "))
old = float(input("enter old salary : "))
salary(old,hikes)
