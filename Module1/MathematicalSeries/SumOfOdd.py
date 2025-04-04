#Odd Series
"""
S = 1 + 3 + 5 + ........ + 2n-1
"""

N = int(input("Enter the Number of Terms: "))

Odd_List = [i for i in range(1, 2*N, 2)]
Odd_Sum = sum(Odd_List) #Approach 1 To Find the Sum of N Odd Numbers

print(f"""
        The Odd Number Series: {Odd_List}
        The Sum of The Series: {Odd_Sum}
""")

Odd_Sum = N*N #Approach 2 to Find the Sum of N Odd Numbers
print(f"""
        The Sum of The Series: {Odd_Sum}
""")