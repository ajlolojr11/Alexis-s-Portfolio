# Problem Set 8
# Program: Test Seasons of Love
# Alexis Varas Ortiz
# Description: test the functions/output in seasons.py
from datetime import date
from seasons import remove_and, calculate_minutes
import pytest


#Tests function that removes instances of the word "and"
def test_remove_and():
    assert remove_and("Three thousand") == "Three thousand"
    assert remove_and("Three thousand and four") == "Three thousand four"
    assert remove_and("Three hundred and forty thousand, eight hundred and sixty-four") == "Three hundred forty thousand, eight hundred sixty-four"

#Tests function that converts the age to minutes
def test_calculate_minutes():
    assert calculate_minutes(date(2024, 5, 20), date(2025, 5, 20)) == 525600
    assert calculate_minutes(date(2000, 1, 1), date(2025, 5, 20)) == 13350240

#Tests error handling when date is not in the correct format
def test_error():
    with pytest.raises(ValueError):
        calculate_minutes(date(2000, 13, 1), date(2025, 5, 20))


