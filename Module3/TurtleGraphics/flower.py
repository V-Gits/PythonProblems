from turtle import Turtle, done
import math
import random

def drawFlower(t, X, Y, penColor= "black", NUM= 13, A= 100):
    t.speed("fastest")
    t.width(3)
    t.goto(X,Y)
    fillColor = "red"
    t.pencolor(penColor)
    for angle in range(1, 361, 1):
        theta = math.radians(angle)
        r = A * math.sin(NUM*theta)
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        t.goto(x, y)
        t.down()

    t.up()
    t.hideturtle()


pen = Turtle()
pen.goto(0, -155)
pen.down()
pen.circle(310)
pen.fillcolor("green")
pen.begin_fill()
pen.end_fill()
drawFlower(pen, 0, 0, "orange",144 , 300)
drawFlower(pen, 0, 0, "purple", 89, 250)
drawFlower(pen, 0, 0, "yellow", 55, 200)
drawFlower(pen, 0, 0, "red", 34, 150)
drawFlower(pen, 0, 0, "pink", 21, 100)

done()