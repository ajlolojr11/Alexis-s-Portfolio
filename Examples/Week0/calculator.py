'''
#CALCULATOR PROGRAM VER 1.0
x = float(input("What's x? "))
y = float(input("What's y? "))

z = x/y

print(f"{z:.2f}")
'''

##CALCULATOR PROGRAM VER 2.0

def main():
    x = int(input("What's x? "))
    print ("x squared is", square(x))

def square(num):
    return pow(num, 2)

main()
