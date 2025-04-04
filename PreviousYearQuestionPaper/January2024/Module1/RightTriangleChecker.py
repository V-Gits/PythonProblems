#Question
"""
Write a program that accepts the lengths of three sides of a triangle as inputs and
outputs whether or not the triangle is a right triangle.
"""

base = int(input("Enter the base of The Triangle: "))
height = int(input("Enter the height of The Triangle: "))
hypotenuse = int(input("Enter the hypotenuse of The Triangle: "))

if (base**2) + (height**2) == (hypotenuse**2):
    print(f"""
        The Triangle with base {base} and height {height} is a right triangle with hypotenuse {hypotenuse}.
    """)
else:
    print(f"""
        The Triangle with base {base} and height {height} cannot be a right triangle with hypotenuse {hypotenuse}.
    """)