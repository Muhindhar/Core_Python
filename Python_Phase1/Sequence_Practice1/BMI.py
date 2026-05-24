weight = float(input("Enter your weight : "))
height = float(input("ENter your height : "))
if(weight>0 and height>0):
    print("BMI : ",round(weight/(height*height),2))
else:
    print("Invalid height and weight")
