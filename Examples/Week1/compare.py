'''
#Compare Ver 1.0
def main():
    x = int(input("Whats's x? "))
    y = int(input("Whats's y? "))

    #Compares x and y and determines if x is less, greater or equal to y
    if x < y:
        print("x is less than y")
    elif x > y:
        print("x is greater than y")
    else:
        print("x is equal to y")

main()
'''

#Compare Ver 2.0
def main():
    x = int(input("Whats's x? "))
    y = int(input("Whats's y? "))

    if x != y:
        print ("x is not equal to y")
    else:
        print ("x is equal to y")

main()
