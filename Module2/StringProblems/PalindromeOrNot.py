"""
Write a Python program to check whether a string is palindrome or not
"""

def palindromeChecker(string):
    Lp = 0
    Rp = len(string) - 1
    while Lp <= Rp:
        if string[Lp] != string[Rp]:
            return False
        Lp+=1
        Rp-=1
    else:
        return True

STRING = input("Enter the String: ")
print(f"The String '{STRING}' is {'Palindrome' if palindromeChecker(STRING) else 'Not Palindrome'}")


#Output
"""
Enter the String: malayalam
The String 'malayalam' is Palindrome

Enter the String: hello
The String 'hello' is Not Palindrome
"""