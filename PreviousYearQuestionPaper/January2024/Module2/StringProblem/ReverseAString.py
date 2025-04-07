"""
Write a Python program to reverse a string
"""

def reverseString(string):
    return string[::-1]

STRING = input("Enter the String: ")
REVERSED_STRING = reverseString(STRING)
print(f"On reversing the string '{STRING}' we get this string '{REVERSED_STRING}'")

#Output

"""
Enter the String: hello world
On reversing the string 'hello world' we get this string 'dlrow olleh'
"""
