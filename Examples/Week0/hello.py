'''
#HELLO PROGRAM VER 1.0

#Ask user for their name
#Remove whitespace from string and capitalize user's name
name = input("What's your name? ").strip().title()

#Split user's name in first and last name
first, last = name.split(" ")


#Say hello to user
print(f"Hello, {first}")
'''
'''
#HELLO PROGRAM VER 2.0

def hello(to="world"):
    print(f"Hello, {to}")

hello()
name = input("What's your name? ")
hello(name)
'''

#HELLO PROGRAM VER 3.0

def main():
    name = input("What's your name? ")
    hello(name)

def hello(n):
    print("Hello, ", n)

main()
