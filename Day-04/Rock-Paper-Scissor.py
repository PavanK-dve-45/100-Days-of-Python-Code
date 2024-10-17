import random
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
user = None
while True:
    user = int(input("What do you chose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
    if -1<user<3:
        break
    print("Please enter valid value.") 

robo= random.randint(0,2)
choice = [rock,paper,scissors]
if user==0 and robo== 3 or user==1 and robo==0 or user==2 and robo==1:
    print(f"You chose:\n{choice[user]}\nOpponent chose:\n{choice[robo]}\nYou Won!!")

elif user == robo:
    print(f"You chose:\n{choice[user]}\nOpponent chose:\n{choice[robo]}\nDraw Game.")

else:
    print(f"You chose:\n{choice[user]}\nOpponent chose:\n{choice[robo]}\nYou Lost.")
    