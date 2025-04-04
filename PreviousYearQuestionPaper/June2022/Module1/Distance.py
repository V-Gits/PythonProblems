#Question: Write a Python program to find distance between two points (x1,y1) and (x2,y2).

'''
Approach
Equation :-> d=squareroot{(X2^2-X1^2)+(Y2^2-Y1^2)
'''

import math

X1,Y1 = map(int, input("Enter the (X,Y)Coordinates of the first Point: ").split(","))
X2,Y2 = map(int, input("Enter the (X,Y)Coordinates of the second Point: ").split(","))

dX = X2-X1
dY = Y2-Y1

pythogrean = math.sqrt(dX**2 + dY**2)

print(f"Distance: {pythogrean}")
