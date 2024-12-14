'''
Problem Set 3
Program: Grocery List
Alexis Varas Ortiz
'''

def main():
    grocery_list = dict() #initialize a dict

    #loop to keep prompting for itemsWorked 
    while True:
        try:
            item = input().upper() #convert input str to uppercase
        except EOFError:
            break

        if item in grocery_list:
            #if the key already exists add 1 to it's value pair
            grocery_list[item] += 1
        else:
            #else add the key and initialize the value to 1
            grocery_list[item] = 1


    #loop to print each key-value pair in dict
    for i in sorted(grocery_list):
        try:
            print(f"{grocery_list[i]} {i}")
        except KeyError: #exception to catch non-existent keys
            print(f"Key '{i}' not in dict")
            continue

main()






