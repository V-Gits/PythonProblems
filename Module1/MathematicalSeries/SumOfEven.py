#Even Series
"""
S = 2 + 4 + 6 + ........ + 2n
"""

N = int(input("Enter the Number of terms in the Series: "))

Even_List = [i for i in range(2, (2*N)+1, 2)]
Even_Sum = sum(Even_List) #Approach 1 To Find the Sum of N Even Numbers

print(f"""
        The Even Number Series: {Even_List}
        The Sum of The Series: {Even_Sum}
""")

Even_Sum = N*(N+1) #Approach 2 to Find the Sum of N Even Numbers

print(f"""
        The Sum of The Series: {Even_Sum}
""")