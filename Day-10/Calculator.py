
from  art import logo
def add(n1, n2):
    """Function to add 2 numbers"""
    return n1 + n2

# TODO: Write out the other 3 function - subtract, multiply and divide.

def subtract(n1, n2):
    """Function to subtract 2 numbers"""
    return  n1 - n2

def multiply(n1, n2):
    """Function to multiply 2 numbers"""
    return  n1*n2

def divide(n1, n2):
    """Function to devide a numbers"""
    return  n1/n2

# TODO: Add these 4 function into a dictionary as the values. Keys = '+', '-' , '*', '/'
operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

# TODO: Use the dictionary operations to perform the calculations.
is_repeat = True
result = None
print(logo)

while is_repeat:

    if result is None:
        n1 = float(input("Type the first number: "))
    else:
        n1=result
    operator = input("Type a mathematical operator ('+','-','*' or '/') : ")
    n2 = float(input("Type the second number: "))
    result=operations[operator](n1,n2)
    print(f"Result: {n1} {operator} {n2} = {result}")
    repeat = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculator, "
                   f"\nor type 'e' to end calculator.")
    
    if repeat=='n':
        result = None
    elif repeat=='e':
        is_repeat=False