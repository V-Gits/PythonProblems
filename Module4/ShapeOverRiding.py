"""
Define a base class "Shape" with attributes width and height, and a method
to calculate the area. Create two subclasses: "Rectangle" and "Triangle"
inheriting from the "Shape" class. Demonstrate polymorphism by calling the
area calculation method on instances of both subclasses.
"""
class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        area = self.width * self.height
        return area


class Recatangle(Shape):
    def __init__(self, width, height):
        super().__init__(width, height)
    
    def area(self):
        area = self.width * self.height
        return area
    

class Triangle(Shape):
    def __init__(self, width, height):
        super().__init__(width, height)
    
    def area(self):
        area = 0.5*self.width*self.height
        return area
    

def main():
    rectangle = Recatangle(5, 10)
    triangle = Triangle(5, 10)
    print(f"Area of Rectangle: {rectangle.area()}")
    print(f"Area of Triangle: {triangle.area()}")

if __name__ == "__main__":
    main()