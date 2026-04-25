import pytest
from jar import Jar 

def test_init():    
    
    assert Jar().capacity == 12
    assert Jar().size == 0
    assert Jar(12).capacity == 12
    


def test_str():
    
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5
    with pytest.raises(ValueError):
        jar.deposit(8)


def test_withdraw():
    jar = Jar()
    jar.deposit(10)
    jar.withdraw(3)
    assert jar.size == 7
    with pytest.raises(ValueError):
        jar.withdraw(8)
        