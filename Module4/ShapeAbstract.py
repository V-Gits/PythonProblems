"""
Create an Abstract Base Class called Shape thatinclude abstract methods area()
and circumference(). Then derive two classes Circle and Rectangle from
the Shape class and implementthe area() and circumference() methods . Write a
Python program to implement above concept.
"""

from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def circumference(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * (self.radius * self.radius)
    
    def circumference(self):
        return 2 * pi * self.radius
    
class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    
    def area(self):
        return self.length * self.breadth

    def circumference(self):
        return 2 * (self.length + self.breadth)


def main():
    circle = Circle(5)
    rectangle = Rectangle(8,9)
    print(f"Circle Area: {circle.area()}")
    print(f"Circle Circumference: {circle.circumference()}")
    print(f"Rectangle Area: {rectangle.area()}")
    print(f"Rectangle Circumference: {rectangle.circumference()}")

if __name__ == "__main__":
    main()