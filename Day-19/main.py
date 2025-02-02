from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    """Forwards by 20"""
    tim.forward(20)
def move_backwards():
    """Backwards by 20"""
    tim.backward(20)
def turn_left():
    """Turns left by 45 degree"""
    new_heading = tim.heading()+45
    tim.setheading(new_heading)
def turn_right():
    """Turns right by 45 degree"""
    new_heading = tim.heading() - 45
    tim.setheading(new_heading)

def clear():
    """Clear and Initialize the drawing"""
    tim.clear()
    tim.home()


screen.listen()
screen.onkey(move_forwards,'w')
screen.onkey(move_backwards,'s')
screen.onkey(turn_left,'a')
screen.onkey(turn_right,'d')
screen.onkey(clear,'c')
screen.exitonclick()