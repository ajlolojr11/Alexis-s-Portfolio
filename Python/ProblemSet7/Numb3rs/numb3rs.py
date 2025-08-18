# Problem Set 7
# Program: Numb3rs
# Alexis Varas Ortiz
# Description: Validate an ip address
import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))
    sys.exit()


def validate(ip):
    if match := re.search(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", ip):
        for n in match.groups():
            if not 0 <= int(n) <= 255:
                return False
            else:
                continue
    else:
        return False

    return True


if __name__ == "__main__":
    main()
