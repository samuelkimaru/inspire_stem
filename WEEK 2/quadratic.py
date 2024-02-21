#program to solve quadratic equation
# date : 20/2/2024
# name : muchiri
a = float(input("enter the coeficient of fist term : "))
b = float(input("enter the coeficient of second term : "))
c = float(input("enter constant : "))
import math

d =(b**2) - 4 * a * c

x_1 = (-b + math.sqrt(d)  ) / 2* a
x_2 = (-b - math.sqrt(d)  ) / 2* a
print("the solution of the quadratic equation is : ",x_1)
print("the solution of the quadratic equation is : ",x_1)
