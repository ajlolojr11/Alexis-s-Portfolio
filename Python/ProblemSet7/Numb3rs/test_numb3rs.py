# Problem Set 7
# Program: Test Numb3rs
# Alexis Varas Ortiz
# Description: test the validate function in Numb3rs.py
from numb3rs import validate


def test_correct():
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True


def test_pattern():
    assert validate("255001") == False
    assert validate("2555.0.0.1") == False
    assert validate("My ip address is 255.0.0.1") == False


def test_letters():
    assert validate("255.abc.0.1") == False


def test_range():
    assert validate("256.0.0.1") == False
    assert validate("255.387.0.1") == False
    assert validate("255.0.897.1") == False
    assert validate("255.0.0.621") == False
