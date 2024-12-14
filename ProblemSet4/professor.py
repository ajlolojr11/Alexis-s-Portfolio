"""
Problem Set 4
Program: Little Professor
Author: Alexis Varas Ortiz
"""

import random
import sys

score = 0


def main():
    global score
    count = 0
    level = get_level()

    #Loop to generate 10 problems
    while count < 10:
        x = generate_integer(level)
        y = generate_integer(level)
        get_answer(x, y)

        #Add 1 to counter once done with a problem
        count += 1

    print("Score: ", score)
    sys.exit() #Exit program


def get_level():
    while True:
        # Prompt user for a level 1, 2 or 3. Reprompt if non-numeric input
        try:
            level = int(input("Level: "))
        except ValueError:
            continue

        # Validate that level is within 1 and 3. Reprompt if not
        if 1 <= level <= 3:
            return int(level)


def generate_integer(level):
    # Return a random interger relative to the level selected
    # Raise exception if not 1, 2, or 3
    match level:
        #Single digit
        case 1:
            return random.randint(0, 9)

        #Double digits
        case 2:
            return random.randint(10, 99)

        #Triple digits
        case 3:
            return random.randint(100, 999)

        #Invalid or non-numeric level
        case _:
            raise ValueError("Level outside of range")


def get_answer(x, y):
    global score
    tries = 0 #Reset tries after every problem

    #Reprompt user up to 3 times if answer is incorrect
    while tries < 3:
        #If answer is non-numeric print 'EEE' and reprompt
        try:
            answer = int(input(f"{x} + {y} = "))
        except ValueError:
            print("EEE")
            tries += 1
            continue

        #If incorrect print 'EEE'and add 1 to the number of tries
        if answer != (x + y):
            print("EEE")
            tries += 1

            #If incorrect 3 times print the correct answer and continue to the next problem
            if tries == 3:
                print(f"{x} + {y} = {x + y}")
                return

        #If answer is correct add 1 to the score and continue to the next problem
        elif answer == (x + y):
            score += 1
            return


if __name__ == "__main__":
    main()
