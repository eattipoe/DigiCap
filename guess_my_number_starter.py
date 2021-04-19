"""
File: guessmynumber.py
----------------------
This program checks if a user's guess of a number matches that guessed by the computer
"""

import random
# use code below  to generate a random integer between 30 and 50 for example
#print(random.randint(30, 50))

# ********************************** YOUR CODE GOES BELOW HERE *********************************************************
print("I am thinking of a number between 1 and 99")
#Generate a random number between 1 and 99
random_number = random.randint(1, 99)

while True:
    try:
        # User enter a guess number
        guess_number = int(input('Enter a guess: '))
        # Check if the number is between 1 and 99

    except ValueError:
        print('Please input valid integer between(1 and 99)')

    else:
        if 1 <= guess_number <= 99:
            #display message to user if the number is lower
            if guess_number > random_number:
                print("Your Guess is TOO HIGH, make another input")

            #display message to user if the numner is lower    
            elif guess_number < random_number:
                print("Your Guess is TOO LOW, Make another input")
                
            else:
                print("Congrat! The number was:", random_number)
                break
            #end of code 

