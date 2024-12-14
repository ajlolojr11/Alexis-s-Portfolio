'''
#Mario program Version 1.0

def main():
    print_column(3)

def print_column(height):
    for _ in range(height):
        print("#")

main()
'''
'''
#Mario program Version 2.0

def main():
    print_row(4)

def print_row(width):
     print("| ? |" * width)

main()
'''
'''
#Mario program Version 3.0

def main():

    print_square(3)

def print_square(size):

    #For each row in square
    for i in range(size):

        #For each brick in row
        for j in range(size):

            #print brick
            print("#", end="")
        print()


main()
'''

#Mario program Version 3.0

def main():

    print_square(3)

def print_square(size):

    for i in range(size):
        print_row(size):

def print_row(width):
    print("#" * width)


main()
