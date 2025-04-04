#Sin Series
"""
S = x - (x^3)/3! + (x^5)/5! - ....... + ((-1)^n) * (x^(2n+1))/(2n+1)!
"""

import math

N = int(input("Enter the Number of Terms: "))
X = int(input("Enter the Value of X in radians: "))

Sin_Series = [((-1) ** i) * (X ** (2 * i + 1))/math.factorial(2 * i + 1) for i in range(0, N)]
Sin_Sum = sum(Sin_Series)

print(f"""
        The Odd Number Series: {Sin_Series}
        The Sum of The Series: {Sin_Sum}
""")