# Problem Set 7
# Program: Test Regular, um, Expressions
# Alexis Varas Ortiz
# Description: test the count function in um.py
from um import count

def test_um():
    assert count("Um") == 1
    assert count("Um, um, um") == 3

def test_no_um():
    assert count("Not stopping to think") == 0

def test_start_um():
    assert count("This should return 0; umbrella, umpire, umpteen") == 0

def test_end_um():
    assert count("This should return 0; sternum, vacuum, podium") == 0

def test_middle_um():
    assert count("This should return 0; lumber, human, costumer") == 0

def test_more_m():
    assert count("Ummmmmmm") == 0
