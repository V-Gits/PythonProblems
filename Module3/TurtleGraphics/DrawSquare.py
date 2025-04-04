"""Write a python function to draw a square using turtle graphics"""

from turtle import Turtle, done

def square(t, length, x, y):
    t.up()
    t.goto(x, y)
    t.down()
    for _ in range(4):
        t.forward(length)
        t.left(90)
    t.hideturtle()

pen = Turtle()
X,Y = map(int, input("Enter the X,Y coordinates: ").split())
length = int(input("Enter the length of the polygon: "))
square(pen, length, X,Y)
done()