def GCD(NUM1, NUM2):
    """Finding GCD/HCF of a number using Recursive Functional Method"""
    if NUM2 == 0:
        return NUM1
    
    return GCD(NUM2, NUM1%NUM2)

NUM1 = int(input("Enter the First Number: "))
NUM2 = int(input("Enter the Second Number: "))
print(f"GCD of {NUM1} & {NUM2} is {GCD(NUM1,NUM2)}")