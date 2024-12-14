"""
Problem Set 4
Program: Emojize
Programmer: Alexis Varas Ortiz
"""

import emoji


def main():
    codes = input("Input: ")
    print(emoji.emojize(codes, language="alias"))


if __name__ == "__main__":
    main()
