#Question: Write a python program to generate prime numbers within a certain range

def isPrime(NUM):
    if NUM < 2:
        return False
    else:
        for i in range(2, int(NUM**0.5) + 1):
            if NUM%i == 0:
                return False
        return True
    
LOWER = int(input("Enter the Lower Limit: "))
UPPER = int(input("Enter the Upper Limit: "))

prime_numbers = []
if UPPER >= LOWER and LOWER > 0 and UPPER > 2:
    prime_numbers = [i for i in range(LOWER, UPPER+1) if isPrime(i)]
print(prime_numbers)