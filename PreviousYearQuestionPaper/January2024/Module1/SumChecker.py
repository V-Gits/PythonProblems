#Question
"""
Write a Python program to print all numbers between 100 and 1000 whose sum
of digits is divisible by 9.
"""

def SumChecker(NUM):
    RESULT = 0
    while NUM > 0:
        digit = NUM%10
        RESULT += digit
        NUM = NUM//10
    
    return RESULT%9 == 0

for NUM in range(100, 1001):
    if SumChecker(NUM):
        print(NUM, end=",")

