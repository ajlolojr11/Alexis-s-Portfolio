'''
Problem Set 1
Program: Deep Thought
Alexis Varas Ortiz
'''

def main():
    four_two = input("What is the Answer to the Great Question of Life, the Universe and Everything? ")

    #Calling function that prints the answer and transfers the user's input
    #Removes whitespace and converts all letters to lowecase
    answer(four_two.strip().lower())

def answer(a):

    #Prints "Yes" if the user's input was 42, forty-two or forty two
    #Prints "No" for everything else
    match a:
        case "42" | "forty-two" | "forty two":
            print ("Yes")
        case _:
            print ("No")

main()
