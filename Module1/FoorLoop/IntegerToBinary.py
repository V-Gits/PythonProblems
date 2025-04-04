NUM = int(input("Enter the Number: "))
BINARY_STRING = ""
if NUM == 0:
    BINARY_STRING += "0"
else:
    for i in range(32):
        BINARY_STRING = str(NUM%2) + BINARY_STRING
        NUM = NUM//2

        if NUM == 0:
            break
print(f"Integer ({NUM}) equals to: {BINARY_STRING}")