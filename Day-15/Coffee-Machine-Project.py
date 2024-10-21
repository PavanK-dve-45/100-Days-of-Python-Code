from coffee_data import MENU,resources,value

resource = resources
menu = MENU

def display_resource(res):
    """Displays Resources Available"""
    print(f"Water: {res['water']}ml\nMilk: {res['milk']}ml\nCoffee: {res['coffee']}g\nMoney: ${res['cost']}")

def insert_coin():
    """Counts and validates total coins values"""
    print("Please insert coins.")
    quarters = float(input("How many quarters?: "))
    dimes = float(input("How many dimes?: "))
    nickles = float(input("How many nickles?: "))
    pennies = float(input("How many pennies?: "))
    return value['Quarter']*float(quarters)+ value['Dime']*dimes+value['Nickel']*nickles+value['Penny']*pennies

def check_resource(ingredients):
    """Checks Resource Available"""
    for i in ingredients:
        if resource[i]<ingredients[i]:
            print(f"Sorry there is not enough {i}")
            return False
    return True

def can_buy(cost, choice):
    """Checks if user can afford or not"""
    if cost >= menu[choice]['cost']:
        print(f"Here is ${round(cost - menu[choice]['cost'], 2)} in change.\nHere is your {choice}🍵 Enjoy!")
        resource['cost'] += menu[choice]['cost']
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def update_resource(ingredients):
    """Updates resource available"""
    for i in ingredients:
        resource[i] = resource[i]-ingredients[i]
    return

Coffee_Machine = True
while Coffee_Machine:
    #TODO-2 Take input from user
    user_choice = input("What would you like? (mocha/leberica/espresso): ").lower()
    if user_choice=='report':
        #TODO-1 Print Report
        display_resource(resource)
    elif user_choice=='clear':
        Coffee_Machine = False
    else:
        print(f"Thanks for choosing {user_choice}.")
        if check_resource(menu[user_choice]['ingredients']):
            if can_buy(insert_coin(),user_choice):
                update_resource(menu[user_choice]['ingredients'])
