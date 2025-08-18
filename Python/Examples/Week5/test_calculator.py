'''
#test calculator ver 1.0
from calculator import square

def main():
    test_square()

def test_square():
    if square(2) != 4:
        print("2 squared was not 4")

    if square(3) != 9:
        print("3 squared was not 9")

    else:
        print("Tests where successful!")

if __name__ == "__main__":
    main()'''

'''
#test calculator ver 2.0
from calculator import square

def main():
    test_square()

def test_square():
    try:
        assert square(2) == 4
    except AssertionError:
        print ("2 square was not 4")

    try:
        assert square(3) == 9
    except AssertionError:
        print ("3 square was not 9")

    try:
        assert square(-2) == 4
    except AssertionError:
        print ("-2 square was not 4")

    try:
        assert square(-3) == 9
    except AssertionError:
        print ("-3 square was not 9")

    try:
        assert square(0) == 0
    except AssertionError:
        print ("0 square was not 0")

if __name__ == "__main__":
    main()'''

'''
#test calculator ver 3.0 (generate random test)
from calculator import square
import random

def main():
    test_square()

def test_square():
    x = 0

    while x < 10:
        num = random.randint(-100, 100)
        num_sq = num*num

        try:
            assert square(num) == num_sq
        except AssertionError:
            print (f"{num} square was not {num_sq}")

        x += 1


if __name__ == "__main__":
    main()'''


#test calculator ver 4.0
from calculator import square
import pytest

def main():
    test_positive()
    test_negative()
    test_zero()


def test_positive():
    assert square(2) == 4
    assert square(3) == 9


def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9


def test_zero():
    assert square(0) == 0


def test_str():
    with pytest.raises(TypeError):
        square("cat")


if __name__ == "__main__":
    main()
