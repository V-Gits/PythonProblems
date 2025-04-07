def NaturalNumberSum(NUM):
    """Calculates the sum of all natural numbers up to NUM."""
    if NUM <= 0:
        return 0
    return NUM + NaturalNumberSum(NUM-1)

NUM = int(input("Enter the Number: "))
print(f"Sum of {NUM} natural numbers is {NaturalNumberSum(NUM)}")