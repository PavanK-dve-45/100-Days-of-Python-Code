#Tip Calculator
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = True
split_count = None
while tip:
    tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
    if(tip == 12 or tip ==15 or tip == 10):
        split_count=int(input("How many people to split the bill? "))
        break
    print("Enter valid percentage!")
split_bill = (bill + bill/tip)/split_count 
print("Each person should pay: $",split_bill)

