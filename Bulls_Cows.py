'''
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Michaela Hronová
email: hronova.michaela09@gmail.com; hronova@ceps.cz
discord: Míša H.#5316
'''

import random

print("""Hi there!
-----------------------------------------------
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
-----------------------------------------------
Enter a number:
-----------------------------------------------""")

while True:
    secret_number = str(random.randint(1000,9999))
    secret_set = set(secret_number)
    if len(secret_number) == len(secret_set): # kontrola unikatnosti secret_number
        break

while True:
    number = input(">>> ")
    if not number.isnumeric():
        print("The value has to be a number. Please, try again.")
        continue
    if number[0] == "0":
        print("The number cannot start with zero. Please, try again.")
        continue
    if len(number) != 4:
        print("The number must contain 4 digits. Please, try again.")
        continue
    if len(set(number)) != len(number):
        print ("The number cannot contain duplicities. Please, try again.")
        continue

