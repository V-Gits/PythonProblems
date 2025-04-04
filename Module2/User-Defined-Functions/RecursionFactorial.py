def factorial(NUM):
    if NUM == 0 or NUM == 1:
        return 1
    return  NUM * factorial(NUM-1)

NUM = int(input("Enter the Number: "))
print(f"Factorial of the number: {factorial(NUM)}")