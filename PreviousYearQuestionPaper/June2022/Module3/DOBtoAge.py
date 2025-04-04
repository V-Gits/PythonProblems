"""
Write Python GUI program to take the birth date and output the age when a
button is pressed.
"""

from breezypythongui import EasyFrame
from datetime import datetime

class AgeCalculator(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Age Calculator", width=300, height=200)
        self.addLabel("Enter the Birth Date (YYYY-MM-DD): ", row=0,column=0)
        self.birthDateField = self.addTextField("",row=0, column=1)
        self.addButton("Calculate Age", row=1, column=0, columnspan=2, command=self.calculate_age)

    def calculate_age(self):
        birth_date_str = self.birthDateField.getText().strip()  # Get and clean input
        birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d").date()  # Convert input to date format
        today = datetime.today().date()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        self.messageBox("Age Calculator", f"Your age is: {age} years")
        

if __name__ == "__main__":
    AgeCalculator().mainloop()