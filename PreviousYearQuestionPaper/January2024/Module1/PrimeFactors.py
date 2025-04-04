#Question 
"""
Write a Python program to print all prime factors of a given number.
"""

def isPrime(NUM):
    if NUM < 2:
        return False
    for i in range(2, (NUM//2)+1):
        if NUM%i == 0:
            return False
    return True

def Factors(NUM):
    return [i for i in range(1, (NUM//2)+1) if isPrime(i)]


NUM = int(input("Enter the Number to Find its Prime Factors: "))
print(f"""
      Prime Factors of {NUM} are: {Factors(NUM)}
    """)
