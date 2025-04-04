"""How to draw a square and hexagon using turtle module in Python."""

from turtle import Turtle, done

def square(t, length, x, y):
    t.up()
    t.goto(x, y)
    t.down()
    for _ in range(4):
        t.forward(length)
        t.left(90)
    t.hideturtle()

def hexagon(t, length, x, y):
    t.up()
    t.goto(x, y)
    t.down()
    for _ in range(6):
        t.forward(length)
        t.left(60)
    t.hideturtle()

pen = Turtle()
X,Y = map(int, input("Enter the X,Y coordinates: ").split())
length = int(input("Enter the length of the polygon: "))
square(pen, length, X,Y)
X,Y = map(int, input("Enter the X,Y Coordinates: ").split())
length = int(input("Enter the length of the polygon: "))
hexagon(pen, length, X, Y)
done()
