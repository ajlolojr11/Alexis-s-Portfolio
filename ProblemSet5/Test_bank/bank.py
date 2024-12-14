"""
Problem Set 1
Program: Home Federal Savings Bank
Alexis Varas Ortiz
"""

import sys


def main():
    # takes input, removes whitespace and converts letters to lowercase
    hello = 1#input("Greeting: ")

    # Calls function and passes input value
    print(f"${value(hello)}")

    sys.exit(0)

def value(greeting):
    greeting = greeting.strip().title()

    # Conditional statement to determine how much money is awarded based on the greeting
    # $0 for "hello", $20 if starts with "h", $100 if neither is true
    if greeting[0:5] == "Hello":
        return 0
    elif greeting[0:1] == "H":
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
