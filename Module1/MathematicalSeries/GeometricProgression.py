# Geometric Progression
"""
S = a + ar + a(r^2) + a(r^3) + .......... + a(r^(n-1))
"""

A = int(input("Enter the Value of A: "))
R = int(input("Enter the Value of R: "))
N = int(input("Enter the Value of N: "))

Series_List = [(A * R**(i)) for i in range(N)]
Sum_Of_Series = sum(Series_List)

print(f"""
      Series Sequence: {Series_List}
      Sum of Geometric Progression Series of Constraint [a={A}, d={R}, n={N}] is {Sum_Of_Series}
""")