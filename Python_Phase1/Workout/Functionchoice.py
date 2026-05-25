def circle(radius):
    print("Circle Area :", 3.14 * radius * radius)
def rectangle(length, breadth):
    print("Rectangle Area :", length * breadth)
def square(side):
    print("Square Area :", side * side)
def triangle(len,bre):
    print("Triangle : ",1.2*len*bre)
while True:
    print("1 - Circle")
    print("2 - Rectangle")
    print("3 - Square")
    print("4 - triangle")
    print("5 - Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        radius = int(input("Enter the radius: "))
        circle(radius)
    elif choice == 2:
        length = int(input("Enter length: "))
        breadth = int(input("Enter breadth: "))
        rectangle(length, breadth)
    elif choice == 3:
        side = int(input("Enter the side: "))
        square(side)
    elif choice ==4:
        tri = int(input("enter the length : "))
        bredth = int(input("Enter breadth"))
        triangle(tri,bredth)
    elif choice == 5:
        print("Program exited")
        break
    else:
        print("Enter valid choice")
        
    