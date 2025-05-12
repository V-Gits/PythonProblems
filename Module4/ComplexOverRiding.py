"""
Write Python program to create a class called as Complex to model complex
numbers and implement __add__() and __mul__() methods to add and
multiply two complex numbers. Display the result by overloading the + and *
operator.
"""

class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        new_real = self.real + other.real
        new_imaginary = self.imaginary + other.imaginary
        return Complex(new_real, new_imaginary)
    
    def __mul__(self, other):
        new_real = ((self.real *other.real)-(self.imaginary*other.imaginary))
        new_imaginary = ((self.real * other.imaginary)+(self.imaginary * other.real))
        return Complex(new_real, new_imaginary)
    
    def __str__(self):
        sign = "+" if self.imaginary >= 0 else "-"
        return f"{self.real} {sign} {abs(self.imaginary)}i"
    

def main():
    c1 = Complex(2,3)
    c2 = Complex(7,1)

    print(f"First Complex Number: {c1}")
    print(f"Second Complex Number: {c2}")

    c3 = c1+c2
    print(f"{c1} + {c2} = {c3}")

    c4 = c1*c2
    print(f"{c1} x {c2} = {c4}")


if __name__ == "__main__":
    main()