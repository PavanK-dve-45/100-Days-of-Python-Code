#Tip Calculator
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = True
people = None
while tip:
    tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
    if(tip == 12 or tip ==15 or tip == 10):
        people=int(input("How many people to split the bill? "))
        break
    print("Enter valid percentage!")
result = (bill + bill * (tip/100))/people
print(f"Each person should pay: ${round(result,2)}")

