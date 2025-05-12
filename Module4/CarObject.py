"""
1.A class Car with attributes registration_number, color, mileage and year, and a
method to display information about the car. Write a Python program to create an
instance of the Car class and demonstrate how to access and modify its attributes.
"""

class Car:
    def __init__(self, registration_number, color, milege, year):
        self.registration_number = registration_number
        self.color = color
        self.milege = milege
        self.year = year
    
    def display_info(self):
        print(f"""
                Registration Number : {self.registration_number}
                Color : {self.color}
                Mileage : {self.milege} km  
                Year of Manufacture : year    
              """)


C = Car("KL-66-H-8912", "Blue", 50000, 2016)
print("Before modification:")
C.display_info()

C.color = "Black"
C.year = 2015
print("After modification:")
C.display_info()
