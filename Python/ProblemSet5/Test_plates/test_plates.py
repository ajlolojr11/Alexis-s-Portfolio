'''
Problem Set 5
Program: Re-requesting a Vanity Plate
Alexis Varas Ortiz
'''
from plates import is_valid


def main():
    test_alphanum()
    test_length()
    test_first_2char()
    test_end_num()


#test that there are only alphanumeric characters
def test_alphanum():
    assert is_valid("BO!123") == False

#test length is between 2-6 characters
def test_length():
    assert is_valid("B") == False
    assert is_valid("BOB1234") == False

#test if first 2 characters are letters
def test_first_2char():
    assert is_valid("B12345") == False

#test if plates has numbers and that they are all at the end
def test_end_num():
    assert is_valid("BO123B") == False

#tests that the first number is not a 0
def test_zero():
    assert is_valid("BO0123") == False


if __name__ == "__main__":
    main()
