# Arithmetic Progression
"""
S = a + (a+d) + (a+2d) + (a+3d) + .......... + (a + (n-1)d)
"""

A = int(input("Enter the Value of A: "))
D = int(input("Enter the Value of D: "))
N = int(input("Enter the Value of N: "))


Series_List = [(A + (i)*D) for i in range(N)]
Sum_Of_Series = sum(Series_List)

print(f"""
      Series Sequence: {Series_List}
      Sum of Arithmetic Progression Series of Constraint [a={A}, d={D}, n={N}] is {Sum_Of_Series}
""")
