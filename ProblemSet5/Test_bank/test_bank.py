"""
Problem Set 5
Program: Back to the Bank
Alexis Varas Ortiz
"""
import pytest
from bank import value


def main():
    test_hello()
    test_h()
    test_other_greeting()
    test_error()

def test_hello():
    assert value("Hello") == 0


def test_h():
    assert value("Hey") == 20


def test_other_greeting():
    assert value("Good morning") == 100

def test_error():
    with pytest.raises(AttributeError):
        value(1)


if __name__ == "__main__":
    main()
