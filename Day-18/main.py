import turtle
from random import random
from turtle import Turtle, Screen
from turtle_colors import colors
import random
def draw_square(length):
    """Draws Square"""
    for i in range(4):
        new_turtle.right(90)
        new_turtle.forward(length)

def drag_line(length):
    """Draws Drag line"""
    for _ in range(length//2):
        if _ & 1:
            new_turtle.penup()
            new_turtle.forward(5)
        else:
            new_turtle.pendown()
            new_turtle.forward(5)

def draw_pentagon(length):
    """Draws a Pentagon"""
    for _ in range (5):
        new_turtle.left(72.0)
        new_turtle.forward(length)

def draw_shapes(length):
    """Draws all Shapes"""
    for i in range(3,11):
        for _ in range (i):
            new_turtle.left(360/i)
            new_turtle.forward(length)
        new_turtle.color(random.choice(colors))
directions = [0,90,180,270]

def random_walk():
    """Draws a Random Walk"""
    new_turtle.pensize(10)
    new_turtle.color(random.choice(colors))
    new_turtle.color(random_color())
    new_turtle.forward(random.randint(30,60))
    new_turtle.setheading(random.choice(directions))

def random_color():
    """Returns Random RGB Color"""
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colors = (r, g, b)
    return random_colors

def draw_spirograph(radius,angle):
    """Draws a Spirograph"""
    for _ in range (360//angle):
        new_turtle.color(random_color())
        new_turtle.circle(radius)
        new_turtle.right(angle)

def draw_spot_painting(size):
    """Draws Spot Hirst Painting"""
    for _ in range(size):
        for __ in range(size):
            new_turtle.dot(10,random.choice(colors))
            new_turtle.penup()
            new_turtle.forward(size)
        new_turtle.back(size*size)
        new_turtle.left(90)
        new_turtle.forward(size)
        new_turtle.right(90)

new_turtle = Turtle()
t = turtle
t.colormode(255)
new_turtle.shape('arrow')
new_turtle.color('red')
#TODO-1: Draw a Square
# draw_square(length=90)
#TODO-2: Draw drag line
# drag_line(50)
#TODO-3: Draw a Pentagon
# draw_pentagon(100)
#TODO-4: Draw different Shapes
# draw_shapes(100)
#TODO-5: Draw a Random Walk
# new_turtle.speed("fastest")
# for _ in range (50):
#     random_walk()
#TODO-6: Draw a Spirograph
# draw_spirograph(70,6)
#TODO-7: Draw a Spot Painting
# draw_spot_painting(10)
screen = Screen()
screen.exitonclick()