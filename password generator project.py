import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_numbers = int(input("How many numbers would you like?\n" ))
nr_symbols = int(input("How many symbols would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
"""
for let in range(nr_letters):
  print(random.choice(letters), end = " ")
for sym in range(nr_symbols):
  print(random.choice(symbols), end = " ")
for num in range(nr_numbers):
  print(random.choice(numbers), end = " ")
"""

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password = " "

for let in range(nr_letters):
  random_let = random.choice(letters)
  password += random_let

for sym in range(nr_symbols):
  random_sym = random.choice(symbols)
  password += random_sym

for let in range(nr_numbers):
  random_num = random.choice(numbers)
  password += random_num

new_password = list(password)
random.shuffle(new_password)

pass1 = " "

for pass in new_password:
  pass1 += pass
print(f"Your new password is {pass1}.")