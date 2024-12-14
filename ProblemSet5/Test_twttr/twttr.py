"""
Problem Set 2
Program: Just setting up my twttr
Author: Alexis Varas Ortiz
"""

vowels = "AaEeIiOoUu"

def main():
    string = input("Input: ")
    print("Output: ", shorten(string))


def shorten(string):
    global vowels
    words = ""

    for char in string:
        if char in vowels:
            continue
        else:
            words += char

    return words


if __name__ == "__main__":
    main()
