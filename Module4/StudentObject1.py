"""
2.Create a Student class and initialize it with name and roll number.

Make methods to :
a.Display - Display all informations of the student.
b.setAge - Assign age to student
c.setTestMarks - Assign marks of a test to the student.
"""

class Student:
    def __init__(self, studentname, rollnumber):
        self.name = studentname
        self.rollnumber = rollnumber
        self.age = None
        self.marks = None
    def display(self):
        print(f"""
        Name: {self.name}
        Roll No: {self.rollnumber}
        Age: {self.age}
        Marks: {self.marks}
        """)
    def setAge(self, age):
        self.age = age
    def setTestMarks(self, marks):
        self.marks = marks

def main():
    student = Student("John", 8)
    student.display()
    student.setAge(17)
    student.display()
    student.setTestMarks(96)
    student.display()

if __name__ == "__main__":
    main()
