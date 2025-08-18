'''
Problem Set 5
Program: Refuel
Alexis Varas Ortiz
'''

import pytest
from fuel import convert, gauge

def main():
    test_fuel()
    test_full()
    test_empty()

def test_fuel():
    assert convert("2/4") == 50
    assert gauge(50) == "50%"

def test_full():
    assert convert("99/100") == 99
    assert gauge(99) == "F"

def test_empty():
    assert convert("1/100") == 1
    assert gauge(1) == "E"

def test_error():
    with pytest.raises(ValueError):
        convert("4/1")

    with pytest.raises(ZeroDivisionError):
        convert("4/0")


if __name__ == "__main__":
    main()
