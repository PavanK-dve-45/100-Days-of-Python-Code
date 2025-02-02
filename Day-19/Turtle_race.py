from random import randint
from turtle import turtles , Screen , Turtle
red = Turtle()
blue = Turtle()
green = Turtle()
orange = Turtle()
yellow = Turtle()
border = Turtle()
timi = [red, blue, green, orange, yellow]
timi_num = {'red':0,'blue':1,'green':2,'orange':3,'yellow':4}
timi_color = ['red','blue','green','orange','yellow']
t = turtles()

def object_shape(shape):
    num = 0
    for i in timi_color:
        timi[num].shape(shape)
        timi[num].color(i)
        num=num+1

def draw_finish_line():
    border.setheading(355)
    border.penup()
    border.forward(350)
    border.setheading(90)
    border.pendown()
    border.forward(200)
    border.setheading(0)

def align_turtle():
    for _ in range(5):
        timi[_].setheading(180 - _ * 5)
        timi[_].penup()
        timi[_].forward(300 + _ * 4)
        timi[_].setheading(0)

def running():
    x_value = []
    for inx in  range(5):
        x_value.append(timi[inx].xcor())
    if max(x_value)>349:
        return False
    else:
        x_value.clear()
        return True

def winner():
    value = []
    for _ in range(5):
        value.append(timi[_].xcor())
    return value.index(max(value))

screen = Screen()
prompt = True
bet = None
object_shape('turtle')
draw_finish_line()
align_turtle()
while prompt:
    bet = screen.textinput("Make your bet","Who will win the race? Enter a color: ").lower()
    if bet in timi_color:
        prompt=False
    else:
        print("Enter Valid color.")

while running():
    timi[randint(0, 4)].forward(5)

winner = winner()
if winner == timi_num[bet]:
    print(f"Congratulation, {bet} Won the match")
else:
    print(f"You Lost, Color {timi_color[winner]} Won the match")

screen.exitonclick()