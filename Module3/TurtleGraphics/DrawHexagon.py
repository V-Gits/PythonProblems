"""Write a python function to draw an hexagon using turle graphics"""

from turtle import Turtle, done

def hexagon(t, length, x, y):
    t.up()
    t.goto(x, y)
    t.down()
    for _ in range(6):
        t.forward(length)
        t.left(60)
    t.hideturtle()

pen = Turtle()
X,Y = map(int, input("Enter the X,Y Coordinates: ").split())
length = int(input("Enter the length of the polygon: "))
hexagon(pen, length, X, Y)
done()