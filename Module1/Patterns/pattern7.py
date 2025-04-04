#Question: Draw the Pattern of N rows
"""
N=4
1
2 3
4 5 6
7 8 9 10
"""

N = int(input("Enter the Number of Rows: "))

k = 1
for i in range(1, N+1):
    for j in range(1, i+1):
        print(k, end = " ")
        k+=1
    print()