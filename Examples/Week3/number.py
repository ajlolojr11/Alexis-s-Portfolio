'''#Number program version 1.0

while True:
    try:

        x = int(input("What's x? "))

    except ValueError:
        print ("x is not an integer")

    else:
        break

print(f"x is {x}")'''


'''
#Number program version 2.0(with function/condensed)

def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            return int(input("What's x? "))

        except ValueError:
            print ("x is not an integer")

main()
'''

#Number program version 3.0 (With pass)

def main():
    x = get_int("What's x? ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))

        except ValueError:
            pass

main()
