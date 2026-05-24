total = int(input("Enter total animals : "))
rabbit = int(input("Enter rabbit count : "))
deer = int(input("Enter deer count : "))
birds = int(input("Enter birds count : "))
squirrels = int(input("Enter squirrels count : "))
sum = rabbit + deer + birds + squirrels
if total == sum + 1:
    print("Baby lion is mischievous")
elif total == sum:
    print("Baby lion is well behaved")
else:
    print("Counted wrongly")
