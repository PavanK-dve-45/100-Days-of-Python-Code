import  random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print('Welcome to the Python Password Generator!')
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How may symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

password=""
newpassword =[]
for i in range(nr_letters):
    newpassword.append(random.choice(letters))
for i in range(nr_numbers):
    newpassword.append(random.choice(numbers))
for i in range(nr_symbols):
    newpassword.append(random.choice(symbols))

random.shuffle(newpassword)
for char in newpassword:
    password+=char

print(f"Password: {password}")