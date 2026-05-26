list1 = []
while True:
    print("1.Append element ")
    print("2.Insert")
    print("3.Append list to given list")
    print("4.Modify existing list")
    print("5.Delete an existing element from its pos")
    print("6.Delete an existing element with given value")
    print("7.Sort the list in ascending")
    print("8.Sort list in descending")
    print("9.Display the list")
    choice=int(input("Enter the choice : "))
    if choice==1:
        ele=input("Enter the element : ")
        list1.append(ele)
    elif choice==2:
        pos=int(input("Enter the position : "))
        ele=input("Enter the element : ")
        list1.insert(pos, ele)
    elif choice==3:
        newlist =input("Enter elements separated by space : ").split()
        list1.extend(newlist)
    elif choice== 4:
        pos =int(input("Enter position : "))
        ele = input("Enter the element : ")
        list1[pos] = ele
    elif choice == 5:
        pos =int(input("Enter the position to delete : "))
        list1.pop(pos)
    elif choice== 6:
        rem = input("Enter the element to remove : ")
        list1.remove(rem)
    elif choice==7:
        list1.sort()
        print("Ascending :", list1)
    elif choice==8:
        list1.sort(reverse=True)
        print("Descending :", list1)
    elif choice==9:
        print("List :", list1)
    else:
        print("Invalid choice")