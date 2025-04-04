NUM = int(input("Enter the Number: "))
ANS = 1
for i in range(1, NUM+1):
    ANS*=i
print(f"Factorial of {NUM}  is ({NUM}!): {ANS}")
