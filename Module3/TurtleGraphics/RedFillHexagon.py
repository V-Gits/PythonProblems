"""Write a Python program to draw a hexagon and to fill it with red colour. Explain
the turtle methods used in it."""

from turtle import Turtle, done


def hexagon(t, length, fillColor,  x=0, y=0):
    t.up()
    t.goto(x, y)
    t.down()
    t.fillcolor(fillColor)
    t.begin_fill()
    for _ in range(6):
        t.forward(length)
        t.left(60)
    t.end_fill()
    t.hideturtle()


pen = Turtle()
X, Y = map(int, input("Enter the X, Y coordinates: ").split())
length = int(input("Enter the Hexagon Length: "))
fillColor = input("Enter the color ins lowercase: ")
fillColor = fillColor.lower()
hexagon(pen, length, fillColor, X, Y)
done()