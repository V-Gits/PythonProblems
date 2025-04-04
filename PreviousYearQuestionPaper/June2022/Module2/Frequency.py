"""
Write a Python program to count how many times each character appears in a
given string and store the count in a dictionary with key as the character.
"""

di = dict()
s = input("Enter the String: ")
for char in s:
    if char in di:
        di[char] += 1
    else:
        di[char] = 1
print(f"The Dictionary is: {di}")