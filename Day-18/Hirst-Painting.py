import turtle
from random import random
from turtle import Turtle, Screen
from turtle_colors import rgb_colors
new_turtle = Turtle()
def draw_spot_painting(size):
    new_turtle.setheading(225)
    new_turtle.penup()
    new_turtle.forward(300)
    new_turtle.setheading(0)
    for _ in range(size):
        for __ in range(size):
            new_turtle.dot(20,random.choice(rgb_colors))
            new_turtle.penup()
            if __ != size-1:
                new_turtle.forward(50)
        if _ & 1:
            new_turtle.right(90)
            new_turtle.forward(50)
            new_turtle.right(90)
        else:
            new_turtle.left(90)
            new_turtle.forward(50)
            new_turtle.left(90)

t = turtle
t.colormode(255)
new_turtle.shape('arrow')
new_turtle.hideturtle()
draw_spot_painting(10)
screen = Screen()