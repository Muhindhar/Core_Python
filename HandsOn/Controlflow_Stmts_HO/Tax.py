income = int(input("Enter income: "))
if income<=250000:
    print("You are exempted from tax")
elif income<=500000:
    tax=(income-250000)*10/100
    print("Tax amount is", int(tax))
elif income<=1200000:
    tax=25000 + (income - 500000) * 20 / 100
    print(int(tax))
else:
    tax=25000 + 140000 + (income - 1200000) * 30 / 100
    print(int(tax))
