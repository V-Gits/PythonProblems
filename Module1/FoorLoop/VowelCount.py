STRING = input("Enter the String: ")
VOWELS = "AEIOUaeiou"
COUNT = 0
for i in STRING:
    if i in VOWELS:
        COUNT += 1
print(f"The Number of Vowels in the String is: {COUNT}")