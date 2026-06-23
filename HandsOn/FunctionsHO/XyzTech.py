def increment(salary,rating):
    if rating>1 and rating<4:
        print("Salary : ",salary*0.10+salary)
    elif rating>4.1 and rating<7:
        print("Salary : ",salary*0.25+salary)
    elif rating>=7 and rating<=10:
        print("Salary : ",salary*0.30+salary)
    else:
        print("No increment")

sal = int(input("enter the salary : "))
rate = float(input("Enter the rating : "))
increment(sal,rate)