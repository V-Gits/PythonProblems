#Question: Write a python program to find X^Y or pow(X,Y) without using standard function
'''
Approach
Using Loop to calculate X^Y By multipling  
'''

X,Y = map(int,input("Enter the base and power Numbers: ").split(","))
RESULT = 1
for _ in range(Y):
    RESULT *= X
print(f"{X}^{Y} = {RESULT}")