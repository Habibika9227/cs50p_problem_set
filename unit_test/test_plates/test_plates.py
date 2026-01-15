
from plates import is_valid

def test_is_valid():

    assert is_valid("AB123")==True
    assert is_valid("AB012")==False
    assert is_valid("AB12C")==False
    assert is_valid("cs50")==True
    assert is_valid("hellopiyt")==False
    assert is_valid("12wed")==False
    assert is_valid("w")==False
    assert is_valid("AB12!")==False
    assert is_valid("a1234")==False
    

if __name__=="__test_is_valid__":
    test_is_valid()
