'''
#Hogwarts example Version 1.0
def main():
    students = ["Hermione", "Harry", "Ron"]

    for student in students:
        print(student)

main()
'''

'''
#Hogwarts example Version 2.0
def main():
    students = ["Hermione", "Harry", "Ron"]

    for i in range(len(students)):
        print(i + 1, students[i])

main()
'''
'''
#Hogwarts example Version 3.0
def main():
    students = {
        "Hermione": "Gryffindor",
        "Harry": "Gryffindor",
        "Ron": "Gryffindor",
        "Draco": "Slytherin"
        }

    for student in students:
        print(student, students[student], sep=", ")

main()
'''

#Hogwarts example Version 4.0
def main():
    students = [
        {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
        {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
        {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell Terrier"},
        {"name": "Draco", "house": "Slytherin", "patronus": None}
    ]

    for student in students:
        print(student["name"], student["house"], student["patronus"], sep=", ")

main()
