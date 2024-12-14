'''
Problem Set 2
Program: camelCase
Alexis Varas Ortiz
'''

def main():
    #Asks user for a variable name in camelCase format
    variable = input("camelCase: ")
    print("snake_case: ", end="")

    #Loop to iterate through every letter in the variable
    for letter in variable:

        #Checks to see what letter is uppercased
        #Converts it to lower case and adds a underscore before it
        if letter.isupper():
            print("_" + letter.lower(), end="")

        #If letter is not uppercase, just print the letter
        else:
            print(letter, end="")
    
    print()

main()

