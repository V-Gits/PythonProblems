NUM = int(input("Enter the Number: "))
i = 1
RES = 1
if NUM > 0:
    while i <= NUM:
        RES *= i
        i += 1

print(f"{NUM}! = {RES}")
