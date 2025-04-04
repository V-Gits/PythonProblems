N = 0
SUM = 0
while True:
    NUM = int(input("Enter the Number: "))
    if NUM == 0:
        break
    else:
        SUM += NUM
        N += 1

print(f"Sum of the Numbers is: {SUM}")
print(f"Average of the Numbers is: {(SUM/N):.3f}")
