"""
Write a Python program to print all prefixes and suffixes of a given string
"""

def prefix(string):
    n = len(string)
    print(f"Prefix of the String '{string}' is: ")
    for i in range(0, n):
        print(string[0:i+1])
    return

def suffix(string):
    n = len(string)
    print(f"Sufffix of the String '{string}' is: ")
    for i in range(0, n):
        print(string[0:n-i])
    return


STRING = input("Enter a string: ")
prefix(STRING)
suffix(STRING)

#Output


"""
Enter a string: Number
Prefix of the String 'Number' is: 
N
Nu
Num
Numb
Numbe
Number
Sufffix of the String 'Number' is:
Number
Numbe
Numb
Num
Nu
N
"""