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

def check_unique_digits(string: str) -> bool:
    """returns True if there are no duplicities""" #docstring
    if len(string) == len(set(string)):
        return True
    else: 
        return False

while True:
    secret_number = str(random.randint(1000,9999))
    if check_unique_digits(secret_number): 
        break

guess_number_count = 0

while True:
    guess_number = input(">>> ")
    if not guess_number.isnumeric():
        print("The value has to be a number. Please, try again.")
        continue
    if guess_number[0] == "0":
        print("The number cannot start with zero. Please, try again.")
        continue
    if len(guess_number) != 4:
        print("The number must contain 4 digits. Please, try again.")
        continue
    if not check_unique_digits(guess_number):
        print ("The number cannot contain duplicities. Please, try again.")
        continue
    guess_number_count += 1

    # Vyhodnoceni tipu uzivatele
    
    if guess_number == secret_number:
        print(f"Correct, you've guessed the right number in {guess_number_count} guesses!")
        break
   
    bulls_count = 0
    for i in range(0, len(guess_number)):
        if guess_number[i] == secret_number[i]:
            bulls_count += 1
    if bulls_count != 1:
        bull_string = f"{bulls_count} bulls"
    else:
        bull_string = f"{bulls_count} bull"
    
    cows_count = 0
    for digit in guess_number:
        if digit in secret_number:
            cows_count += 1
    cows_count -= bulls_count
    if cows_count != 1:
        cow_string = f"{cows_count} cows"
    else:
        cow_string = f"{cows_count} cow"
    
    print(f"{bull_string}, {cow_string}")

    




