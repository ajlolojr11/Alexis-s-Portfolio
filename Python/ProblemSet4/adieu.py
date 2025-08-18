"""
Problem Set 4
Program: Adieu, Adieu
Programmer: Alexis Varas Ortiz
"""

import inflect

p = inflect.engine()
names = []


def main():
    try:
        #Prompt user for a name until ctrl + d is used to trigger exception and break loop
        while True:
            names.append(input("Name: "))
    except EOFError:
        print()
        #print out the list of names with the join() function from the inflect module
        print("Adieu, adieu, to " + p.join(names))


if __name__ == "__main__":
    main()
