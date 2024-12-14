'''
#Cat program Ver 1.0

def main():
    i = 0
    while i < 3:
        print("meow")
        i += 1

main()
'''
'''
#Cat program Ver 2.0

def main():
    for _ in range(3):
        print("meow")

main()
'''
'''
#Cat program Ver 3.0

def main():
    print("meow\n" * 3, end="")

main()
'''
'''
#Cat program Ver 4.0

def main():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break

    for _ in range(n):
        print("meow")

main()
'''

#Cat program Ver 5.0

def main():
    number = get_number()
    meow(number)

def get_numbner():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n

def meow(n):
    for _ in range(n):
        print("meow")

main()
