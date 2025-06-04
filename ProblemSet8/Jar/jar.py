# Problem Set 8
# Program: Cookie jar
# Alexis Varas Ortiz
# Description: Create a cookie jar(class) to store coockies

class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        #Checks capacity is a positive no-zero integer
        if n is not int and n < 1:
            raise ValueError("Invalid number of cookies")
        #Checks that deposit does not exceed capacity
        if self._size + n > self._capacity:
            raise ValueError("Too many cookies!")
        self._size += n #adds deposit amount if no raised errors

    def withdraw(self, n):
        #Checks capacity is a positive no-zero integer
        if n is not int and n < 1:
            raise ValueError("Invalid number of cookies")
        #Checks that withdraw does not make capacity negative
        if self._size - n < 0:
            raise ValueError("Ran out of cookies!")
        self._size -= n #removes withdraw amount if no raised errors

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

#active testing class properties and methods
'''
def main():
    jar = Jar()
    jar.deposit(10)
    print(f"Cookies in the jar: {jar}\n"
          f"Jar capacity: {jar.capacity}")
    jar.withdraw(2)
    print(f"Cookies in the jar: {jar}\n"
          f"Jar capacity: {jar.capacity}")


if __name__ == "__main__":
    main()
'''
