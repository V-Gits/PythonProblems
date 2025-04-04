#Question: Draw the Pattern of N rows
"""
N=4
*
* *
* * *
* * * *
"""

N = int(input("Enter the Number of Rows: "))

#Approach 1
for i in range(1, N+1):
    for j in range(1, i+1):
        print("* ", end= "")
    print()

print("-----------------------------")

#Approach 2
for i in range(1, N+1):
    print("* " * i)