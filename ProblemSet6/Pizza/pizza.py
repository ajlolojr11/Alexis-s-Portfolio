# Problem Set 6
# Author: Alexis Varas Ortiz
# Program: Pizza Py
# Description: Displays a table of data from a specified file
import sys
import csv
from tabulate import tabulate


def main():
    try:
        # Assign the 2nd command-line argument if it's valid
        file_name = verify_arg(sys.argv[1])
    # Catch error if there is no second argument
    except IndexError:
        print("Too few command line arguments")
        sys.exit(1)

    #Prints the list retuned from the function in a table format
    print(tabulate(tabulate_data(file_name), headers="keys", tablefmt="grid"))

    sys.exit() #End program

def verify_arg(arg):
    # If there are more than 2 arguments display message and exit program
    if len(sys.argv) > 2:
        print("Too many command line arguments")
        sys.exit(1)

    # If the file name does not end in '.py' display message and exit program
    if arg[-4:] != ".csv":
        print("Not a CSV file")
        sys.exit(1)

    return arg


def tabulate_data(file):
    menu = [] #list to store the data from the file

    try:
        with open(file) as data:
            reader = csv.DictReader(data)

            #Add each row to the menu list
            for row in reader:
                menu.append(row)

    # Catch error if file does not exist or not in the right directory
    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)

    #Return the data to main() for printing
    return menu


if __name__ == "__main__":
    main()
