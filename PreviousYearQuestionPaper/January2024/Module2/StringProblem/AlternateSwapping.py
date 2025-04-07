"""
Write a Python to input a word and replace all alternate character with $
"""

def alternate(string):
    n = len(string)
    new_string = list(string)
    for i in range(n):
        if i % 2 != 0:
            new_string[i] = '$'
    return ''.join(new_string)

string = input("Enter a word: ")
print(f"String after updated: {alternate(string)}")

#Output
"""
Enter a word: hello
String after updated: h$l$o
"""