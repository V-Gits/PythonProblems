# Harmonic Series
"""
S = 1 + 1/2 + 1/3 + 1/4 + ............ + 1/n
"""

N = int(input("Enter the Number of Term in the Series: "))

Series_List = [1/i for i in range(1, N+1)]
Sum_Of_Series = sum(Series_List)

print(f"""
      Series Sequence: {Series_List}
      Sum of Harmonic Seriesof  [n={N}] is {Sum_Of_Series}
""")
