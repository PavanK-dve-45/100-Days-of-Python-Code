import random
from art import logo

EASY_LEVEL = 10
HARD_LEVEL = 5
def check_answer(guess,answer,count):
    if guess==answer:
        print(f"You got it! The answer was {answer}")
        return True
    if guess!=answer:
        print("Too high." if guess>answer else "Too low.")
        return count -1
        

def chose_difficulty(difficulty):
    return HARD_LEVEL if difficulty == "hard" else EASY_LEVEL

def guess_game():
    '''Guess the number game logic'''
    print(logo)
    attempts=None
    is_continue_game=True
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    correct_answer = random.randint(1,100)
    difficulty = input("Chose a difficulty. Type 'easy' or 'hard': ").lower()
    attempts = chose_difficulty(difficulty)
    guess = 0
    while guess!=correct_answer:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        attempts = check_answer(guess,correct_answer,attempts)
        if not attempts:
            print(f"You Lose. The correct answer was {correct_answer}")
            return
    new_game = input("Do you want to play guess game? Type 'y' or 'n': ").lower()
    if new_game=='y':
        guess_game()

guess_game()





   

