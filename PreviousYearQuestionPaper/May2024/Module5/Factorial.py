#Question
"""
Write a python program to print factorial of a given number.
"""

#Approach 1

def factorial(NUM):
    if (NUM == 0) or (NUM == 1):
        return 1
    return NUM * (factorial(NUM-1))

NUM = int(input("Enter the Number of which you want to find the factorial: "))

print(f"\nFactorial of {NUM} is ({NUM}!) = {factorial(NUM)}\n")

#Approach 2
result = 1
for i in range(1, NUM+1):
    result *= i

print(f"\nFactorial of {NUM} is ({NUM}!) = {result}\n")