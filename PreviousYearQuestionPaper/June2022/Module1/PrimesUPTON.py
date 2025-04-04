#Question: Write the python program to print all prime numbers less than 1000.

def isPrime(NUM):
    if NUM < 2:
        return False
    else:
        for i in range(2, int(NUM**0.5) + 1):
            if NUM%i == 0:
                return False
        return True
    
N = int(input("Enter the Top Boundary: "))
if N > 2:
    prime_numbers =[i for i in range(2, N) if isPrime(i)]

print(prime_numbers)
