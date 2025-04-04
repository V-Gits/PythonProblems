"""Draw a Triangle:
Use Turtle to draw an equilateral triangle and fill it with a color"""

from turtle import Turtle, done

def equilaterlTriangle(t, length, X, Y, colorFill):
    t.up()
    t.goto(X,Y)
    t.down()
    t.fillcolor(colorFill)
    t.begin_fill()
    for _ in range(3):
        t.forward(length)
        t.left(120)
    t.end_fill()
    t.hideturtle()
    done()

pen = Turtle()
X, Y = map(int, input("Enter the X,Y Coordinates seperated by comma: ").split(","))
length = int(input("Enter the length of the triangle: "))
colorFill = input("Enter the color of the triangle: ")
colorFill = colorFill.lower()
equilaterlTriangle(pen, length, X, Y, colorFill)


