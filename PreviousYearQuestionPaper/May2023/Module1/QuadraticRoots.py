#Question: Write a Python program to find the roots of a quadratic equation, ax^2 + bx + c = 0 . Consider the cases of both real and imaginary roots.

'''
Approach:
Roots are real if b^2-4ac > 0
Roots are imaginary if b^2-4ac < 0
Roots are equal if b^2-4ac = 0

If roots are real, we can use the formula x = ((-b ± squareroot(b^2-4ac))/2a) for roots 
If roots are imaginary, we can use the formula x = ((-b ± j *squareroot(b^2-4ac))/2a) for roots
If roots are equal, we can use the formula x = -c / b
'''

import cmath

def FindRoots(A,B,C):
    if A == 0:
        if B == 0:
            return f"No Solution is there as A and B cannot be 0"
        return f"Linear Equation Solution : x= {-C/B}"
    
    discriminant = B**2 - 4*A*C 

    root1 = (-B + cmath.sqrt(discriminant))/(2 * A)
    root2 = (-B - cmath.sqrt(discriminant))/(2 * A)

    return root1, root2

print("For the equation ax^2 + bx + c = 0,")
A,B,C = map(float, input("Enter the Coefficent of (a,b,c) respectively: ").split(", "))

roots = FindRoots(A,B,C)

if isinstance(roots, str):
    print(roots)
else:
    print(f"The Roots of the Equation are: {roots[0]} & {roots[1]}")

