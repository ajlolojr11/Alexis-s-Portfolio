"""
Problem Set 5
Program: Testing my twttr
Author: Alexis Varas Ortiz
"""

from twttr import shorten


def main():
    test_lowercase()
    test_uppercase()
    test_numbers()


def test_lowercase():
    assert shorten("world") == "wrld"


def test_uppercase():
    assert shorten("HELLO") == "HLL"


def test_numbers():
    assert shorten("H3ll0, W0rld") == "H3ll0, W0rld"


if __name__ == "__main__":
    main()
