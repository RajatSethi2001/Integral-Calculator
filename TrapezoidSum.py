#Integral Calculator
from math import *

upbound = 1
lowbound = 0
rectAmount = 100

function = input("Enter a function: ")
function = function.replace('^', '**')

upbound = eval(input("Enter the upper bound: "))
lowbound = eval(input("Enter the lower bound: "))
rectAmount = eval(input("Enter the trapezoid amount: "))

difference = (upbound - lowbound) / rectAmount

rects = [lowbound]

while (lowbound < upbound):
    rects.append(lowbound + difference)
    lowbound += difference
    
s = 0
x = rects[0]
s += eval(function)
x = rects[(len(rects) - 1)]
s += eval(function)

for i in range(1, len(rects) - 1):
    x = rects[i]
    s += (2 * eval(function))

s = s * difference / 2
print("The integral value is approximately: " + str(s))


