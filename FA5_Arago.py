import turtle
import random
import math

t = turtle.Turtle()
t.speed(0) 

def DrawCircle():
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(0, -100)
    t.pendown()
    t.circle(100)


    t.hideturtle()



t.penup()
t.goto(0, 0)
t.setheading(random.uniform(0, 360))

def Bounce_off_circle():
    while True:
        t.forward(2)

        if t.distance(0, 0) >= 100:
            t.left(random.uniform(120, 180))

DrawCircle()
Bounce_off_circle()

turtle.done()