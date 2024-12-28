'''
TEXT FILE


#Write to file
def main():
    name = input("What's your name? ")

    with open("names.txt", "a") as file:
        file.write(name + "\n")


if __name__ == "__main__":
    main()'''

'''#Read file
def main():
    with open("names.txt", "r") as file:
        lines = file.readlines()

    for line in lines:
        print(f"hello, {line.strip()}")


if __name__ == "__main__":
    main()'''


'''#Read file ver 2.0
def main():
    names = []

    with open("names.txt") as file:
        for line in file:
            names.append(line.rstrip())

    for name in sorted(names):
        print(f"hello, {name}")

if __name__ == "__main__":
    main()'''


#Read file ver 3.0
def main():
    with open("names.txt") as file:
        for line in sorted(file):
            print(line.rstrip())


if __name__ == "__main__":
    main()
