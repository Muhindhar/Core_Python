months = int(input("Enter month number: "))
year = int(input("Enter year: "))
if months == 1:
    month = "January"
    days = 31
elif months == 2:
    month = "February"
    if year % 400 == 0 or (year%4==0 and year%100!=0):
        days = 29
    else:
        days= 28
elif months ==3:
    month="March"
    days =31
elif months==4:
    month = "April"
    days = 30
elif months == 5:
    month = "May"
    days = 31
elif months == 6:
    month = "June"
    days = 30
elif months == 7:
    month = "July"
    days = 31
elif months == 8:
    month = "August"
    days = 31
elif months == 9:
    month = "September"
    days = 30
elif months == 10:
    month = "October"
    days = 31
elif months == 11:
    month = "November"
    days = 30
elif months == 12:
    month = "December"
    days = 31
else:
    month = ""
    days = 0
if days == 0:
    print("Invalid month")
else:
    print(month, year,"has",days,"days")
