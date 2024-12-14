"""
Problem Set 4
Program: Guessing Game
Programmer: Alexis Varas Ortiz
"""

import random
import sys

def main():
    #Prompt user for a level between 1 - 100
    while True:
        #Validate that input is a number
        try:
            level = int(input("Level: "))
        #If input is not a number reprompt
        except ValueError:
            continue

        #Validate that level is within 1 and 100. Reprompt if not
        if 1 > level > 100:
            continue
        else:
            break

    #Prompt user to guess a number
    while True:
        #Validate that input is a number
        try:
            guess = int(input("Guess: "))
        except ValueError:
            continue

        #Validate that guess is a positive number. Reprompt if not
        if guess < 1:
            continue
        #Call function to compare the guess. Reprompt if incorrect guess
        #If guess is correct break loop
        elif generate(level, guess) == False:
            break

    sys.exit() #End program

#Function to generate a random number within the set range and compare it to the guessed number
def generate(l, g):
    gen_level = random.randint(1, l)

    #Print out the respective string relative to each condition
    if g < gen_level:
        print("Too small!")
    elif g > gen_level:
        print("Too large!")
    else:
        print("Just right!")
        #Return false if the guess is right to exit the loop
        return False

    #If guess was not correct loop will continue
    return True


if __name__ == "__main__":
    main()
