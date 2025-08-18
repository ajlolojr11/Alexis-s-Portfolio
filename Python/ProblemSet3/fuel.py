'''
Problem Set 3
Program: Fuel Gauge
Alexis Varas Ortiz
'''

def main():
    while True: #loop to re-prompt user if input is not valid
        fraction = input("Fraction: ").split(sep="/")

        try:
            #calls function convert while converting the index values to interger and passing to arguments
            fuel_level = (convert(int(fraction[0]), int(fraction[1])))
        except(ValueError, ZeroDivisionError):
            #If these exceptions occurr go to next Loop iteration
            continue
        else:
            #Handling output based on percent value
            if fuel_level <= 1:
                print("E")
                break

            elif 99 <= fuel_level <= 100:
                print("F")
                break

            elif fuel_level > 100: #If y is greater than x it should give a value over 100. Re-prompt user
                continue

            else:
                print (f"{round(fuel_level)}%")
                break

def convert(x, y):
    #Convert fraction to percent
    return (x/y) * 100

main()
