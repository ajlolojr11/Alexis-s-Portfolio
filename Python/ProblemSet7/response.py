# Problem Set 7
# Program: Response Validation
# Alexis Varas Ortiz
# Description: Validate an email address
from validators import email, ValidationError
import sys


def main():
    try:
        print(validate(input("Email address: ")))
    except ValidationError as e:
        print("An error occurred...", e)
        sys.exit(1) #Exit with code 1 if exception is found

    sys.exit() #End program

def validate(s):
    if email(s): #Validate if string is an email
        return "Valid"

    return "Invalid" #Return invalid if string is not a valid email


if __name__ == "__main__":
    main()
