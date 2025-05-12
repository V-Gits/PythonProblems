"""
Write a Python class Person with a private attribute __age.
Provide methods to set and get the age.
"""

class Person:
    def __init__(self):
        self.__age = None
    def setAge(self):
        age = int(input("Enter the Age: "))
        self.__age = age
    def getAge(self):
        print(f"AGE: {self.__age}")

def main():
    person = Person()
    person.setAge()
    person.getAge()

if __name__ == "__main__":
    main()