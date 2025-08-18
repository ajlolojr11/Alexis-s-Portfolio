'''
Problem Set 2
Program: Vanity Plates
Alexis Varas Ortiz
'''

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    valid = True

    #Checked to see if any characters are non-letters/numbers
    for char in s:
        if char.isalnum() != True:
            valid = False

    #Checkes that plate is between 2-6 characters long
    if not 2 <= len(s) <= 6:
        valid = False

    #Checkes first two character to see if they are numbers
    elif s[0].isdigit() or s[1].isdigit():
        valid = False

    #Checks if plate has numbers and if they are at the end
    for num in s:
        if num.isdigit() and num != "0":
            num = s.split(num, 1)
            num = num[1]

            if num.isdigit() != True:
                valid = False

            break

        elif num.isdigit() and num == "0":
            valid = False
            break



    return valid





main()
