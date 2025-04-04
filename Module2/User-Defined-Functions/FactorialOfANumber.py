def factorial(NUM):
    fact = 1
    for i in range(1, NUM+1):
        fact *= i
    return fact

NUM = int(input("Enter the Number: "))
print(f"Factorial of the number: {factorial(NUM)}")