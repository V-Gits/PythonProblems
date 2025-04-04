""" Circle using the equation x^2+y^2=r^2
"""

from turtle import Turtle, done
import math

def Draw_Circle_from_Equation(t, radius, X=0, Y=0, penColor="black", fillColor="orange"):
    # Draw a circle using the equation x^2+y^2=r^2
    t.up()
    t.pencolor(penColor)
    t.fillcolor(fillColor)
    t.begin_fill()
    for angle in range(361):
        rad = math.radians(angle)
        x = X + radius * math.cos(rad)
        y = Y + radius * math.sin(rad)
        t.goto(x, y)
        t.down()

    t.end_fill()
    t.hideturtle()
    done()

pen = Turtle()
X,Y = map(int, input("Enter the X,Y coordinates: ").split())
radius = int(input("Enter the radius of Circle: "))
penColor = input("Enter the Pencolor: ")
fillColor = input("Enter the Fillcolor: ")
Draw_Circle_from_Equation(pen, radius, X,Y, penColor, fillColor)