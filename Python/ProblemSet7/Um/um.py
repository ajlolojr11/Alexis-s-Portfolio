# Problem Set 7
# Program: Regular, um, Expressions
# Alexis Varas Ortiz
# Description: Count how many instances of 'um' are in a string
import re
import sys


def main():
    try:
        print(count(input("Text: ")))
    # Catch any errors relating to the regex
    except re.error as e:
        print("Invalid regular expression...", e)
        sys.exit(1) #Exit with code 1 if exception is found

    sys.exit() # End program

def count(s):
    #Returning the number of matches if 'um' is found in the string
    if match := re.findall(r"\b(um)\b", s, re.IGNORECASE):
        return len(match)

    #If there is no match, return 0
    return 0

if __name__ == "__main__":
    main()
