"""
Creating of heart using math function
x=16sin^3(θ)
y=13cos(θ)-5cos(2θ)-2cos(3θ)-cos(4θ)
"""

from turtle import Turtle, done
import math
import random

def drawHeart(t, X, Y, penColor="black", NUM =100):
    t.speed("fastest")
    colors = ["red", "black", "green", "yellow", "blue", "purple", "orange", "pink"]
    t.pencolor(penColor)
    for i in range(NUM):
        fillColor = random.choice(colors)
        t.up()
        t.fillcolor(fillColor)
        t.begin_fill()
        for i in range(361):
            theta = math.radians(i)
            x = 16 * (math.sin(theta)**3)
            y = (13 * (math.cos(theta))) - (5 * (math.cos(2 * theta))) - (2 * (math.cos(3 * theta))) - (math.cos(4 * theta))
            t.goto(x+X, y+Y)
            t.down()
        t.end_fill()
        
        xChange = random.randrange(-100, 100)
        yChange = random.randrange(-100, 100)
        print(f"{xChange=} {yChange=}")
        X+=xChange
        Y+=yChange
        t.up()
        t.goto(X, Y)
    
    
    t.hideturtle()
    done()

pen = Turtle()
X,Y = map(int, input("Enter the X,Y coordinates: ").split())
penColor = input("Enter the Pencolor: ")
NUM = int(input("Enter the number of hearts: "))
drawHeart(pen, X,Y, penColor, NUM)
    
