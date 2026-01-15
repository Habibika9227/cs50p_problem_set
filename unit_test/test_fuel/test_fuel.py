import fuel 


def main():
    test_convert()
    test_gauge()
    test_convertError()
    test_zero_divisionError()
    test_non_int_error()
    negative_convert()
def test_convert():
    assert fuel.convert("3/5")==60
    assert fuel.convert("1/5")==20

def test_convertError():
    try:
        fuel.convert("3/2")
        assert False
    except ValueError:
        assert True

    
def test_zero_divisionError():
    try:
        fuel.convert("1/0")
        assert False

    except ZeroDivisionError:
        assert True
   
def test_non_int_error():
    try:
        fuel.convert("a/b")
        assert False
    except ValueError:
        assert True
def negative_convert():
    try:
        fuel.convert("-1/2")
        assert False
    except ValueError:
        assert True
    try:
        fuel.convert("1/-5")
        assert False
    except ValueError:
        assert True
def test_gauge():
    assert fuel.gauge(1)=="E"
    assert fuel.gauge(99)=="F"
    assert fuel.gauge(100)=="F"
    assert fuel.gauge(20)=="20%"

if __name__=="__main__":
    main()