#Question: Write a python program to generate the following type of pattern for the given Nrows where N <= 26.
'''
A
A B
A B C D
A B C D E
'''

N = int(input("Enter the Number of Rows: "))
ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" #26 Letters

if 0 < N <= 26:
    for i in range(N):
        for j in range(i+1):
            print(ALPHA[j], end=" ")
        print("")
