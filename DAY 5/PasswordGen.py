import random
print("Welcome to Shirin's Password Generator!")
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

numbers = [
    '0', '1', '2', '3', '4',
    '5', '6', '7', '8', '9'
]

symbols = [
    '!', '#', '$', '%', '&',
    '(', ')', '*', '+'
]
letter_count = int(input("How many letters would you like in your password?\n"))
num_count = int(input("How many numbers would you like in your password?\n"))
symbol_count = int(input("How many symbols would you like in your password?\n"))
password = []
for i in range(letter_count):
    password.append(random.choice(letters))
for j in range(num_count):
    password.append(random.choice(numbers))
for k in range(symbol_count):
    password.append(random.choice(symbols))
res = random.shuffle(password)
print(f"Your password is: {''.join(password)}"  )