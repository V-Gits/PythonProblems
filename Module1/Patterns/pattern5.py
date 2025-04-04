#Question: Draw the Pattern of N rows
"""
N=4
* * * *
  * * *
    * *
      *
"""

N = int(input("Enter the Number of Rows: "))
 
#Approach 1
for i in range(N, 0, -1):
  print("  "*(N-i),end=" ") #Add 2 space
  for j in range(1,i+1):
    print("*", end=" ")
  print()

#Approach 2
for i in range(N, 0, -1):
    for j in range(i, N):
        print(" ", end=" ")
    for k in range(1, i+1):
       print("*", end = " ")
    print()

#Approach 3
for i in range(N, 0, -1):
   print("  "*(N-i),"* "*i)