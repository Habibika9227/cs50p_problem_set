from bank import value

def test_greeting():
    assert value("hello")==0
    assert value("hey")==20
    assert value("yes")==100
    assert value("HELLO")==0
    assert value("HEY")==20
    assert value("YES")==100

