#Question: Write a Python program to display the sum of odd numbers between a programmer specified upper and lower limit.

def isOdd(NUM):
    return NUM % 2 != 0

LOWER = int(input("Enter the lower Limit: "))
UPPER = int(input("Enter the Upper Limit: "))

print(f"Sum of Odd Numbers from {LOWER} to {UPPER}: {sum([i for i in range(LOWER, UPPER+1) if isOdd(i)])}")