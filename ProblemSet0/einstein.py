'''
Problem Set 0
Program: Einstein
Alexis Varas Ortiz
'''

def main():
    mass = int(input("Enter mass: "))
    print("E: ", joules(mass))

def joules(m):
    return m * pow(300000000, 2)

main()
