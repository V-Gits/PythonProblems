#Question: Write a Python program to check whether a number is Armstrong number or not. An Armstrong number is an n-digit number that is equal to the sum of the nth powers of its digits.
#Examples: 153 = 1^3 + 5^3 + 3^3 , 1634 = 1^4 + 6^4 + 3^4+ 4^4

NUM = int(input("Enter the Number: "))
TEMP = NUM

POWER= 0

while TEMP > 0:
    POWER += 1
    TEMP = TEMP//10

TEMP = NUM
AMSTRONG_NUM = 0

while TEMP > 0:
    DIGIT = TEMP%10
    AMSTRONG_NUM += DIGIT**POWER
    TEMP = TEMP//10

if AMSTRONG_NUM == NUM:
    print(f"{NUM} is an AMSTRONG number")
else:
    print(f"{NUM} is not an AMSTRONG number")