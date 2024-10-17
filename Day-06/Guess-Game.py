import random
num=random.randint(0,9)
count=3
while True:
    user_num=int(input("Guess a number between 0-9: "))
    hint = 'Greater' if user_num>num else 'Lesser'
    count-=1
    if num==user_num:
        print("You Won!..")
        break
    elif count==0:
        print("You Lost..")
        break
    else:
        print(f"Hint: Your number is {hint} than actual number.\nYou have {count} attempt's left")
    
        
