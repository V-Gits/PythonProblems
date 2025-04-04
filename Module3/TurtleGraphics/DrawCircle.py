"""Draw a Circle:
Write a program to draw a circle with a radius of user entered pixels."""

from turtle import Turtle, done
import math

def DrawCircle(t, radius, X=0, Y=0, penColor="black", fillColor="blue"):
    t.up()
    t.goto(X, Y)
    t.down()
    t.pencolor(penColor)
    t.fillcolor(fillColor)
    t.begin_fill()
    arc_length = (2 * math.pi * radius)/360
    for _ in range(360):
        t.forward(arc_length)
        t.left(1)
    t.end_fill()
    t.hideturtle()
    done()

pen = Turtle()
X,Y = map(int, input("Enter the X,Y coordinates: ").split())
radius = int(input("Enter the radius of Circle: "))
penColor = input("Enter the Pencolor: ")
fillColor = input("Enter the Fillcolor: ")
DrawCircle(pen, radius, X,Y, penColor, fillColor)
