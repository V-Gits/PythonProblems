#Question: Given the value of x, write a Python program to evaluate the following series (Taylor Series) upto n terms:

"""
Approach: nth Term (Tn) = x^n/n! -> x**n/factorial(n)
"""

from math import factorial

SUM_of_SERIES = 0.0

X = float(input("Enter the value of x: "))
N = int(input("Enter the Number of Terms(n): "))

for i in range(N):
    TERM = (X**i)/factorial(i)
    SUM_of_SERIES += TERM

print(f"Sum of Taylor Series upto n terms is: {SUM_of_SERIES}") 