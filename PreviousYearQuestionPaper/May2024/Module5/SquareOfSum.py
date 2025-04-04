#Question
"""
Consider the mathematical expression (a+b)^2=(a^2+2ab+b^2). Write a Python
program that takes user input for values of a and b, then evaluates both sides of
the expression. Finally, compare the results and print whether the equation holds
true or false.
"""

A,B = map(int, input("Enter the Values of A & B respectively (Seperated by Commas): ").split(","))

LeftSide = ((A+B)**2)
RightSide = (A**2) + (2*A*B) + (B**2)

print(f"""
      Left Side and Right Side of the Equation are {LeftSide} and {RightSide} respectively
      Does the Equation Hold True? {LeftSide == RightSide}
""")
