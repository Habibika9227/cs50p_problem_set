from twttr import shorten
 

def test_shorten():
    assert shorten("hello")=="hll"
    assert shorten("book")=="bk"
    assert shorten("AEIOU")==""
    assert shorten("HELLO")=="HLL"
    assert shorten("aeiou")==""
    assert shorten("12345") == "12345"          # numbers stay
    assert shorten("!@#$%^&*()") == "!@#$%^&*()"

