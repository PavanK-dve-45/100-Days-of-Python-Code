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
idnx = None
while True:
    idnx = int(input("What do you chose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
    if -1<idnx<3:
        break
    print("Please enter valid value.") 
robo = random.choice(['rock','paper','scissors'])
choice = [rock,paper,scissors]
if idnx==0 and robo=='scissors':
    print(f"You chose:\n{rock}\nOpponent chose:\n{scissors}\nYou Won!!")
elif idnx==0 and robo=='paper':
    print(f"You chose:\n{rock}\nOpponent chose:\n{paper}\nYou Lost!!")
elif idnx==1 and robo=='rock':
    print(f"You chose:\n{paper}\nOpponent chose:\n{rock}\nYou Won!!") 
elif idnx==1 and robo=='scissors':
    print(f"You chose:\n{paper}\nOpponent chose:\n{scissors}\nYou Lost!!")
elif idnx==2 and robo=='paper':
    print(f"You chose:\n{scissors}\nOpponent chose:\n{paper}\nYou Won!!")
elif idnx==2 and robo=='rock':
    print(f"You chose:\n{scissors}\nOpponent chose:\n{rock}\nYou Lost!!")
else:
    print(f"You chose:\n{choice[idnx]}\nOpponent chose:\n{choice[idnx]}\nDraw Game.")
 