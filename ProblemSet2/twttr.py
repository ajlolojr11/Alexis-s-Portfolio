'''
Problem Set 2
Program: Just setting up my twttr
Alexis Varas Ortiz

Version 1.0
def main():
    remove_vowels(input("Input: "))
    print()

def remove_vowels(words):
    print("Output: ", end="")

    for letters in words:
        match letters:
            case "a"|"e"|"i"|"o"|"u"|"A"|"E"|"I"|"O"|"U":
                continue
            case _:
                print(letters, end="")

main()
'''

#Version 2.0
def main():
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    string = (input("Input: "))

    print("Output: ", end="")

    #loop goes through each character from the user's input
    for letter in string:

        #Checks if the character is a vowel. If so, it skips to the next character without printing it
        if letter in vowels:
            continue
        else:
            print(letter, end="")

    print()

main()
