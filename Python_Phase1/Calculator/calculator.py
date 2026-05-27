'''import addition 
import subtraction 
import multi 
import division'''

from Calculation.addition import add
from Calculation.subtraction import sub
from Calculation.division import div
from Calculation.multi import multi 

'''from addition import add
from subtraction import sub
from division import div
from multi import multi'''

print("Addition : ",add(2,3))
print("Subtraction : ",sub(5,3))
print("Multiplication : ",multi(3,4))
print("Division : ",div(4,8))