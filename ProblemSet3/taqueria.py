'''
Problem Set 3
Program: Felipe's taqueria
Alexis Varas Ortiz
'''
def main():
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
        }
    total = 0

    while True:
        try:
            item = menu[input("Item: ").title()]
        except KeyError:
            continue #reprompt
        except EOFError:
            print("\n")#add new line when ending program via ctrl + d
            break
        else:
            total += item #add price of item to running total
            print(f"Total: ${total:.2f}")#format variable to always include 2 decimal spaces, even if 00

main()
