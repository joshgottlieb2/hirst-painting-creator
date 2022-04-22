import random
import turtle
from turtle import Turtle, Screen
turtle.speed("fastest")
turtle.hideturtle()

turtle.colormode(255)
color_list = [(139, 166, 193), (207, 155, 117), (192, 141, 151), (56, 103, 136), (230, 212, 107), (145, 179, 163), (148, 68, 58)]


def row():
    for dot in range(10):
        turtle.pencolor(random.choice(color_list))
        turtle.dot(20)
        turtle.penup()
        turtle.forward(50)
        turtle.pendown()

turtle.penup()
turtle.goto(-200, -200)
turtle.pendown()

for _ in range(10):
    row()
    turtle.penup()
    turtle.back(500)
    turtle.left(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.pendown()


screen = Screen()
turtle.exitonclick()
