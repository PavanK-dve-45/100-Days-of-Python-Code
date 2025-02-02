from turtle import Turtle,Screen
import  random

is_race_on = None
screen = Screen()
screen.setup(500,400)
user_bet = screen.textinput("Make your bet","Which turtle will win the race? Enter a color: ")
colors =['red','orange','yellow','green','blue','purple']
y_pos = [-10,20,-40,50,-70,80]
all_turtles = []

for index in range(0,6):
    pet = Turtle(shape='turtle')
    pet.color(colors[index])
    pet.penup()
    pet.goto(-230, y_pos[index])
    all_turtles.append(pet)

if user_bet:
    is_race_on= True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor()>230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've Won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've Lost!, The {winning_color} turtle is the winner.")
                is_race_on = False
        turtle.forward(random.randint(1,10))


screen.exitonclick()