# 1. Write a Python program to convert degree to radian. Input degree: 15. Output radian: 0.261904
import math

#n = float(input("Degree: "))
def mat(n):
    radians = n * (math.pi/180)
    return radians
print("Radians: ", mat(15))

# 2.Write a Python program to calculate the area of a trapezoid. Height: 5; Base, first value: 5; Base, second value: 6; Expected Output: 27.5 
"""import math

h = float(input("Height: "))
a = float(input("Base a: "))
b = float(input("Base b: "))

def area(h, a, b):
    return h / 2*(a+b)
print("Area of trapezoid: ", area(h, a, b))
"""

# 3. Write a Python program to calculate the area of regular polygon. Input number of sides: 4. Input the length of a side: 25. The area of the polygon is: 625
