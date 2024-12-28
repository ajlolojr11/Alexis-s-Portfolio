# Problem Set 7
# Program: Test Working 9 to 5
# Alexis Varas Ortiz
# Description:
import pytest
from working import convert

def test_no_minutes():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"

def test_minutes():
    assert convert("9:30 AM to 5:30 PM") == "09:30 to 17:30"

def test_error():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5 PM")
    with pytest.raises(ValueError):
        convert("960 AM to 5 PM")
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")




