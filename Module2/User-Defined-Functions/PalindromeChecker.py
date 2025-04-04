def isPalindrome(STRING):
    LENGTH = len(STRING)
    leftPointer = 0
    rightPointer = LENGTH - 1
    while leftPointer <= rightPointer:
        if STRING[leftPointer] != STRING[rightPointer]:
            return False
        leftPointer += 1
        rightPointer -= 1
    return True

STRING = input("Enter the String: ")
print(isPalindrome(STRING))
