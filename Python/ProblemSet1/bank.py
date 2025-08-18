'''
Problem Set 1
Program: Home Federal Savings Bank
Alexis Varas Ortiz
'''

def main():
    #takes input, removes whitespace and converts letters to lowercase
    hello = input("Greeting: ").strip().lower()

    #Calls function and passes input value
    greeting(hello)

def greeting(s):
    #Conditional statement to determine how much money is awarded based on the greeting
    #$0 for "hello", $20 if starts with "h", $100 if neither is true
    if s[0:5] == "hello":
        print ("$0")
    elif s[0:1] == "h":
        print ("$20")
    else:
        print ("$100")

main()
