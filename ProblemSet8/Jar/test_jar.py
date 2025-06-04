# Problem Set 8
# Program: Test Cokies Jar
# Alexis Varas Ortiz
# Description: test the instance methods of the Jar class
from jar import Jar
import pytest


#Tests initializing a Jar object
def test_init():
    jar = Jar() #initialize Jar object(default capacity=12)
    assert jar.capacity == 12
    jar = Jar(10)#initialize Jar object with a capacity of 10
    assert jar.capacity == 10


#Test calling the __str__ function
def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


#Test using the deposit method/adding a cookie to the jar
def test_deposit():
    jar = Jar()
    jar.deposit(4) #Add 4 cookies to the jar
    assert jar.size == 4
    jar.deposit(2) #Add 2 more
    assert jar.size == 6


#Test using the withdraw method/removing a cookie to the jar
def test_withdraw():
    jar = Jar()
    jar.deposit(10)#Add 10 cookies to the jar
    jar.withdraw(1)#Remove 1 cookies from the jar
    assert jar.size == 9
    jar.withdraw(4)#Remove 4 more cookies from the jar
    assert jar.size == 5


#Test error messages triggering properly
def test_error():
    with pytest.raises(ValueError): #Adds more cookies than the set  capacity
        jar = Jar(10)
        jar.deposit(11)

    with pytest.raises(ValueError): #Withdraws more cookes than are available
        jar = Jar(10)
        jar.deposit(8)
        jar.withdraw(9)

    with pytest.raises(ValueError): #Sets capacity with a negative integer
        jar = Jar(-2)


