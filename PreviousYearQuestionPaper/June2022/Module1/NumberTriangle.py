"""
Question: Write a python program to generate the following type of pattern for the given N rows .
1
1 2
1 2 3
1 2 3 4
"""

N = int(input("Enter the number of rows: "))

for i in range(1, N+1):
    for j in range(1, i+1):
        print(j , end = " ")
    print("\n")