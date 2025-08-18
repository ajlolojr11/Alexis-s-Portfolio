'''
Problem Set 0
Program: Faces
Alexis Varas Ortiz
'''

def main():
    words = input("Type words: ")
    print(convert(words))

def convert(e):
    #Converting emoticons to emojis and reassigning the new value back to variable
    e = e.replace(":)", "\N{slightly smiling face}")
    e = e.replace(":(", "\N{slightly frowning face}")
    return e

main()
