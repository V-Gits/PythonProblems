#Sin Series
"""
S = 1 - (x^2)/2! + (x^4)/4! - ....... + ((-1)^n) * (x^(2n))/(2n)!
"""

import math

N = int(input("Enter the Number of Terms: "))
X = int(input("Enter the Value of X in radians: "))

Sin_Series = [((-1) ** i) * (X ** (2 * i))/math.factorial(2 * i) for i in range(0, N)]
Sin_Sum = sum(Sin_Series)

print(f"""
        The Odd Number Series: {Sin_Series}
        The Sum of The Series: {Sin_Sum}
""")