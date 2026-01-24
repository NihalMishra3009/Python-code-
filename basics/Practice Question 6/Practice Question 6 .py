"""
write a program to simulate a roll of a die/dice
A die has 6 faces with numbers 1 to 6 written on them
The program should randomly print a number between 1 and 6
"""

import random
print("Welcome to the game of rolling a dice.")

while True:
    choice = input("Would you like to play (Y,N): ")
    choice = choice.upper()
    choice = choice.strip()
    if choice == 'N':
        print("Your loss bye!")
        break
    elif choice == 'Y':
        number = random.randint(1,6)
        user_choice = int(input("Enter your choice number: "))
        if number == user_choice:
            print(" You got it ")
            print(f"You rolled a {number}")

        else :
            print("wrong choice")
            print(f"You rolled a {number}")
            print("Try again")
    else:
        print("Invalid input, please try again")
print("GAME OVER")

