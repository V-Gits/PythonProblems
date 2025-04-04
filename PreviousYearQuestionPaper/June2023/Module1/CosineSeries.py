#Question: Write a python program to find the sum of the cosine series 1 - x^2/2! + x^4/4!- ......
'''
Approach:
cos(x) = 1 - x^2/2! + x^4/4! - x^6/6! .....
'''

import math

def CosineSum(angle, terms):
    COS_SUM = 0
    radians = math.radians(angle)
    for i in range(terms):
        term = (((-1) ** i) * (radians ** (2 * i))) / math.factorial(2 * i)
        COS_SUM += term
    return COS_SUM

ANGLE = float(input("Enter the angle in Degrees: "))
TERMS = int(input("Enter the number of terms in the Series: "))

print(f"The sum of the cosine series for {TERMS} terms is: {CosineSum(ANGLE, TERMS)}")