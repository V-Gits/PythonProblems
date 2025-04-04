"""
Write a Python program to count the number of occurances of a
character in a given string without using count() method
"""

def frequency(string, character):
    di = dict()
    for char in string:
        if char in di:
            di[char] += 1
        else:
            di[char] = 1
    return di.get(character, 0)

STRING = input("Enter a long string: ")
CHAR = input("Enter a character: ")
print(f"The frequency of '{CHAR}' in '{STRING}' is {frequency(STRING, CHAR)}")

#OUTPUT
"""
Enter a long string: Hi, I'm from India
Enter a character: i
The frequency of 'i' in 'Hi, I'm from India' is 2
"""