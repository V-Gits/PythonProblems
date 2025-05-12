"""
3.Define a class Student in Python with attributes to store the roll number, name,and
marks of three subjects for each student.
Define the following methods:
1.readData()- to assign values to the attributes
2.computeTotal() – to find the total marks
3.print_details() - to display the attribute values and the total marks
4.Create an object of the class and invoke the methods.
"""

class Student:
    def __init__(self):
        self.name = None
        self.roll_number = None
        self.marks = dict()

    def readData(self):
        self.name = input("Enter the name of student: ")
        self.roll_number = input(f"Enter the roll number of student {self.name}: ")
        subjects = list(map(str.strip, input("Enter the three subjects fo the student (separated by comma ): ").split(",")))
        for subject in subjects: 
            self.marks[subject] = int(input(f"Enter the marks of the student {self.name} for the subject {subject}: "))
        
    def computeTotal(self, marks):
        total = 0
        for mark in marks.values():
            total += mark
        return total
    
    def print_details(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_number}")
        print(f"Subject\t|Marks")
        print("--"*10)
        for subject, mark in self.marks.items():
            print(f"{subject}\t|{mark}")
        print("--"*10)
        print(f"Total Marks: {self.computeTotal(self.marks)}")


def main():
    student = Student()
    student.readData()
    student.print_details()

if __name__ == "__main__":
    main()