from  art import  logo
import random
print(logo)
def winner(list1,list2):
    """Returns the String 'You win' or 'You Lose' """
    sum1= sum(list1)
    sum2= sum(list2)
    if sum1==sum2:
        return 'Draw'
    elif sum1<22 and sum2<22:
        return 'You win' if sum1-sum2>0 else 'You Lose'
    elif sum1>21 or sum2>21:
        return 'You win' if sum1-21<sum2-21 else 'You Lose'

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def blackjack():
    play_on = True
    play_card =[]
    computer_card = []
    play_card.append(random.choice(cards))
    while play_on:
        play_card.append(random.choice(cards))
        computer_card.append(random.choice(cards))
        print(f"Your cards: {play_card}\nComputer's card {computer_card} ")
        another_card = input("Type 'y' to get another card, type 'n' to pass: " )
        if another_card=='y':
            continue
        elif another_card=='n':
            computer_card.append(random.choice(cards))
            print(f"Your final hand: {play_card}\nComputer's final hand: {computer_card}")
            print(winner(play_card,computer_card))
        repeat=input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
        play_on = False if repeat=='n' else True
        if repeat=='y':
            blackjack()

blackjack()
