'''
Problem Set 3
Program: Fuel Gauge
Alexis Varas Ortiz
'''

import sys


def main():
    while True: #loop to re-prompt user if input is not valid
        fraction = input("Fraction: ")
        fuel_level = (convert(fraction))
        print (gauge(fuel_level))
        break

    sys.exit()

def convert(fraction):
    x, y = fraction.split("/")

    if int(y) == 0:
        raise ZeroDivisionError("Cannot divide by 0")
    elif int(x) > int(y):
        raise ValueError("X is greater than Y")

    return (int(x)/int(y)) * 100

def gauge(fuel_level):
    #Handling output based on percent value
    if fuel_level <= 1:
        return "E"

    elif 99 <= fuel_level <= 100:
        return "F"

    elif fuel_level > 100: #If y is greater than x it should give a value over 100. Re-prompt user
        return False

    else:
        return f"{round(fuel_level)}%"


if __name__ == "__main__":
    main()
