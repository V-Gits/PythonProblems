#Question: Draw the Pattern of N rows
"""
N=4
* * * *
 * * *
  * *
   *
"""

N = int(input("Enter the number of Rows: "))

#Approach 1
for i in range(N, 0, -1):
    print(" "*(N-i), end = "")
    for j in range(i):
        print("* ", end = "")
    print()

#Approach 2
for i in range(N, 0, -1):
    print(" "*(N-i)+"* "*i)
