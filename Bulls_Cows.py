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

number = input(">>> ")

