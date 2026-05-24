import math
radius = float(input("Enter the radius of the circle: "))
angle = float(input("Enter the angle in degrees (for sector area): "))
if radius <= 0:
    print("Invalid radius")
elif angle < 0 or angle > 360:
    print("Invalid angle")
else:
    diameter = 2 * radius
    circumference = 2 * math.pi * radius
    area = (angle / 360) * math.pi * radius * radius
    arclength = (angle / 360) * circumference
    print("Radius:", radius)
    print("Diameter:", diameter)
    print("Circumference:", circumference)
    print("Sector Area for", angle, "degrees:", area)
    print("Arc Length for", angle, "degrees:", arclength)
