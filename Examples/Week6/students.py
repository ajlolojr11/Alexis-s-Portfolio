'''
CSV FILE


#Students ver 1.0
def main():
    with open("students.csv") as file:
        for line in file:
            name, house = line.rstrip().split(",")
            print(f"{name} is in {house}")

if __name__ == "__main__":
    main()'''

'''#Students ver 2.0
def main():
    students = []

    with open("students.csv") as file:
        for line in file:
            name, house = line.rstrip().split(",")
            students.append(f"{name} is in {house}")

    for student in sorted(students):
        print(student)

if __name__ == "__main__":
    main()'''

'''#Students ver 3.0
def main():
    students = []

    with open("students.csv") as file:
        for line in file:
            name, house = line.rstrip().split(",")
            student = {"name": name, "house": house,}
            students.append(student)

    for student in sorted(students, key=lambda student: student["name"]):
        print(f"{student['name']} is in {student['house']}")


if __name__ == "__main__":
    main()'''

'''#Students ver 4.0
import csv

def main():
    students = []

    with open("students.csv") as file:
        reader = csv.reader(file)
        for name, home in reader:
            students.append({"name": name, "home": home})

    for student in sorted(students, key=lambda student: student["name"]):
        print(f"{student['name']} is from {student['home']}")


if __name__ == "__main__":
    main()'''

'''#Students ver 4.0
import csv

def main():
    students = []

    with open("students.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append(row)
            #students.append({"name": row["name"], "home": row["home"], "house": row["house"]})

    for student in sorted(students, key=lambda student: student["name"]):
        print(f"{student['name']} is from {student['home']} in {student['house']}")


if __name__ == "__main__":
    main()'''

#Students ver 4.0 - Write
import csv

def main():
    name = input("What's your name? ")
    home = input("Where's your home? ")

    with open("students.csv", "a") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "home"])
        writer.writerow({"name": name, "home": home})

if __name__ == "__main__":
    main()

