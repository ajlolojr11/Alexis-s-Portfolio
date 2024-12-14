'''
Problem Set 1
Program: Math Interpreter
Alexis Varas Ortiz
'''

def main():
    #Take input from user. Remove whitespace. Create a list with each section that has a space in between
    expression = input("Expression: ").strip().split(" ")

    #Assign the respective index to each variable
    x = expression[0]
    y = expression[1]
    z = expression[2]
    
    #Evaluate string expression
    result = eval(x + y + z)

    #Convert 'result' to a float and round to the first decimal, then print
    print(float(round(result, 1)))

main()
