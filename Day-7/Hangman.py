import random
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = ['interaction','product','storage','platform','meaning']
lives= 6
chosen_word = random.choice(word_list)
# print(chosen_word)

for i in chosen_word:
    print('_',end="")

correct_letters =[]
game_over = False
print()
while not game_over:
    guess= input('Guess a letter: ').lower()
    display=''

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += '_'
    print(display)

    if '_' not in display:
        game_over = True
        print('You Won!..')
    elif guess not in chosen_word:
        lives-=1
    if lives==0:
        print('You Lost.')
        game_over= True
    print(stages[lives])
    