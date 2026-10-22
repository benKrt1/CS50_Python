import pytest

from fuel import convert, gauge

def main():
    test_convert()
    test_gauge()


def test_convert():
    assert convert("1/2") == 50

    with pytest.raises(ValueError):
        convert("3/2")

    with pytest.raises(ZeroDivisionError):
        convert("1/0")

    with pytest.raises(ValueError):
        convert("1.5/3")

    with pytest.raises(ValueError):
        convert("cat/dog")

    with pytest.raises(ValueError):
        convert("1/2/3")

    with pytest.raises(ValueError):
        convert("-1/2")

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(2) == "2%"
    assert gauge(50) == "50%"
    assert gauge(98) == "98%"
    

if __name__ == "__main__":
    main()