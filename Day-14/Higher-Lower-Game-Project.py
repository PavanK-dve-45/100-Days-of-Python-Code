from  art import  logo,vs
from game_data import data
import random
import os
score = 0
print(logo)
def pick_any_one():
    return random.choice(data)

def check_answer(set1,set2):
    return True if set1['follower_count'] > set2['follower_count'] else False
def higher_lower(set1, set2, total):
    print(f"Compare A: {set1['name']}, {set1['description']}, {set1['country']}")
    print(vs)
    print(f"Compare B: {set2['name']}, {set2['description']}, {set2['country']}")
    user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    result = check_answer(set1, set2) if user_choice=='a' else check_answer(set2,set1)
    if result:
        os.system('cls')
        total +=1
        print(f"You're right! Current score: {total}")
        dist_list = [set2,set1]
        new_set1 = random.choice(dist_list)
        new_set2 = pick_any_one()
        while new_set1==new_set2:
            new_set2=pick_any_one()
        higher_lower(new_set1, new_set2, total)
    else:
        os.system('cls')
        print(logo)
        print(f"Sorry, that's wrong. Final score: {total}")
        return

data1 = pick_any_one()
data2 = pick_any_one()
while data1==data2:
    data2=pick_any_one()
higher_lower(data1,data2,score)





