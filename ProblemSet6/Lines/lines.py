# Problem Set 6
# Author: Alexis Varas Ortiz
# Program: Lines of Code
# Description: Read the provided program and count how many
# lines of code it has omiting any lines with white spaces or comments

import sys


def main():
    counter = 0

    try:
        #Assign the 2nd command-line argument if it's valid
        file_name = verify_arg(sys.argv[1])
    #Catch error if there is no second argument
    except IndexError:
        print("Too few command line arguments")
        sys.exit(1)

    counter = count_lines(file_name, counter)
    print(counter)


#Verify that the correct amount of argument are input and that
# the argument is a valid python file
def verify_arg(arg):
    #If there are more than 2 arguments display message and exit program
    if len(sys.argv) > 2:
        print("Too many command line arguments")
        sys.exit(1)

    #If the file name does not end in '.py' display message and exit program
    elif arg[-3:] != ".py":
        print("not a python file")
        sys.exit(1)

    return arg


#Open the file and count the lines of code
def count_lines(arg, count):
    try:
        with open(arg) as file:
            reader = file.readlines() #Read each line in the file

            #Go through each line and determine if it's empty, a comment or code
            for line in reader:
                char = line.lstrip()
                if line.isspace(): #if line is empty don't count it
                    continue
                elif char[0] == "#": #if line is a comment don't count it
                    continue
                else: #Add 1 to the counter if the previous 2 conditions are not met
                    count += 1

    #Catch error if file does not exist or not in the right directory
    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)

    #return the number of lines for main() to print
    return count


if __name__ == "__main__":
    main()
