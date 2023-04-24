import cmath
import math

a = int(input("What is a?"))
b = int(input("What is b?"))
c = int(input("What is c?"))

d = (b**2)-(4*a*c)

x1 = (-b-cmath.sqrt(d))/(2*a)
x2 = (-b+cmath.sqrt(d))/(2*a)

print(f"The first solution to the given quadratic equation are x1: {x1} and x2: {x2}")