"""
Problem Set 4
Program: Frank, Ian and Glen’s Letters
Programmer: Alexis Varas Ortiz
"""

from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
font_list = figlet.getFonts()  # assigns all fonts into a list


def main():
    validate()
    string = input("Input: ")
    print(convert(string))


def validate():
    arg = len(sys.argv)

    # verify there are either none or 2 command-line arguments
    if arg != 1 and arg != 3:
        sys.exit("Invalid usage")

    if arg == 3:
        # verify first argument being inputted correctly
        if sys.argv[1] != "-f" and sys.argv[1] != "--font":
            sys.exit("Invalid usage")
        # verify the second argument is a valid font type
        if sys.argv[2] not in font_list:
            sys.exit("Invalid usage")

    return


def convert(s):
    # Determine what font to use depending on how many arguments where passed
    if len(sys.argv) == 3:
        figlet.setFont(font=sys.argv[2])
    else:
        figlet.setFont(font=random.choice(font_list))

    return figlet.renderText(s)


if __name__ == "__main__":
    main()
