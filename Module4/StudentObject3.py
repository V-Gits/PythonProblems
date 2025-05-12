"""
Write a Python class Person with a private attribute __age.
Provide methods to set and get the age.
"""
class Class:
    def __init__(self, roll_number, marks):
        self._roll_number = roll_number
        self._marks = marks

class EnglishClass(Class):
    def __init__(self, roll_number,marks):
        super().__init__(roll_number, marks)
        print(f"Roll No: {self._roll_number}")
        print(f"Marks: {self._marks}")

def main():
    english_class = EnglishClass(23, 98)

if __name__ == "__main__":
    main()
