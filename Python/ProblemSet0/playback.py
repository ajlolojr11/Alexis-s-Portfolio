'''
Problem Set 0
Program: Playback
Alexis Varas Ortiz
'''

def main():
    words = input("Type a sentence: ")
    print(slowdown(words))

def slowdown(s):
    return s.replace(" ", "...")

main()
