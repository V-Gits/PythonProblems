#Question: Write a Python program to count number of even numbers and odd numbers in a given set of n numbers.

N = int(input("Enter the Number of Elements: "))
li = []

for _ in range(N):
    li.append(int(input("Enter the Number: ")))

EVEN = 0
ODD = 0

for NUM in li:
    if NUM%2 == 0:
        EVEN+=1
    else:
        ODD+=1

print(f"Number of Even: {EVEN} \nNumber of Odd: {ODD}")