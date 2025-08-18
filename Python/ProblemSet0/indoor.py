'''
Problem Set 0
Program: Indoor Voice
Alexis Varas Ortiz
'''

def main():
    #Asking user to type a string and outputting
    words = input("Type words: ")
    print("You said: ", repeat(words))

def repeat(s):
    #Returning input and making it all lower case
    return s.lower()

main()
