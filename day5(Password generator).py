#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#our code
#easy level(in order of letters,symbols,numbers->it@#67)
# password="" #empty intailly
# for char in range(1,nr_letters+1):
#     password+=random.choice(letters)
# for char in range(1,nr_symbols+1):
#     password+=random.choice(symbols)
# for char in range(1,nr_numbers+1):
#     password+=random.choice(numbers)
# print(password)

#hard level(in any order for eg:hi90ik#i@)
password=[] #instead of string we pass list
for char in range(1,nr_letters+1):
    password+=random.choice(letters) #you can also use password=password.append(random.choice(letters))
for char in range(1,nr_symbols+1):
    password+=random.choice(symbols)
for char in range(1,nr_numbers+1):
    password+=random.choice(numbers)
#to suffle the ordering
print(password)
random.shuffle(password)
print(password)
#for make it into string
passwrd=" "
for char in password:
    passwrd+=char
print(f"The password suggested is {passwrd}")
