'''
Problem Set 2
Program: Coke Machine
Alexis Varas Ortiz
'''

def main():
    #Set coke price and pass value to function
    price = 50
    buy_coke(price)

def buy_coke(owed):

    #Loop that will run while the price owed is greater than 0
    while owed > 0:

        print(f"Amount Due: {owed}")

        #Input from user. What coin denomination is being inserted
        coins = int(input("Insert coins: "))

        #Match case to verify only value being accepted is 25, 10 or 5
        match coins:
            case 25 | 10 | 5:
                #Subtracts the coins from the total price
                owed -= coins
                print()

    #Will show how much change is owed after the full price is met
    print(f"Change Owed: {abs(owed)}")


main()

