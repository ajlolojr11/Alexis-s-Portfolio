# Problem Set 6
# Author: Alexis Varas Ortiz
# Program: Scourgify
# Description: Takes the name field of a csv file and splits the field into
# first and last names. Then writes the first and last names into their own
# columns in a new file
import sys
import csv


def main():
    try:
        # Assign the 2nd command-line argument if it's valid
        input, output = verify_arg(sys.argv[1], sys.argv[2])
    # Catch error if there is no second argument
    except IndexError:
        print("Too few command line arguments")
        sys.exit(1)

    scourgify(input, output)
    sys.exit(0)  # End program


# Verify that the correct amount of arguments are input and that
# the arguments are a valid csv file
def verify_arg(arg1, arg2):
    # If there are more than 2 arguments display message and exit program
    if len(sys.argv) > 3:
        print("Too many command line arguments")
        sys.exit(1)

    # If the file name does not end in '.csv' display message and exit program
    if arg1[-4:] != ".csv" and arg2[-4:] != ".csv":
        print("Not a CSV file")
        sys.exit(1)

    return arg1, arg2


#Reads input file, converts name field and writes to new file
def scourgify(in_, out_):
    try:
        #Opening the input, output files in read and write mode respectively
        with open(in_) as data_in, open(out_, "w") as data_out:
            reader = csv.DictReader(data_in)
            writer = csv.DictWriter(data_out, fieldnames=["first", "last", "house"])

            writer.writeheader() #write headers before adding the rest of the data

            # Splits each name into first and last and writes them into the new file along with the house
            for row in reader:
                last, first = row["name"].split(", ")
                writer.writerow({"first": first, "last": last, "house": row["house"]})

    # Catch error if file does not exist or not in the right directory
    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)


if __name__ == "__main__":
    main()
